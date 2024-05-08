import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [0])

def test_more_than_10():
    result = []
    input_arr =[1,2,3,4,5,6,7,8,9,10] #10 or more numbers in the array

    result = Lab3.bubble_sort(input_arr,any)

    assert (result ==[1])

    

def test_0_numbers():
    result =[]
    input_arr = [] #nothing in the array

    result = Lab3.bubble_sort(input_arr,any)

    assert (result == [])

    

def not_all_integers(arr):
    input_arr = [1.5,2,3,4,5,6]

    result = Lab3.bubble_sort(input_arr, any)

    assert (result == [2])