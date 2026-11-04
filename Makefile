PYTHON ?= python3
.PHONY: plan-check plan-render plan-test task-status
plan-check:
	$(PYTHON) plan/scripts/check.py
plan-render:
	$(PYTHON) plan/scripts/render.py
plan-test:
	$(PYTHON) -m unittest discover -s plan/scripts -p 'test_*.py' -v
task-status:
	$(PYTHON) plan/scripts/status.py "$(ID)" "$(STATUS)"
