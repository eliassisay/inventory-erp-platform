#!/usr/bin/env python3
"""Render reviewed registry data. IDs/statuses are never inferred or reassigned."""
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def table(headers,rows):
    esc=lambda v:str(v).replace('|','&#124;').replace('\n',' ')
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(esc(x) for x in row)+' |' for row in rows])+'\n'

def outputs(d):
    out={}; tasks=d['tasks']; mods=d['modules']; tm={x['id']:x for x in tasks}; mm={x['id']:x for x in mods}
    banner=f"> Registry baseline {d['baseline']} · {d['date']} · {len(mods)} modules · {len(tasks)} tasks · {len(d['features'])} capabilities · {len(d['phases'])} phases. Generated; edit registry.json and run `make plan-render`.\n\n"
    text='# Inventory ERP — Roadmap\n\n'+banner+'All phases belong to the full baseline. No production stock go-live occurs before valuation, migration and launch gates pass. Planning artifacts exist; application work is not implemented. Phase gates are documented in RELEASE_GATE.md.\n\n'
    text+=table(['Phase','Name','Modules','Tasks','Entry gate'],[(p['id'],p['name'],', '.join(m['id'] for m in mods if m['phase']==p['id']),sum(t['phase']==p['id'] for t in tasks),'Approved baseline' if p['id']==1 else f"Previous phase gate passed; same-phase task dependencies completed") for p in d['phases']])
    for p in d['phases']:
        pt=[t for t in tasks if t['phase']==p['id']]
        text+=f"\n## Phase {p['id']} — {p['name']}\n\nTasks: {pt[0]['id']}–{pt[-1]['id']} ({len(pt)}).\n\n**Exit:** {p['exit_criteria']}\n\n"
        text+='\n'.join(f"- {m['id']} {m['name']}: "+'; '.join(f['title'] for f in m['features'])+'.' for m in mods if m['phase']==p['id'])+'\n'
    text+='\n## Deliberate boundaries\n\n'+table(['ID','Capability','Disposition','Reason','Revisit trigger'],[(x['id'],x['feature'],x['disposition'],x['reason'],x['revisit_trigger']) for x in d['exclusions']])
    out['plan/ROADMAP.md']=text
    text='# Inventory ERP — Implementation tasks\n\n'+banner+'Statuses: `[ ]` planned, `[~]` active, `[?]` verified awaiting review, `[x]` accepted/merged. At most one active task. Use `make task-status ID=INV-001 STATUS=~`; status is stored in registry.json, never copied from generated Markdown. No software task is claimed complete by this planning delivery.\n\n'
    for p in d['phases']:
        text+=f"## Phase {p['id']} — {p['name']}\n\n"
        for m in [m for m in mods if m['phase']==p['id']]:
            text+=f"### {m['id']} · {m['name']}\n\n"
            for t in [t for t in tasks if t['module']==m['id']]:
                text+=f"- [{t['status']}] {t['id']} · `{t['discipline']}` · `{m['id']}·{t['lens']}` · {t['title']}\n"
                text+=f"  - Depends on: {', '.join(t['depends_on']) or 'none'}.\n  - Deliverable: {t['deliverable']}\n"
                text+='  - Acceptance: '+' '.join(t['acceptance'])+'\n  - Tests: '+' '.join(t['tests'])+'\n'
                if t['screens']: text+='  - Screens: '+', '.join(t['screens'])+'.\n'
                text+='\n'
    out['plan/tasks.md']=text
    text='# Module registry and completeness matrix\n\n'+banner+'The 15 lenses are DATA, API, AUTHZ, LIFE, DESIGN, BUILD, NOTIFY, ADMIN, AUDIT, EVENTS, PRIVACY, QA, INTEGRATION, OFFLINE and OPERABILITY. No blank cell is allowed. N/A means the stated boundary, not forgotten work.\n\n'
    text+=table(['Module']+d['lenses'],[(m['id']+' '+m['name'],*[len(m['coverage'][l]['tasks']) if 'tasks' in m['coverage'][l] else 'N/A' for l in d['lenses']]) for m in mods])
    for m in mods:
        text+=f"\n## {m['id']} — {m['name']}\n\nPhase {m['phase']}; prerequisites: {', '.join(m['depends_on']) or 'none'}; intended roles: {', '.join(m['roles'])}.\n\n"
        text+=table(['Lens','Owner tasks or explicit exception'],[(l,', '.join(m['coverage'][l]['tasks']) if 'tasks' in m['coverage'][l] else 'N/A: '+m['coverage'][l]['na']) for l in d['lenses']])
    out['plan/MODULES.md']=text
    text='# Feature coverage and disposition\n\n'+banner+'Every included feature has a delivery task and acceptance-test owner. Later-phase exclusions are outside this frozen baseline until change control admits them. References S00 are explicit product decisions, not claimed external research.\n\n'
    text+=table(['Feature','Requirement','Disposition','Source','Module / phase','Tasks','Tests'],[(f['id']+' '+f['title'],f['requirement'],f['disposition'],f['source'],f"{f['module']} / P{f['phase']}",', '.join(f['tasks']),', '.join(f['tests'])) for f in d['features']])
    text+='\n## Excluded and future scope\n\n'+table(['ID','Feature','Disposition','Reason','Revisit'],[(x['id'],x['feature'],x['disposition'],x['reason'],x['revisit_trigger']) for x in d['exclusions']])
    out['plan/COVERAGE.md']=text
    text='# Research and source register\n\n'+banner+'Research date: 2026-11-04 (Africa/Addis_Ababa). Official references only. Odoo 19.0 is a versioned functional baseline, not a claim to be its newest release or match its editions. Findings below are short paraphrases; the adopted behavior is our product decision. Recheck links and version/license support before implementation.\n\n'
    for s in d['sources']:
        link=f"[{s['title']}]({s['url']})" if s['url'] else s['title']
        text+=f"## {s['id']} — {link}\n\nVersion: {s['version']}. Checked: {s['checked_on']}.\n\nFinding: {s['finding']}\n\nDecision / difference: {s['decision']}\n\nCoverage: "+', '.join(m['id'] for m in mods if m['source']==s['id'])+'.\n\n'
    text+='## Research limits and implementation gates\n\nNo official Ethiopian e-invoicing interface or sector-specific certification was verified for this package. Tax invoice issuance is excluded. The localization review must establish whether inventory documents, hosting, personal data transfers and retention impose additional requirements, record qualified review and block launch on unresolved applicability. No tax rates, legal retention periods or statutory compliance certification are assumed. See LOCALIZATION.md.\n'
    out['plan/RESEARCH.md']=text
    text='# Screen inventory and design gate\n\n'+banner+'Each screen ID includes its list/work queue, detail/history, and action forms. Shared shell/design primitives live in M11/M12. BUILD cannot enter active/review/done state until its design is approved with a real artifact and reviewer. Every screen includes error, empty, denied, loading and relevant lifecycle/offline states.\n\n'
    text+=table(['ID','Screen family','Surface','Design owner','Build owner','Status','Artifact','Reviewer'],[(s['id'],s['title'],', '.join(s['surfaces']),s['design_task'],s['build_task'],s['status'],s['artifact'] or 'Not designed',s['reviewer'] or 'Unassigned') for s in d['screens']])
    out['plan/SCREENS.md']=text
    text='# Entity ownership and conceptual schema\n\n'+banner+'Read DATABASE_SCHEMA.md for common column types, scope constraints, invariants and relationships. Every row below has a migration owner. These are planned entities, not deployed tables.\n\n'
    text+=table(['Entity','Module','Migration task','Scope','Domain fields'],[(e['name'],e['module'],e['owner_task'],e['scope'],', '.join(e['fields'])) for e in d['entities']])
    out['plan/ENTITIES.md']=text
    text='# Endpoint ownership registry\n\n'+banner+'All paths are under /api/v1. API_REFERENCE.md supplies request conventions, command DTOs, resource contracts and error semantics. Each endpoint must receive a concrete Zod/OpenAPI schema in its API task before a client is built. Roles listed are personas; PERMISSIONS.md maps them to explicit actions and scope grants.\n\n'
    text+=table(['Method','Path','Module','Owner task','Intended roles'],[(e['method'],e['path'],e['module'],e['owner_task'],', '.join(e['roles'])) for e in d['endpoints']])
    out['plan/ENDPOINTS.md']=text
    text='# Acceptance scenarios\n\n'+banner+'These are required application tests, not tests claimed to have run. The planning checker validates ownership and coverage; software implementation must produce the actual evidence.\n\n'
    for s in d['scenarios']:
        text+=f"## {s['id']} — {s['when']}\n\nFeature {s['feature']} · module {s['module']} · QA task {s['task']}.\n\n- Given: {s['given']}.\n- When: {s['when']}.\n- Then: {s['then']}\n- Negative: {s['negative']}\n\n"
    text+='## Cross-module critical scenarios\n\n'
    for s in d.get('critical_scenarios',[]):
        text+=f"### {s['id']} — {s['title']}\n\nOwner: {s['task']}; modules: {', '.join(s['modules'])}.\n\n{s['steps']}\n\nExpected: {s['expected']}\n\n"
    out['plan/ACCEPTANCE.md']=text
    text='# Work breakdown by discipline\n\n'+banner
    for discipline in sorted({t['discipline'] for t in tasks}):
        text+=f'## {discipline}\n\n'+table(['Task','Phase','Module / lens','Deliverable'],[(t['id'],t['phase'],t['module']+' / '+t['lens'],t['title']) for t in tasks if t['discipline']==discipline])+'\n'
    out['plan/WBS.md']=text
    text='# Permission and role ownership\n\n'+banner+'Each module permission family uses `<module>.view`, `.manage`, `.submit`, `.approve`, `.post`, `.export` only where the action exists. The AUTHZ task declares concrete route/action permissions before use; roles never bypass scope checks. See PERMISSIONS.md for default persona grants and independent approval rules.\n\n'
    text+=table(['Module','Roles','AUTHZ task','Approval/lifecycle owners'],[(m['id']+' '+m['name'],', '.join(m['roles']),', '.join(m['coverage']['AUTHZ']['tasks']),', '.join(m['coverage']['LIFE']['tasks'])) for m in mods])
    out['plan/ROLE_OWNERS.md']=text
    return {name: body.rstrip() + '\n' for name, body in out.items()}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args()
    d=json.loads((ROOT/'plan/registry.json').read_text()); mismatches=[]
    for name,body in outputs(d).items():
        p=ROOT/name
        if args.check:
            if not p.exists() or p.read_text()!=body: mismatches.append(name)
        else:p.write_text(body)
    if mismatches:
        print('Generated files differ: '+', '.join(mismatches));return 1
    print(f"{'Checked' if args.check else 'Rendered'} {len(outputs(d))} documents; IDs and statuses unchanged.");return 0
if __name__=='__main__':raise SystemExit(main())
