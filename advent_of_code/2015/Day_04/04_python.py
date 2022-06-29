import os 
import hashlib
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
    string = source
    digit = 0
    while True:
      
        hash = str(string) + str(digit)
    
        result = hashlib.md5(hash.encode()).hexdigest()
        if result.startswith("00000"):

            return digit

        digit += 1
        


def part_two(source):
    # part two:
    string = source
    digit = 0
    while True:
      
        hash = str(string) + str(digit)
    
        result = hashlib.md5(hash.encode()).hexdigest()
        if result.startswith("000000"):

            return digit

        digit += 1


if __name__ == "__main__":
    main()