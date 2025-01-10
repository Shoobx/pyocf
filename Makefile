root_dir := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
ifdef NO_VENV
bin_dir :=
python_exe := python3
endif
ifndef NO_VENV
bin_dir := $(root_dir)/ve/bin/
python_exe := $(bin_dir)python3
endif
git_source := https://github.com/regebro/Open-Cap-Format-OCF.git
git_branch := lregebro-v1.2.0

all: devenv fetch build

build: generate check docs

# The fullrelease script is a part of zest.releaser, which is the last
# package installed, so if it exists, the devenv is installed.
devenv:	$(bin_dir)fullrelease

$(bin_dir):
	virtualenv ve --python python3.9

$(bin_dir)fullrelease: $(bin_dir)
	$(python_exe) -m pip install -e .[build]

fetch: Open-Cap-Format-OCF update

Open-Cap-Format-OCF:
	git clone $(git_source)

update:
	cd Open-Cap-Format-OCF; \
	git checkout $(git_branch); \
	git pull

generate:
	$(bin_dir)python3 utils/generate.py
	$(bin_dir)black src/

check:
	$(bin_dir)black src utils tests docs
	$(bin_dir)flake8 src utils tests docs
	$(bin_dir)pyroma -d .

coverage:
	$(bin_dir)coverage run $(bin_dir)pytest
	$(bin_dir)coverage html
	$(bin_dir)coverage report

.PHONY: docs
docs:
	cd ./docs; make html doctest

Open-Cap-Format-OCF/samples/*.json: devenv fetch generate

tests/samples/Captable.ocf.zip: Open-Cap-Format-OCF/samples/*.json
	zip -j tests/samples/Captable.ocf.zip Open-Cap-Format-OCF/samples/*.json

test: tests/samples/Captable.ocf.zip
	$(bin_dir)pytest

release:
	$(bin_dir)fullrelease

clean:
	rm -rf Open-Cap-Format-OCF ve .coverage htmlcov build .pytest_cache docs/source/generated docs/build
