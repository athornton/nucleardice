"""NuclearDice implements Sam Krughoff's Nuclear Dice mechanic.

For a roll of ndx:
   the accumulated sum starts at zero.
   roll the dice and add their sum to the accumulated sum.
   if all dice are less than n, return the accumulated sum.
   if any dice are the maximum value, add the sum to the accumulated sum, and
     reroll all dice.
"""
from importlib.metadata import PackageNotFoundError, version

from .nucleardice import NuclearDice, singleroll
from .stats import NuclearDiceStatistics

__version__: str
"""The application version string (PEP 440 / SemVer compatible)."""

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    # package is not installed
    __version__ = "0.0.0"

__all__ = ["NuclearDice", "NuclearDiceStatistics", "singleroll", "__version__"]
