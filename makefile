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

#RunDiplomacy.tmp: RunDiplomacy1.in RunDiplomacy2.in RunDiplomacy3.in RunDiplomacy4.in RunDiplomacy5.in RunDiplomacy1.out RunDiplomacy2.out RunDiplomacy3.out RunDiplomacy4.out RunDiplomacy5.out RunDiplomacy.py
#	$(PYTHON) RunDiplomacy.py < RunDiplomacy1.in > RunDiplomacy1.tmp
#	$(PYTHON) RunDiplomacy.py < RunDiplomacy2.in > RunDiplomacy2.tmp
#	$(PYTHON) RunDiplomacy.py < RunDiplomacy3.in > RunDiplomacy3.tmp
#	$(PYTHON) RunDiplomacy.py < RunDiplomacy4.in > RunDiplomacy4.tmp
#	$(PYTHON) RunDiplomacy.py < RunDiplomacy5.in > RunDiplomacy5.tmp
#	diff --strip-trailing-cr RunDiplomacy1.tmp RunDiplomacy1.out
#	diff --strip-trailing-cr RunDiplomacy2.tmp RunDiplomacy2.out
#	diff --strip-trailing-cr RunDiplomacy3.tmp RunDiplomacy3.out
#	diff --strip-trailing-cr RunDiplomacy4.tmp RunDiplomacy4.out
#	diff --strip-trailing-cr RunDiplomacy5.tmp RunDiplomacy5.out

tests.tmp: tests.py
	$(COVERAGE) run    --branch tests.py >  tests.tmp 2>&1
	$(COVERAGE) report -m                      >> tests.tmp
	cat tests.tmp

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

test: models.html IDB2.log tests.tmp
