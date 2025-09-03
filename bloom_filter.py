import typing as tp


class BloomFilter:
    """This Bloom Filter is using the built-in hash function to calculate
    hashes.

    Attributes:
        size: An integer identificator of the filter size.
        filter: A bytearray filter that stored information about the entity exists or not.
    """

    def __init__(self, size: int) -> None:
        self.size = size
        self.filter = bytearray([0 for _ in range(size)])

    def add(self, value: tp.Hashable) -> None:
        """The method adds information to the filter.

        Notes:
            We don't use several hash functions. Also, we use a simple built-in method to calculate
            hash.
        """
        index = self.hash(value)
        self.filter[index] = 1

    def contains(self, value: tp.Hashable) -> bool:
        """The method checks if a value exists or not."""
        return value in self

    def hash(self, value: tp.Hashable) -> int:
        """Primitive hash method.

        Notes: If needed if can replace print with logging.
        """
        try:
            return hash(value) % self.size
        except TypeError as err:
            print(f"Cannot calculate a hash of the object `{value}`.")
            print(err)
            raise

    def __contains__(self, value: tp.Hashable) -> bool:
        index = self.hash(value)
        return bool(self.filter[index])
