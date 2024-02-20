"""Test the Nuclear Dice CLI."""
import subprocess


def test_cli_roll() -> None:
    """Test rolling one set of nuclear dice with the CLI."""
    cp = subprocess.run(
        ["nucleardice", "3", "20", "--seed", "42"],
        capture_output=True,
        check=False,
    )
    assert cp.returncode == 0
    assert cp.stdout.decode() == "14\n"


def test_cli_stats() -> None:
    """Test rolling repeated sets of nuclear dice with the CLI."""
    cp = subprocess.run(
        ["nucleardice", "3", "20", "-r", "100", "--seed", "42"],
        capture_output=True,
        check=False,
    )
    assert cp.returncode == 0
    assert (
        cp.stdout.decode()
        == """100 rolls of 3d20 nuclear ->
    Minimum: 8
    Maximum: 80
    Mean:    34.19
    Median:  30.0
    Mode:    25
    Pstdev:  16.27187450787401
Number-of-rolls statistics ->
    Minimum: 1
    Maximum: 2
    Mean:    1.12
    Median:  1.0
    Mode:    1
    Pstdev:  0.32496153618543844
"""
    )
