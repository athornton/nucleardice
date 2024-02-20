# Nuclear Dice

"Nuclear Dice" is a game mechanic invented by Sam Krughoff.  A player
rolls n dice of x faces each (henceforth, `ndx`); the result is the sum
of those dice.  However, if *any* of those dice are their maximum value,
the sum is added to the running total (which begins at zero) and *all*
dice are rerolled.

This is a tool to investigate the statistical properties of those dice,
in order to lead us towards a closed-form solution for the expected
outcomes.

## Usage

Use `nucleardice <trials> <d> <x>` to roll `ndx` <trials> times and
report statistics for them.
