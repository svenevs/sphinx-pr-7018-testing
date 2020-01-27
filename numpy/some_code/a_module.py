"""This is a module."""

from pathlib import Path
from typing import Callable, Match, Optional, Union

def filter_file(path: Union[Path, str], pattern: str,
                repl: Union[Callable[[Match], str], str], count: int = 0,
                flags: int = 0, backup_extension: str = ".orig",
                line_based: bool = False, demand_different: bool = True,
                encoding: Optional[str] = None) -> Path:
    """
    Filter the contents of a file.

    Parameters
    ----------
    path
        A parameter ``path``.
    pattern
        A parameter ``pattern``.
    repl
        A parameter ``repl``.
    count
        A parameter ``count``.
    flags
        A parameter ``flags``.
    backup_extension
        A parameter ``backup_extension``.
    line_based
        A parameter ``line_based``.
    demand_different
        A parameter ``demand_different``.
    encoding : int
        A parameter ``encoding``.

    Return
    ------
    A path is returned.  A long paragraph.
    It continues to the next line.

    This is a longer description.

    .. danger::

        Danger is among us.

        .. note::

            I'm still in the docstring!

    How fun.  To be in a docstring.
    """
    return Path(".")
