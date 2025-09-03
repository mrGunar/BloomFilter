from collections.abc import Iterator
from uuid import uuid4


def generate_filenames(number: int) -> Iterator[str]:
    """The method generates a random filename with a length of 255."""
    assert number > 0, "The number should be greater than 0"
    for _ in range(number):
        yield f"{uuid4().hex:0>255}"
