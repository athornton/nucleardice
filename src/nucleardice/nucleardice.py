"""Class implementing "nuclear dice" -- if *any* dice in a group of
ndx roll their maximum value, reroll all of them and sum the result.
Repeat until none of them roll maximum value.
"""
import logging
import random


def singleroll(n: int, x: int) -> list[int]:
    """Roll ndx."""
    return [random.randint(1, x) for d in range(n)]


class NuclearDice:
    """Roll ndx, nuclear-style, and keep the results."""

    def __init__(
        self,
        n: int,
        x: int,
        *,
        logger: logging.Logger | None = None,
        debug: bool = False,
    ) -> None:
        self.n = n
        self.x = x
        if n < 1:
            raise ValueError("At least 1 die must be rolled.")
        if x < 2:
            raise ValueError("A die must have at least two sides.")
        self._debug = debug
        if logger is None:
            self._logger = logging.getLogger(__name__)
            level = logging.INFO
            if self._debug:
                level = logging.DEBUG
                logging.basicConfig(level=level)
                self._logger.setLevel(level)
        else:
            self._logger = logger
        self._rolls: list[list[int]] = []
        self.roll_count = 0
        self.total = 0

    def roll(self) -> None:
        """Roll the dice until we don't get any maximum values."""
        # Reset counters
        self._rolls = []
        self.total = 0
        self.roll_count = 0

        # Roll until we're done
        while True:
            self.roll_count += 1
            this_roll = singleroll(self.n, self.x)
            sum_this = sum(this_roll)
            self._logger.debug(
                f"Roll #{self.roll_count} ({self.n}d{self.x}): {this_roll}"
                f" -> {sum_this}"
            )
            self._rolls.append(this_roll)
            self.total += sum_this
            if self.x not in this_roll:
                self._logger.debug(f"No {self.x}s rolled")
                self._logger.info(
                    f"Total sum {self.total}/{self.roll_count} rolls"
                )
                return
