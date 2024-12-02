# aoc 2024 day 1

leftList = []
rightList = []
rightMap = {}

def parse_input():
    with open('input.txt', 'r') as file:
        for line in file:
            leftList.append(line.split()[0])
            rightList.append(line.split()[1])
    leftList.sort()
    rightList.sort()


def map_right_list_freq():
    for num in rightList:
        if not num in rightMap:
            rightMap[num] = 1
        else:
            rightMap[num] += 1


def find_list_diff():
    diff = 0
    for a, b in zip(leftList, rightList):
        diff += abs(int(a)-int(b))
    print("List difference: " + str(diff))


def find_similarity_score():
    score = 0
    for num in leftList:
        score += int(num) * rightMap.get(num, 0)
    print("Similarity score: " + str(score))


def main():
    parse_input()
    map_right_list_freq()
    find_list_diff()
    find_similarity_score()


if __name__=="__main__":
    main()
