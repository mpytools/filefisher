import warnings
from contextlib import contextmanager

import pandas as pd

from filefinder import FileContainer


@contextmanager
def assert_no_warnings():

    with warnings.catch_warnings(record=True) as record:
        yield record
        assert len(record) == 0, "got unexpected warning(s)"


def assert_empty_filecontainer(fc, columns=None):

    assert isinstance(fc, FileContainer)

    assert isinstance(fc.df, pd.DataFrame)
    assert fc.df.index.name == "path"
    assert len(fc) == 0, f"FileContainer not empty ({len(fc)=})"

    if columns:
        assert set(fc.df.columns) == set(columns)
