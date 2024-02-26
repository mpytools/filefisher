# flake8: noqa

from . import _filefinder, cmip, utils
from ._filefinder import FileContainer, FileFinder
from importlib.metadata import version as _get_version

try:
    __version__ = _get_version("filefinder")
except Exception:
    # Local copy or not installed with setuptools.
    # Disable minimum version checks on downstream libraries.
    __version__ = "999"
