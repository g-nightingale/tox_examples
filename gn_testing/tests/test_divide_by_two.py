import sys
from pathlib import Path

sys.path.insert(1, str(Path(__file__).resolve().parent.parent))

from model.functions import square


def test_square():
    # When
    subject = square(4)

    # Then
    assert subject == 16
