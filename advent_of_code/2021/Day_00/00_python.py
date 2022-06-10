import os 

# preset #


def open_file():
    i =  "/input.txt"
    file_path = os.path.dirname(os.path.realpath(__file__)) + i
    with open(file_path,"r") as f:
        return f.readlines()


def main():
    source = open_file()
    
    print(f"Solution Part 1: {part_one(source)}")
    print(f"Solution Part 2: {part_two(source)}")



def part_one(source):
    # part one:
    ...

    


def part_two(source):
    # part two:
    
    ...



if __name__ == "__main__":
    main()