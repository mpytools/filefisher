import warnings

from filefisher import __version__  # noqa: F401
from filefisher import _filefinder, _utils, cmip, filters
from filefisher._filefinder import FileContainer, FileFinder

__all__ = [
    "_filefinder",
    "_utils",
    "cmip",
    "FileContainer",
    "FileFinder",
    "filters",
]

msg = (
    "`filefinder` has been renamed to `filefisher`! Please install filefisher to get "
    "future releases, and update your imports from `import filefinder` to "
    "`import filefisher`"
)

warnings.warn(msg, FutureWarning, stacklevel=2)
