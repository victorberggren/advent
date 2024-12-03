# aoc 2024 day 3
import re


def main():
    sum = 0
    enabled = True
    with open("input.txt", "r") as file:
        input = file.read().rstrip()
        matches = re.finditer(r"(?:mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))", input)
        for match in matches:
            if match.group(1) and enabled:
                sum += int(match.group(1)) * int(match.group(2))
            else:
                enabled = match.group(3)
    print(f"Total sum: {sum}")


if __name__ == "__main__":
    main()
