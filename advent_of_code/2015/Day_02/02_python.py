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
    sq_feet = 0
    ls = source

    # convert to integer and sort
    for i in range(0, len(ls)):
        ls[i] = (ls[i].strip().split("x"))
        for j in range(len(ls[i])):
            ls[i][j] = int(ls[i][j])
        ls[i].sort()


        l = ls[i][0]
        w = ls[i][1]
        h = ls[i][2]
        sq_feet += (2*l*w + 2*w*h + 2*h*l)

        # extra paper
        sq_feet += (l*w)
    

    return(sq_feet)

    


def part_two(source):
    # part two:
    
    ribbon = 0
    ls2 = source

    # convert to integer and sort
    for i in range(0, len(ls2)):
  
        for j in range(len(ls2[i])):
            ls2[i][j] = int(ls2[i][j])
        ls2[i].sort()


        l = ls2[i][0]
        w = ls2[i][1]
        h = ls2[i][2]
        
        ribbon += (2*l + 2*w + (w*h*l))

    

    return(ribbon)




if __name__ == "__main__":
    main()