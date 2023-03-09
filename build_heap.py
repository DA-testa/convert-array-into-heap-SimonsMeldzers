# python3
def sort_heap(data, n, swaps, i):
    sm = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and data[l] < data[sm]:
        sm = l
        
    if r < n and data[r] < data[sm]:
        sm = r

    if sm != i:
        swaps.append((i, sm))
        sort_heap(data, n, swaps, sm)



def build_heap(data):
    swaps = []
    n = len(data)

    for i in range(int(n / 2), -1, -1):
        sort_heap(data, n, swaps, i)

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    fileType = input()

    if "F" in fileType:
        fileName = input()

        if "a"  in fileName:
            return
        
        if "test/" not in fileName:
            fileName = 'test/' + fileName
        
        with open(fileName) as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().split()))

    elif "I" in fileType:
        n = int(input())
        data = list(map(int, input().split()))
    else:
        print("Error")

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
