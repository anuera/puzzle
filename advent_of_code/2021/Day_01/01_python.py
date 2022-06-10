import os 

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = dir_path + "/input.txt"

def main():
    source = open_file()
    
    print(f"Solution Part 1: {part_one(source)}")
    print(f"Solution Part 2: {part_two(source)}")



def part_one(source):
    # part one:
    counter_p1 = 0
    for i in range(1,len(source)-1):
        if source[(i-1)] < source[i]:
            counter_p1 += 1

    return (counter_p1 + 1) # +1 because first entry is bigger than NULL



def part_two(source):
    
    counter_p2 = 0

    for i in range(3,len(source)):
    
        # just compare value [0] and [3], as [1] and [2] are present in both
        if source[i-3] < source[i]:
            counter_p2 += 1

    return counter_p2

def open_file():
    with open(file_path,"r") as f:
        return f.readlines()

if __name__ == "__main__":
    main()