import pytest


def test_filefinder_deprecation() -> None:

    with pytest.raises(
        ImportError, match="`filefinder` has been renamed to `filefisher`"
    ):
        import filefinder  # noqa: F401

    with pytest.raises(
        ImportError, match="`filefinder` has been renamed to `filefisher`"
    ):
        from filefinder import FileFinder  # type: ignore[attr-defined] # noqa: F401
