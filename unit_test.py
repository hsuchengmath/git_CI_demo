from main import Two_Sum


def testing(test_arr, test_target_value, test_ans):
    pred = Two_Sum(test_arr, test_target_value)
    if pred == test_ans:
        return 'O/'
    else:
        return 'X/'

test_arr_list = [[1,2,3,5],[1,2,3,5],[1,2,3,5]]
test_target_value_list = [8,4,10]
test_ans_list = [[2,3],[0,2],None]



if __name__ == '__main__':
    result_str = ''
    for i in range(len(test_arr_list)):
        test_arr = test_arr_list[i]
        test_target_value = test_target_value_list[i]
        test_ans = test_ans_list[i]
        result_str += testing(test_arr, test_target_value, test_ans)
    print('result : ',result_str)