#!/usr/bin/env python3

def main():
    testArray = [12, 10, 9, 17]
    print(bubbleSort(testArray))

def bubbleSort(array):
    j = True
    for i in range(1, len(array)):
        if array[i] < array[i -1]:
            j = False
            t = array[i - 1]
            array[i - 1] = array[i]
            array[i] = t
    return array if j else bubbleSort(array)


if __name__ == '__main__':
    main()
