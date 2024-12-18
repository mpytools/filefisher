import sys

import pytest

from . import assert_no_warnings


def test_filefinder_deprecation():

    with pytest.warns(
        FutureWarning, match="`filefinder` has been renamed to `filefisher`"
    ):
        import filefinder  # noqa: F401

    # NOTE warning only issued once (even for from imports)
    with assert_no_warnings():
        from filefinder import FileContainer  # noqa: F401

    # remove imported module to re-trigger warning
    del sys.modules["filefinder"]

    with pytest.warns(
        FutureWarning, match="`filefinder` has been renamed to `filefisher`"
    ):
        from filefinder import FileFinder  # noqa: F401 # noqa: F401
