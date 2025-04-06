from dataStructures import LinkedList

def mergeForMergeSort(lhs: list, rhs: list): 

    c = []

    while lhs and rhs: 
        if lhs[-1]>=rhs[-1]: 
            c.append(rhs.pop())
        else: 
            c.append(lhs.pop())
    

    while lhs: 
        c.append(lhs.pop())

    while rhs: 
        c.append(rhs.pop())

    return c

def mergeSort(a: list) -> list: 
    n = len(a)
    halfway = int(n/2)

    if n == 1:
        return a

    lhs = a[0:halfway]
    rhs = a[halfway:n]

    lhs = list(reversed(mergeSort(lhs)))
    rhs = list(reversed(mergeSort(rhs)))
    
    return mergeForMergeSort(lhs,rhs)

def main():
    arr = [9,7,5,4,8]
    print(mergeSort(arr))


if __name__ == "__main__":
    main()