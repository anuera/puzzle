import os 

def open_file():
    i =  "/input.txt"
    file_path = os.path.dirname(os.path.realpath(__file__)) + i
    with open(file_path,"r") as f:
        return f.read().strip()


def main():
    source = open_file()
    
    print(f"Solution Part 1: {part_one(source)}")
    print(f"Solution Part 2: {part_two(source)}")



def part_one(source):
    # part one:

    coords = [0,0]
    coord_list = []
    for i in source:
        if i == "^":
            coords[1] += 1
        elif i == "v":
            coords[1] -= 1
        elif i == "<":
            coords[0] -= 1
        elif i == ">":
            coords[0] += 1

        coord_list.append(str(coords[0])+","+str(coords[1]))

    # print(coord_list)
    print(len(set(coord_list)))



def part_two(source):
    # part two:
    santa_coords = [0,0]
    robo_coords = [0,0]
    
    coord_list = []


    #santa:
    for i in source[::2]:
        if i == "^":
            santa_coords[1] += 1
        elif i == "v":
            santa_coords[1] -= 1
        elif i == "<":
            santa_coords[0] -= 1
        elif i == ">":
            santa_coords[0] += 1

        coord_list.append(str(santa_coords[0])+","+str(santa_coords[1]))


    #robo:
    for i in source[1::2]:
        if i == "^":
            robo_coords[1] += 1
        elif i == "v":
            robo_coords[1] -= 1
        elif i == "<":
            robo_coords[0] -= 1
        elif i == ">":
            robo_coords[0] += 1

        coord_list.append(str(robo_coords[0])+","+str(robo_coords[1]))


    return(len(set(coord_list)))

   

if __name__ == "__main__":
    main()