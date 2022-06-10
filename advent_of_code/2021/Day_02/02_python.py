import os


# preset #


def open_file():
    i =  "/input.txt"
    file_path = os.path.dirname(os.path.realpath(__file__)) + i
    with open(file_path,"r") as f:
        return f.read().splitlines()


def main():
    source = open_file()
    data = []
    for line in source:
 
        data.append(line.split(" "))


    print(f"Solution Part 1: {part_one(data)}")
    print(f"Solution Part 2: {part_two(data)}")



def part_one(source):
    # part one:
    depth = 0
    distance = 0

    for i in source:

        if i[0] == "forward":
            distance += int(i[1])
        elif i[0] == "down":
            depth += int(i[1])
        elif i[0] == "up":
            depth -= int(i[1])
    
    #print(depth, distance)
    return (distance * depth)


def part_two(source):
    # part two:

    distance = 0
    depth = 0
    aim = 0

    for i in source:
        
        if i[0] == "forward":
            distance += int(i[1])
            depth += (aim * int(i[1]))


        elif i[0] == "down":
            aim += int(i[1])
        elif i[0] == "up":
            aim -= int(i[1])
        


    return (distance * depth)





if __name__ == "__main__":
    main()