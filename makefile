.PHONY: Ephemeral.log


ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3
    PIP      := pip3
    PYLINT   := pylint
    COVERAGE := coverage
    PYDOC    := pydoc3
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Windows
    PYTHON   := python                 
    PIP      := pip3
    PYLINT   := pylint
    COVERAGE := coverage
    PYDOC    := python -m pydoc        
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3
    PIP      := pip3
    PYLINT   := pylint3
    COVERAGE := coverage
    PYDOC    := pydoc3
    AUTOPEP8 := autopep8
endif

models.html: models.py
	$(PYDOC) -w models

IDB2.log:
	git log > IDB2.log

test_results.txt: test.py
	$(PIP) install -r requirements.txt
	$(COVERAGE) run    test.py >  test_results.txt 2>&1
	$(COVERAGE) report -m      >> test_results.txt
	cat test_results.txt

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  *.tmp
	rm -rf __pycache__

config:
	git config -l

format:
	$(AUTOPEP8) -i models.py
	$(AUTOPEP8) -i tests.py
	$(AUTOPEP8) -i main.py

scrub:
	make clean
	rm -f  models.html
	rm -f  IDB2.log
	rm -f test_results.txt

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

versions:
	which       $(AUTOPEP8)
	$(AUTOPEP8) --version
	@echo
	which       $(COVERAGE)
	$(COVERAGE) --version
	@echo
	which       git
	git         --version
	@echo
	which       make
	make        --version
	@echo
	which       $(PIP)
	$(PIP)      --version
	@echo
	which       $(PYLINT)
	$(PYLINT)   --version
	@echo
	which        $(PYTHON)
	$(PYTHON)    --version

test: scrub models.html IDB2.log test_results.txt
