def get_largest_num(number, n):
    number.sort()

    return number[-n:]

nums = [3,47,4,5,3,24,345,345,6,4]

print(nums)
largest = get_largest_num(nums, 2)
print(largest)