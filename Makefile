.ONESHELL:

py := poetry run
python := $(py) python

package_dir := src
tests_dir := tests

code_dir := $(package_dir) $(tests_dir)

define setup_env
    $(eval ENV_FILE := $(1))
    @echo " - setup env $(ENV_FILE)"
    $(eval include $(1))
    $(eval export)
endef

