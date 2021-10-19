import sys
from pathlib import Path

sys.path.insert(1, str(Path(__file__).resolve().parent.parent))

from model.functions import divide_by_two


def test_divide_by_two():
    # When
    subject = divide_by_two(4)

    # Then
    assert subject == 2
