# aoc 2024 day 2
from typing import List

def is_valid_line(arr: List[int]) -> bool:
    if arr == sorted(arr) or arr == sorted(arr, reverse=True):
        return all(1 <= abs(arr[i] - arr[i-1]) <= 3 for i in range(1, len(arr)))
    return False


def count_safe_levels(file_path: str) -> int:
    num_safe = 0
    with open(file_path, 'r') as file:
        for line in file:
            arr = list(map(int, line.split()))
            if any(is_valid_line(arr[:i] + arr[i+1:]) for i in range(len(arr))):
                num_safe += 1
    return num_safe


def main():
    input_file = 'input.txt'
    num_safe_levels = count_safe_levels(input_file)
    print(f"Number of safe levels: {num_safe_levels}")


if __name__=="__main__":
    main()
