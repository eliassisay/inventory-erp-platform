#!/usr/bin/env python3
"""Offline structural/traceability validator. No application correctness claims."""
import json,re
from pathlib import Path
from collections import Counter
from render import outputs,ROOT

REQUIRED=['README.md','AGENTS.md','Makefile','plan/README.md','plan/PRODUCT_REQUIREMENTS.md','plan/ARCHITECTURE.md','plan/DECISIONS.md','plan/DATABASE_SCHEMA.md','plan/API_REFERENCE.md','plan/INVARIANTS.md','plan/WORKFLOWS.md','plan/LIFECYCLES.md','plan/OFFLINE_SYNC.md','plan/PERMISSIONS.md','plan/APPROVALS.md','plan/DESIGN_SYSTEM.md','plan/EVENTS_AUDIT.md','plan/PRIVACY.md','plan/LOCALIZATION.md','plan/TEST_STRATEGY.md','plan/RELEASE_GATE.md','plan/MIGRATION.md','plan/OPERATIONS.md','plan/SETUP.md','plan/RISKS.md','plan/SCOPE_CONTROL.md','plan/INBOX.md','plan/GLOSSARY.md','plan/releases/TEMPLATE.md']
LENSES={'DATA','API','AUTHZ','LIFE','DESIGN','BUILD','NOTIFY','ADMIN','AUDIT','EVENTS','PRIVACY','QA','INTEGRATION','OFFLINE','OPERABILITY'}

def validate(d,root=ROOT,check_generated=True):
    errors=[]
    def need(ok,msg):
        if not ok:errors.append(msg)
    for key in ['modules','tasks','features','screens','entities','endpoints','scenarios','sources','phases','exclusions','critical_scenarios']:
        need(isinstance(d.get(key),list),f'Missing collection {key}')
    if errors:return errors
    def unique(seq,key,label):
        counts=Counter(x.get(key) for x in seq)
        for k,c in counts.items():need(k is not None and c==1,f'Duplicate/missing {label}: {k}')
    for field,key in [('modules','id'),('tasks','id'),('features','id'),('screens','id'),('entities','name'),('scenarios','id'),('sources','id'),('phases','id'),('exclusions','id'),('critical_scenarios','id')]:unique(d[field],key,field)
    ts={t['id']:t for t in d['tasks']}; ms={m['id']:m for m in d['modules']}; fs={f['id']:f for f in d['features']};ss={s['id']:s for s in d['screens']};sc={s['id']:s for s in d['scenarios']};src={s['id']:s for s in d['sources']};ph={p['id'] for p in d['phases']}
    need(set(d.get('lenses',[]))==LENSES,'Lens registry must contain all 15 lenses')
    need(ph==set(range(1,14)),'All 13 phases required')
    baseline=d.get('baseline_task_ids',[])
    need(len(baseline)==len(set(baseline)) and bool(baseline),'Invalid frozen baseline IDs')
    for tid in baseline:need(tid in ts,f'Baseline task removed: {tid}')
    for t in d['tasks']:
        tid=t['id'];need(bool(re.fullmatch(r'INV-\d{3,}',tid)),f'Invalid task ID {tid}')
        need(t['module'] in ms,f'Unknown task module {tid}')
        need(t.get('status') in [' ','~','?','x'],f'Invalid status {tid}')
        need(t.get('phase') in ph,f'Unknown phase {tid}')
        need(t.get('lens') in LENSES,f'Unknown lens {tid}')
        if t['module'] in ms:need(t['phase']==ms[t['module']]['phase'],f'Task phase mismatch {tid}')
        for field in ['discipline','title','deliverable','acceptance','tests']:
            v=t.get(field);need(bool(v) and (not isinstance(v,list) or all(isinstance(x,str) and x.strip() for x in v)),f'Missing {field} in {tid}')
        if tid not in baseline:need(t.get('scope_delta') is True and bool(t.get('reason')) and bool(t.get('decision')),f'Unapproved scope delta {tid}')
        need(len(t['depends_on'])==len(set(t['depends_on'])),f'Duplicate dependency {tid}')
        for dep in t['depends_on']:
            need(dep in ts,f'Unknown dependency {tid} -> {dep}')
            if dep in ts:
                need(ts[dep]['phase']<=t['phase'],f'Future-phase dependency {tid} -> {dep}')
                if t['status'] in ['~','?','x']:need(ts[dep]['status']=='x',f'Incomplete prerequisite {tid} -> {dep}')
        for sid in t.get('screens',[]):need(sid in ss,f'Unknown screen on {tid}: {sid}')
    need(sum(t['status']=='~' for t in d['tasks'])<=1,'More than one active task')
    seen=set();active=set()
    def visit(tid):
        if tid in active:errors.append(f'Dependency cycle at {tid}');return
        if tid in seen or tid not in ts:return
        active.add(tid)
        for dep in ts[tid]['depends_on']:visit(dep)
        active.remove(tid);seen.add(tid)
    for tid in ts:visit(tid)
    for m in d['modules']:
        mid=m['id'];need(m['phase'] in ph,f'Unknown module phase {mid}');need(m['source'] in src,f'Unknown source {mid}')
        need(set(m.get('coverage',{}))==LENSES,f'Incomplete coverage {mid}')
        for lens,cell in m.get('coverage',{}).items():
            need(set(cell) in [{'tasks'},{'na'}],f'Invalid coverage cell {mid}/{lens}')
            if 'tasks' in cell:
                need(bool(cell['tasks']),f'Empty task coverage {mid}/{lens}')
                for tid in cell['tasks']:need(tid in ts and ts[tid]['module']==mid and ts[tid]['lens']==lens,f'Wrong coverage owner {mid}/{lens}: {tid}')
            if 'na' in cell:need(isinstance(cell['na'],str) and len(cell['na'].strip())>=20,f'Missing N/A reason {mid}/{lens}')
        for t in [t for t in d['tasks'] if t['module']==mid]:need(t['id'] in m.get('coverage',{}).get(t['lens'],{}).get('tasks',[]),f'Orphan task {t["id"]}')
        for dep in m['depends_on']:
            need(dep in ms,f'Unknown module dependency {mid}/{dep}')
            if dep in ms:
                need(ms[dep]['phase']<=m['phase'],f'Future module dependency {mid}/{dep}')
                prereq=set(ms[dep]['coverage']['QA']['tasks'])
                need(any(prereq.intersection(t['depends_on']) for t in d['tasks'] if t['module']==mid),f'Module dependency not implemented in task graph {mid}/{dep}')
        module_features=[f for f in d['features'] if f['module']==mid]
        need({f['title'] for f in module_features}=={f['title'] for f in m['features']},f'Module/feature drift {mid}')
        need({e['name'] for e in d['entities'] if e['module']==mid}=={e[0] for e in m['tables']},f'Module/entity drift {mid}')
        need({e['method']+' '+e['path'].removeprefix('/api/v1') for e in d['endpoints'] if e['module']==mid}==set(m['routes']),f'Module/endpoint drift {mid}')
    for f in d['features']:
        need(f['module'] in ms and f['source'] in src,f'Unknown feature owner/source {f["id"]}')
        if f['module'] in ms:need(f['phase']==ms[f['module']]['phase'],f'Feature phase mismatch {f["id"]}')
        need(f.get('disposition')=='included',f'Invalid baseline disposition {f["id"]}')
        need(bool(f.get('requirement')) and bool(f.get('tasks')) and bool(f.get('tests')),f'Incomplete feature {f["id"]}')
        for tid in f['tasks']:need(tid in ts and ts[tid]['module']==f['module'],f'Wrong feature task {f["id"]}/{tid}')
        need(any(ts.get(t,{}).get('lens')=='LIFE' for t in f['tasks']),f'Feature has no delivery task {f["id"]}')
        for sid in f['tests']:need(sid in sc and sc[sid]['feature']==f['id'],f'Invalid feature test {f["id"]}/{sid}')
    for s in d['scenarios']:
        need(s['feature'] in fs and s['module'] in ms,f'Unknown scenario owner {s["id"]}')
        need(s['task'] in ts and ts[s['task']]['lens']=='QA' and ts[s['task']]['module']==s['module'],f'Invalid QA owner {s["id"]}')
        for field in ['given','when','then','negative']:need(bool(s.get(field)),f'Missing scenario {field}: {s["id"]}')
    for c in d['critical_scenarios']:
        need(bool(c.get('steps')) and bool(c.get('expected')),f'Incomplete critical scenario {c["id"]}')
        need(c['task'] in ts and ts[c['task']]['lens']=='QA',f'Invalid critical test owner {c["id"]}')
        for m in c['modules']:need(m in ms,f'Unknown critical module {c["id"]}')
        need(any(c['id'] in s for s in ts.get(c['task'],{}).get('tests',[])),f'Critical scenario not required by QA task {c["id"]}')
    for e in d['entities']:
        need(e['owner_task'] in ts and ts[e['owner_task']]['module']==e['module'] and ts[e['owner_task']]['lens']=='DATA',f'Invalid entity owner {e["name"]}')
        need(bool(e['fields']) and e['scope'] in ['platform','tenant','company','global-reference'],f'Invalid entity contract {e["name"]}')
    ep=Counter((e['method'],e['path']) for e in d['endpoints'])
    for k,n in ep.items():need(n==1,f'Duplicate endpoint {k}')
    for e in d['endpoints']:
        need(e['owner_task'] in ts and ts[e['owner_task']]['module']==e['module'] and ts[e['owner_task']]['lens']=='API',f'Invalid API owner {e["path"]}')
        need(e['path'].startswith('/api/v1/') and e['method'] in ['GET','POST','PUT','PATCH','DELETE'],f'Invalid endpoint {e["path"]}')
        need(bool(e.get('roles')),f'Missing endpoint access persona {e["path"]}')
    for s in d['screens']:
        for field,lens in [('design_task','DESIGN'),('build_task','BUILD')]:need(s[field] in ts and ts[s[field]]['lens']==lens and ts[s[field]]['module']==s['module'],f'Invalid screen owner {s["id"]}')
        need(s['status'] in ['planned','designed','built'],f'Invalid screen status {s["id"]}')
        if s['status'] in ['designed','built'] or ts.get(s['build_task'],{}).get('status') in ['~','?','x']:
            a=s.get('artifact');need(bool(a) and bool(s.get('reviewer')),f'Missing design evidence {s["id"]}')
            if a:
                need(not any(x in a.lower() for x in ['placeholder','example.com','todo']),f'Placeholder design evidence {s["id"]}')
                if not a.startswith('https://'):need((root/a).is_file(),f'Missing design artifact {s["id"]}')
            need(ts[s['design_task']]['status']=='x',f'Design not accepted {s["id"]}')
        if ts.get(s['build_task'],{}).get('status') in ['~','?','x']:need(s['status'] in ['designed','built'],f'Undesigned build started {s["id"]}')
    for x in d['exclusions']:
        need(x['disposition'] in ['excluded','later phase'] and x.get('baseline') is False,f'Invalid exclusion disposition {x["id"]}')
        need(bool(x.get('reason')) and bool(x.get('revisit_trigger')),f'Unexplained exclusion {x["id"]}')
    for s in d['sources']:
        need(bool(s.get('version')) and bool(s.get('checked_on')) and bool(s.get('finding')) and bool(s.get('decision')),f'Incomplete source {s["id"]}')
        need(s['id']=='S00' or str(s.get('url','')).startswith('https://'),f'Missing research URL {s["id"]}')
    for name in REQUIRED:need((root/name).is_file(),f'Missing required document {name}')
    for file in root.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)',file.read_text()):
            if '://' not in target and not target.startswith('#'):
                need((file.parent/target.split('#')[0]).exists(),f'Broken local link {file.relative_to(root)} -> {target}')
    if check_generated and not errors:
        for name,content in outputs(d).items():need((root/name).exists() and (root/name).read_text()==content,f'Generated document drift: {name}')
    return errors

def main():
    try:d=json.loads((ROOT/'plan/registry.json').read_text());errs=validate(d)
    except (ValueError,KeyError,TypeError) as ex:print(f'ERROR: malformed registry: {ex}');return 1
    for err in errs:print('ERROR:',err)
    print(f"{len(d['modules'])} modules; {len(d['tasks'])} tasks; {len(d['features'])} capabilities; {len(d['endpoints'])} endpoints; {len(d['entities'])} entities; {len(d['screens'])} screens; {len(errs)} errors.")
    delta=[t['id'] for t in d['tasks'] if t['id'] not in d['baseline_task_ids']]
    print('Scope delta:',', '.join(delta) or 'none')
    return int(bool(errs))
if __name__=='__main__':raise SystemExit(main())
