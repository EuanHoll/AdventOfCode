import os
import re

resources_path = os.path.join(os.path.dirname(__file__), "resources")


def open_input_file(path: str) -> list:
    with open(path, "r") as f:
        lines = f.readlines()
    return lines


def word_to_int(word):
    number_map = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    value = number_map.get(word.lower())
    if value is not None:
        return value
    else:
        return word


def convert_to_int(string: str) -> int:
    value = word_to_int(string)
    if value is not None:
        return value
    else:
        return int(string)


def get_first_and_last_number_in_str(string: str) -> int:
    searching_for = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]
    char_list = list(string)

    indices = []
    for i in range(len(char_list)):
        for search in searching_for:
            if string[i:].startswith(search):
                indices.append((i, search))

    return int(word_to_int(indices[0][1]) + word_to_int(indices[-1][1]))


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
