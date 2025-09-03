import typing as tp


class BloomFilter:
    """This Bloom Filter is using the built-in hash function to calculate
    hashes.

    Attributes:
        size: An integer identificator of the filter size.
        filter: A bytearray filter that stored information about the entity exists or not.
        hash_func_count: A number stands for how many times a hash function needs to be called.
    """

    def __init__(
        self,
        number_of_items: int,
        false_positive_probability: float = 0.0001,
    ) -> None:
        """
        Args:
            number_of_items: The number of items to be stored.
            false_positive_probability: A false positive probability parameter.

        Notes: We need to add dependency of false_positive_probability parameter.
        """
        self.size = self._get_size(number_of_items)

        self.hash_func_count = self._get_number_of_hash_functions(
            self.size, number_of_items
        )

        self.filter = bytearray([0 for _ in range(self.size)])

    def _get_number_of_hash_functions(self, size: int, item_count: int) -> int:
        """The method calculate the number of hash functions.

        Notes: At this moment, it simply return 1.
        """
        return 1

    def _get_size(self, number_of_items: int) -> int:
        """This method calculates size of the filter.

        Notes: At this moment we don't use any algorithm to calculate this number.
        """
        return number_of_items

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
