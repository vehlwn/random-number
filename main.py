import random
import sys
import argparse
import typing


def _positive_integer_validator(s: str) -> int:
    ret = int(s)
    if ret > 0:
        return ret
    else:
        raise argparse.ArgumentTypeError("length must be positive integer")


class Config:
    def __init__(
        self,
        is_integer: bool,
        is_float: bool,
        count: int,
        min_value: typing.Union[int, float],
        max_value: typing.Union[int, float],
    ):
        self.is_integer = is_integer
        self.is_float = is_float
        self.count = count
        self.__min_value = min_value
        self.__max_value = max_value

    def min_int(self) -> int:
        return int(self.__min_value)

    def max_int(self) -> int:
        return int(self.__max_value)

    def min_float(self) -> float:
        return float(self.__min_value)

    def max_float(self) -> float:
        return float(self.__max_value)


def _parse_command_line() -> Config:
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-i",
        "--integer",
        help="return integer from [min, max]",
        action="store_true",
    )
    group.add_argument(
        "-f",
        "--float",
        help="return float from [min, max)",
        action="store_true",
    )
    parser.add_argument(
        "-c",
        "--count",
        help="print count numbers",
        type=_positive_integer_validator,
        default=5,
    )
    parser.add_argument(
        "min",
        help="minimum value",
    )
    parser.add_argument(
        "max",
        help="maximum value",
    )
    args = parser.parse_args()
    if args.integer:
        try:
            min_int = int(args.min)
        except ValueError:
            print("min in not an integer")
            sys.exit(1)
        try:
            max_int = int(args.max)
        except ValueError:
            print("max in not an integer")
            sys.exit(1)
        if max_int <= min_int:
            print("Max must be greater than min")
            sys.exit(1)
        return Config(
            is_integer=args.integer,
            is_float=args.float,
            count=args.count,
            min_value=min_int,
            max_value=max_int,
        )
    elif args.float:
        try:
            min_float = float(args.min)
        except ValueError:
            print("min in not a float")
            sys.exit(1)
        try:
            max_float = float(args.max)
        except ValueError:
            print("max in not a float")
            sys.exit(1)
        if max_float <= min_float:
            print("Max must be greater than min")
            sys.exit(1)
        return Config(
            is_integer=args.integer,
            is_float=args.float,
            count=args.count,
            min_value=min_float,
            max_value=max_float,
        )
    else:
        raise RuntimeError("Unreachable")


if __name__ == "__main__":
    config = _parse_command_line()
    if config.is_integer:
        for _ in range(config.count):
            print(random.randint(config.min_int(), config.max_int()))
    elif config.is_float:
        for _ in range(config.count):
            print(random.uniform(config.min_float(), config.max_float()))
    else:
        raise RuntimeError("Unreachable")
