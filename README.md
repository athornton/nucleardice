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

Use `nucleardice <d> <x>` to do a single roll of ndx nuclear dice.

Use `nucleardice -r <rolls> <d> <x>` to roll the dice _rolls_ times and
report statistics for those rolls.

## Run on binder.org

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/athornton/nucleardice/HEAD)

