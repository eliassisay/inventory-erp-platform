#!/usr/bin/env python3
"""Validated task-state mutation; only registry owns task status."""
import argparse,json,os
from check import validate,ROOT
from render import outputs

def set_status(d,tid,status,root=ROOT):
    import copy
    updated=copy.deepcopy(d)
    task=next((t for t in updated['tasks'] if t['id']==tid),None)
    if task is None:raise ValueError('Unknown task '+tid)
    if status not in [' ','~','?','x']:raise ValueError('Status must be space, ~, ?, or x')
    task['status']=status
    errors=validate(updated,root,check_generated=False)
    if errors:raise ValueError('\n'.join(errors))
    return updated

def main():
    ap=argparse.ArgumentParser();ap.add_argument('task');ap.add_argument('status');a=ap.parse_args()
    p=ROOT/'plan/registry.json';d=json.loads(p.read_text())
    current_errors=validate(d)
    if current_errors:print('\n'.join(current_errors));return 1
    try:updated=set_status(d,a.task,a.status)
    except ValueError as ex:print(ex);return 1
    tmp=p.with_suffix('.json.tmp');tmp.write_text(json.dumps(updated,indent=2,ensure_ascii=False)+'\n');os.replace(tmp,p)
    for name,body in outputs(updated).items():(ROOT/name).write_text(body)
    print(f'{a.task} is [{a.status}]; task IDs preserved.');return 0
if __name__=='__main__':raise SystemExit(main())
