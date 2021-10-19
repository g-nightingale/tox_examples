import sys
from pathlib import Path

sys.path.insert(1, str(Path(__file__).resolve().parent.parent))

from model.functions import add_three


def test_add_three():
    # When
    subject = add_three(4)

    # Then
    assert subject == 7
