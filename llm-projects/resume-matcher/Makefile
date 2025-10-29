
# Makefile for Steve's Resume Matcher

RESUME=resume.md
MODEL=gpt-4o
SCRIPT=resume_matcher.py
INSTALL_PATH=$(HOME)/bin

all: words

words:
	wc -l $(RESUME)

install:
	mkdir -p $(INSTALL_PATH)
	cp $(SCRIPT) $(INSTALL_PATH)/resume_matcher.py
	echo "Installed $(SCRIPT) to $(INSTALL_PATH)"
