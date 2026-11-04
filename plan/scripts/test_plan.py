import copy,json,shutil,tempfile,unittest
from pathlib import Path
from check import validate,ROOT
from render import outputs
from status import set_status

class PlanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.baseline=json.loads((ROOT/'plan/registry.json').read_text())
    def setUp(self):self.d=copy.deepcopy(self.baseline)
    def errors(self):return '\n'.join(validate(self.d,check_generated=False))
    def test_baseline_and_generated_files_pass(self):self.assertEqual(validate(self.d),[])
    def test_duplicate_id_is_rejected(self):
        self.d['tasks'][1]['id']=self.d['tasks'][0]['id'];self.assertIn('Duplicate/missing tasks',self.errors())
    def test_removed_baseline_id_is_rejected(self):
        self.d['tasks'].pop();self.assertIn('Baseline task removed',self.errors())
    def test_missing_dependency_is_rejected(self):
        self.d['tasks'][0]['depends_on']=['INV-99999'];self.assertIn('Unknown dependency',self.errors())
    def test_dependency_cycle_is_rejected(self):
        a,b=self.d['tasks'][:2];a['depends_on']=[b['id']];b['depends_on']=[a['id']];self.assertIn('Dependency cycle',self.errors())
    def test_future_phase_dependency_is_rejected(self):
        self.d['tasks'][0]['depends_on']=[self.d['tasks'][-1]['id']];self.assertIn('Future-phase dependency',self.errors())
    def test_empty_lens_is_rejected(self):
        self.d['modules'][0]['coverage']['DATA']={'tasks':[]};self.assertIn('Empty task coverage',self.errors())
    def test_missing_lens_is_rejected(self):
        self.d['modules'][0]['coverage'].pop('PRIVACY');self.assertIn('Incomplete coverage',self.errors())
    def test_unexplained_na_is_rejected(self):
        self.d['modules'][0]['coverage']['DATA']={'na':''};self.assertIn('Missing N/A reason',self.errors())
    def test_orphan_task_is_rejected(self):
        self.d['modules'][0]['coverage']['AUTHZ']={'na':'Deliberately remove coverage to test the checker.'};self.assertIn('Orphan task',self.errors())
    def test_module_dependency_must_exist_in_task_graph(self):
        self.d['modules'][-1]['depends_on'].append('M01');self.assertIn('Module dependency not implemented',self.errors())
    def test_feature_requires_valid_source_and_test(self):
        self.d['features'][0]['source']='S999';self.d['features'][0]['tests']=['T-NONE'];e=self.errors();self.assertIn('Unknown feature owner/source',e);self.assertIn('Invalid feature test',e)
    def test_entity_owner_must_be_data_task(self):
        self.d['entities'][0]['owner_task']=self.d['tasks'][0]['id'];self.assertIn('Invalid entity owner',self.errors())
    def test_api_owner_and_duplicates_are_checked(self):
        self.d['endpoints'][0]['owner_task']=self.d['tasks'][0]['id'];self.d['endpoints'].append(copy.deepcopy(self.d['endpoints'][0]));e=self.errors();self.assertIn('Invalid API owner',e);self.assertIn('Duplicate endpoint',e)
    def test_active_task_requires_completed_prerequisites(self):
        self.d['tasks'][1]['status']='~';self.assertIn('Incomplete prerequisite',self.errors())
    def test_two_active_tasks_are_rejected(self):
        self.d['tasks'][0]['status']='~';self.d['tasks'][1]['status']='~';self.assertIn('More than one active task',self.errors())
    def test_started_screen_requires_design_evidence(self):
        sid=self.d['screens'][0];t=next(t for t in self.d['tasks'] if t['id']==sid['build_task']);t['status']='~';self.assertIn('Missing design evidence',self.errors())
    def test_placeholder_design_artifact_is_rejected(self):
        s=self.d['screens'][0];s.update(status='designed',artifact='https://example.com/design',reviewer='Reviewer');self.assertIn('Placeholder design evidence',self.errors())
    def test_critical_scenario_is_owned_and_required(self):
        self.d['critical_scenarios'][0]['id']='C-UNKNOWN';self.assertIn('Critical scenario not required',self.errors())
    def test_missing_exclusion_reason_is_rejected(self):
        self.d['exclusions'][0]['reason']='';self.assertIn('Unexplained exclusion',self.errors())
    def test_renderer_is_deterministic_and_nonmutating(self):
        before=copy.deepcopy(self.d);self.assertEqual(outputs(self.d),outputs(self.d));self.assertEqual(self.d,before)
    def test_status_update_preserves_ids_and_other_statuses(self):
        before=copy.deepcopy(self.d);after=set_status(self.d,self.d['tasks'][0]['id'],'~');self.assertEqual(self.d,before)
        self.assertEqual([t['id'] for t in after['tasks']],[t['id'] for t in before['tasks']]);self.assertEqual(after['tasks'][1:],before['tasks'][1:]);self.assertEqual(after['tasks'][0]['status'],'~')
        self.assertIn('- [~] '+after['tasks'][0]['id'],outputs(after)['plan/tasks.md'])
    def test_unknown_task_status_is_rejected(self):
        with self.assertRaisesRegex(ValueError,'Unknown task'):set_status(self.d,'INV-99999','~')
    def test_generated_drift_and_broken_links_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp)/'plan-copy';shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('__pycache__'))
            p=root/'plan/tasks.md';p.write_text(p.read_text()+'\nDrift\n')
            self.assertTrue(any('Generated document drift' in e for e in validate(self.d,root)))
            p.write_text(outputs(self.d)['plan/tasks.md'])
            (root/'README.md').write_text('[broken](plan/absent.md)')
            self.assertTrue(any('Broken local link' in e for e in validate(self.d,root)))
    def test_missing_required_document_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            self.assertTrue(any('Missing required document' in e for e in validate(self.d,Path(temp),False)))

if __name__=='__main__':unittest.main()
