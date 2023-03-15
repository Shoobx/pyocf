# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'pyocf'
copyright = '2023, Lennart Regebro'
author = 'Lennart Regebro'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinxcontrib.autodoc_pydantic',
    'sphinx.ext.doctest',
]

templates_path = ['_templates']
exclude_patterns = []
autosummary_generate = True
autodoc_pydantic_model_show_json = False
autodoc_pydantic_model_show_field_summary = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

doctest_global_setup = '''
import tempfile
TEST_DIR = tempfile.mkdtemp()
'''

doctest_global_cleanup = '''
import shutil

shutil.rmtree(TEST_DIR)
'''
