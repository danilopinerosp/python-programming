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
    
    maximum_product = float('-inf')
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = numbers[i] * numbers[j]
            if maximum_product < product:
                maximum_product = product
    return maximum_product
    
if __name__ == "__main__":
    numbers = input()
    numbers = [int(i) for i in numbers.split()]
    max_pairwise_product = maximum_pairwise_product(numbers)
    print('Maximum pairwise product: {}'.format(max_pairwise_product))
