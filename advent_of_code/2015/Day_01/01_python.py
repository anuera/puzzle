import os 

# preset #


def open_file():
    i =  "/input.txt"
    file_path = os.path.dirname(os.path.realpath(__file__)) + i
    with open(file_path,"r") as f:
        return f.read()


def main():
    source = open_file()
    
    print(f"Solution Part 1: {part_one(source)}")
    print(f"Solution Part 2: {part_two(source)}")



def part_one(source):
    # part one:
    floor = 0
    for i in source:
        if i == "(":
            floor += 1
        elif i == ")":
            floor -=1

    return (floor)
    ...

    


def part_two(source):
    # part two:
    floor = 0
    position = 0
    for i in source:
        if floor == -1:
            return position
        else:
            position += 1 
            if i == "(":
                floor += 1
            elif i == ")":
                floor -=1
            
    



if __name__ == "__main__":
    main()