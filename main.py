

def Two_Sum(arr, target_value):
    '''
    given array, target value. 
    Then find two index that sum of mapping value is equal to target value.
    Ex. arr = [1,2,3,5] target_value = 5 -> output [1,2]
    '''
    for i in range(len(arr)):
        val = arr[i]
        diff_val = target_value - val
        start, end = i+1, len(arr)-1
        # binary search algorithm
        while start <= end:
            middle = int((start + end)/2)
            if arr[middle] == diff_val:
                return [i, middle]
            elif arr[middle] < diff_val:
                start = middle + 1
            else:
                end = middle - 1
    return None

if __name__ == '__main__':
    # local unit test
    test_arr = [1,2,3,5]
    test_target_value = 8
    print('Result : ',Two_Sum(test_arr, test_target_value))

