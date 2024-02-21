"""Class implementing statistics for Nuclear Dice."""
import logging
import statistics
from dataclasses import dataclass

from .nucleardice import NuclearDice


@dataclass(frozen=True)
class StatValues:
    """Hold statistical values for our nuclear rolls."""

    minimum: float
    maximum: float
    mean: float
    median: float
    mode: int | float
    pstdev: float

    @classmethod
    def from_list(cls, rolls: list[int]) -> "StatValues":
        """Generate statistics from a list of rolls."""
        return cls(
            min(rolls),
            max(rolls),
            statistics.mean(rolls),
            statistics.median(rolls),
            statistics.mode(rolls),
            statistics.pstdev(rolls),
        )

    def report(self, *, indent: int = 0) -> None:
        """Print the statistical results from rolls."""
        _i = " " * indent
        print(f"{_i}Minimum: {self.minimum}")
        print(f"{_i}Maximum: {self.maximum}")
        print(f"{_i}Mean:    {self.mean}")
        print(f"{_i}Median:  {self.median}")
        print(f"{_i}Mode:    {self.mode}")
        print(f"{_i}Pstdev:  {self.pstdev}")


class NuclearDiceStatistics:
    """Statistics for repeated NuclearDice rolls."""

    def __init__(
        self, rolls: int, n: int, x: int, *, debug: bool = False
    ) -> None:
        self._logger = logging.getLogger(__name__)
        level = logging.INFO
        if debug:
            level = logging.DEBUG
            logging.basicConfig(level=level)
            self._logger.setLevel(level)
        self._n = n
        self._x = x
        self._dice = NuclearDice(n, x, debug=debug, logger=self._logger)
        self._rolls = rolls
        self._sums: list[int] = []
        self._roll_counts: list[int] = []
        self._sum_stats: StatValues | None = None
        self._roll_stats: StatValues | None = None

    def roll(self) -> None:
        """Roll the dice and accumulate statistics."""
        self._sum_stats = None
        self._roll_stats = None
        for i in range(self._rolls):
            self._logger.debug(f"Trial {i+1}/{self._rolls}")
            self._dice.roll()
            self._sums.append(self._dice.total)
            self._roll_counts.append(self._dice.roll_count)
        self._logger.info(
            f"Trial ({self._rolls} of {self._n}d{self._x}) complete"
        )
        self._calculate_statistics()

    def _calculate_statistics(self) -> None:
        self._sum_stats = StatValues.from_list(self._sums)
        self._roll_stats = StatValues.from_list(self._roll_counts)

    def report(self) -> None:
        """Report our statistics."""
        if self._sum_stats is None or self._roll_stats is None:
            raise RuntimeError("No results to report; call roll() first")
        print(f"{self._rolls} rolls of {self._n}d{self._x} nuclear ->")
        self._sum_stats.report(indent=4)
        print("Number-of-rolls statistics ->")
        self._roll_stats.report(indent=4)
