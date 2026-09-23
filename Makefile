.PHONY: all run-script run-server

all: run-md-build-script run-server

run-server:
	python3 -m http.server 8000

run-md-build-script:
	python3.14 scripts/convert-files.py
