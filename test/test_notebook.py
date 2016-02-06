import glob

from nbconvert.preprocessors import ExecutePreprocessor
import nbformat
import pytest

notebooks = list(glob.glob("*.ipynb", recursive=True))


@pytest.mark.parametrize("notebook", notebooks)
def test_notebook_execution(notebook):
    with open(notebook) as fin:
        nb = nbformat.read(fin, as_version=4)

    ep = ExecutePreprocessor(timeout=120, kernel_name="python3")
    ep.preprocess(nb, resources={})
