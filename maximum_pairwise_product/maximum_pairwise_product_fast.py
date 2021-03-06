#!/usr/bin/env python3

def maximum_pairwise_product(numbers):
    """Returns the maximum pairwise product between numbers."""

    ## Validation of list numbers
    if not isinstance(numbers, list): #Numbers must be a list
        raise TypeError('must be list not {}'.format(type(numbers)))    
    if len(numbers) < 2: #Numbers must have len(numbers) greater than 2
        raise IndexError('List has not enough elements')
    
    # Each item in numbers must be a number
    try:
        [int(i) for i in numbers]
    except ValueError as e:
        raise e
    
    max_idx_1 = -1
    max_idx_2 = -1

    # Select first max number
    for i in range(len(numbers)):
        if max_idx_1 == -1 or numbers[max_idx_1] < numbers[i]:
            max_idx_1 = i
            max_1 = numbers[i]

    # Select second max number
    for i in range(len(numbers)):
        if (max_idx_2 == -1 or numbers[max_idx_2] < numbers[i]) and max_idx_1 != i:
            max_idx_2 = i
            max_2 = numbers[i]

    return numbers[max_idx_1] * numbers[max_idx_2]
    
if __name__ == "__main__":
    numbers = input()
    numbers = [int(i) for i in numbers.split()]
    max_pairwise_product = maximum_pairwise_product(numbers)
    print('Maximum pairwise product: {}'.format(max_pairwise_product))
