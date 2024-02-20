"""Test a single (nuclear) dice roll."""
import random

import nucleardice


def test_nucleardice() -> None:
    """Test a single nuclear dice roll."""
    random.seed(42)
    nd = nucleardice.NuclearDice(4, 12)
    nd.roll()
    assert nd.total == 42
    assert nd.roll_count == 2
