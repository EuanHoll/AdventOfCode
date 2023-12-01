import json
import os
import re

resources_path = os.path.join(os.path.dirname(__file__), "resources")


def open_input_file(path: str) -> list:
    with open(path, "r") as f:
        lines = f.readlines()
    return lines


def get_first_and_last_number_in_str(string: str) -> int:
    # Find all numbers in string as a list of singke digit stringd
    numbers = re.findall(r"\d", string)

    return int(numbers[0] + numbers[-1])


def get_first_and_last_from_list(list_of_strings: list) -> list:
    return [get_first_and_last_number_in_str(string) for string in list_of_strings]


def cli():
    lines = open_input_file(os.path.join(resources_path, "day_1_input.txt"))
    numbers = get_first_and_last_from_list(lines)

    print(f"Sum of all numbers: {sum(numbers)}")


if __name__ == "__main__":
    import time

    start = time.time()
    cli()
    end = time.time()
    print(f"Runtime: {end - start}")
