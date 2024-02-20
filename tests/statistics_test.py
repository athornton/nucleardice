"""Test repeated nuclear dice rolls."""
import random

import nucleardice


def test_statistics() -> None:
    """Test statistical functions."""
    random.seed(42)
    st = nucleardice.NuclearDiceStatistics(50, 2, 5)
    st.roll()
    assert st._sum_stats is not None
    assert st._roll_stats is not None
    assert st._sum_stats.minimum == 2
    assert st._sum_stats.maximum == 38
    assert st._sum_stats.mean == 9.5
    assert st._sum_stats.median == 6.0
    assert st._sum_stats.mode == 4
    assert st._sum_stats.pstdev == 8.626123115281858
    assert st._roll_stats.minimum == 1
    assert st._roll_stats.maximum == 5
    assert st._roll_stats.mean == 1.64
    assert st._roll_stats.median == 1.0
    assert st._roll_stats.mode == 1
    assert st._roll_stats.pstdev == 1.1271202242884297
