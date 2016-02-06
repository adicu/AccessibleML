import os
import glob
import contextlib
import subprocess

import pytest

notebooks = list(glob.glob("*.ipynb", recursive=True))

@contextlib.contextmanager
def cleanup(notebook):
    name, __ = os.path.splitext(notebook)
    yield

    fname = name + ".html"
    if os.path.isfile(fname):
        os.remove(fname)


@pytest.mark.parametrize("notebook", notebooks)
def test_notebook(notebook):
    with cleanup(notebook):
        # hack to execute the notebook from commandline
        assert 0 == subprocess.call(["jupyter", "nbconvert", "--to=html",
                                     "--ExecutePreprocessor.enabled=True",
                                     notebook])
