import random

# A dictionary of test cases for the quick sort algorithm
tests = {
    "nums_unsorted": [9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    "nums_sorted": [i for i in range(10)],
    "nums_random_all_positive": [random.randint(0, 10) for i in range(10)],
    "nums_random_very_large": [random.randint(0, 1000) for i in range(5000)],
    "nums_empty": [],
    "nums_one_element": [1],
    "nums_negative_only": [random.randint(-10, 0) for i in range(10)],
    "nums_mixed_pos_neg": [random.randint(-1000, 1000) for i in range(10)]
}

def quick_sort(list_of_numbers):
    """
    A quick sort algorithm implementation.

    Parameters:
    list_of_numbers (list): The list of numbers to be sorted.

    Returns:
    list: The sorted list of numbers.
    """
    if len(list_of_numbers) == 0:
        # base case
        sorted_list = list_of_numbers
    else:
        pivot_num = list_of_numbers[-1]
        list_of_numbers.pop()

        less_than_pivot = [num for num in list_of_numbers if num <= pivot_num]
        greater_than_pivot = [num for num in list_of_numbers if num > pivot_num]

        # recursive call
        sorted_list = quick_sort(less_than_pivot) + [pivot_num] + quick_sort(greater_than_pivot)

    return sorted_list


# check tests and prints results with input, output, and expected output
for test_name, test_list in tests.items():
    original_list = test_list.copy()
    expected_sorted_list = sorted(test_list)
    quick_sorted_list = quick_sort(test_list)

    if expected_sorted_list != quick_sorted_list:
        print(f"---{test_name}: Test failed!---")
    else:
        print(f"---{test_name}: Test passed!---")

    print(f"Unsorted: {original_list}")
    print(f"Expected: {expected_sorted_list}")
    print(f"Output: {quick_sorted_list}\n")
