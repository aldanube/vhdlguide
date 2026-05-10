"""
VHDL-Utils - Helper functions for VHDL design and simulation.
"""

__version__ = "1.0.0"


class DesignError(Exception):
    """Raised if the VHDL design has an inconsistency."""
    pass


def get_standard_libraries():
    """
    Return a list of standard VHDL libraries.

    :return: The library list.
    :rtype: list[str]
    """
    return ["IEEE", "STD", "WORK"]
