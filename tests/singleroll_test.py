"""Test a single (normal) dice roll."""
import random

import nucleardice


def test_singleroll() -> None:
    """Test a single dice roll."""
    random.seed(42)
    val = nucleardice.singleroll(4, 12)
    assert val == [11, 2, 1, 12]
