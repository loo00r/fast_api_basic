def binary_search(arr, target):

    low = 0
    high = len(arr) - 1
    counter = 0

    while low <= high:
        mid = (low + high) // 2
        guess_n = arr[mid]
        counter += 1

        if guess_n == target:
            return f'''
            Index of the searched number: {mid}
            Number of iterations: {counter}
            '''
        elif guess_n > target:
            high = mid - 1
        else:
            low = mid + 1
    return None

list_of_numbers = [1, 4, 6, 7, 19, 21, 25, 29, 34, 47, 48, 56, 78, 81]

print(binary_search(list_of_numbers, 25))

