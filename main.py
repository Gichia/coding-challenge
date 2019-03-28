"""
A python function that takes in an integer list and returns the sum of elements 
"""

# Solution One
def primes_sum(my_list):
    """
    This function takes in a list as a parameter,
    then it initializes a variable total to Zero as a start
    then we loop through the items in the list and appends their sum to the total variable
    in the end we return the total as the result
    """
    total = 0
    for num in my_list:
        total += num
    return total


if __name__ == "__main__":
    print(primes_sum([1, 4, 56]))
