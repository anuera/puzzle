import os 

# preset #


def open_file():
    i =  "/input.txt"
    file_path = os.path.dirname(os.path.realpath(__file__)) + i
    with open(file_path,"r") as f:
        return f.read().splitlines()


def main():
    source = open_file()
    
    print(f"Solution Part 1: {part_one(source)}")
    print(f"Solution Part 2: {part_two(source)}")



def part_one(source):
    # part one:
    #print("lines",len(source))
    
    gamma = ""
    epsilon = ""

    
    for char in (range(len(source[0]))):
        sum = 0
        for line in source:
    
            sum += int(line[char])

        if sum > (len(source)/2):
            gamma += "1"
            epsilon += "0"
        elif sum < (len(source)/2):
            gamma += "0"
            epsilon += "1"
              


    gamma = int(gamma,2)
    epsilon = int(epsilon,2)

    return(gamma * epsilon)

    
    
    ...


def part_two(source):
    # part two:
    
    ...



if __name__ == "__main__":
    main()