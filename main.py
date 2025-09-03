import argparse

import time
import sys

from bloom_filter import BloomFilter
from filename_generator import generate_filenames


def parse_args():
    parser = argparse.ArgumentParser(description="Bloom Filter")
    parser.add_argument(
        "-n",
        "--numbers",
        type=int,
        default=1_000,
        help="Number of desired items.",
    )
    parser.add_argument(
        "-fn",
        "--filenames",
        type=int,
        default=1_000,
        help="Number of filenames to generate.",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    bf = BloomFilter(args.numbers)

    start_generating_filenames = time.perf_counter()
    for _ in generate_filenames(args.filenames):
        pass
    print(
        f"Total time to generate {args.filenames} filenames: {time.perf_counter() - start_generating_filenames:.6f} seconds"
    )
    start_adding_filenames = time.perf_counter()
    filename_generator = generate_filenames(args.filenames)

    print(f"Total size of filename generator: {sys.getsizeof(filename_generator)}")
    print(f"Total size of bloom filter: {sys.getsizeof(bf.filter)}")

    for filename in filename_generator:
        bf.add(filename)
    print(
        f"Total time to add {args.filenames} enntties: {time.perf_counter() - start_adding_filenames:.6f} seconds"
    )

    start_checking_the_entity = time.perf_counter()
    is_exists = "699e1079b28c4fb8848fe0b19c79d257".zfill(255) in bf
    print(
        f"Total time to check if it exists: {time.perf_counter() - start_checking_the_entity:.6f} seconds"
    )


if __name__ == "__main__":
    main()
