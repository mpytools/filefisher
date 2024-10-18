# flake8: noqa

from importlib.metadata import version as _get_version

from filefinder import _filefinder, _utils, cmip
from filefinder._filefinder import FileContainer, FileFinder

__all__ = [
    "_filefinder",
    "cmip",
    "FileContainer",
    "FileFinder",
    "_utils",
]

try:
    __version__ = _get_version("filefinder")
    del _get_version
except Exception:  # pragma: no cover
    # Local copy or not installed with setuptools.
    # Disable minimum version checks on downstream libraries.
    __version__ = "999"
