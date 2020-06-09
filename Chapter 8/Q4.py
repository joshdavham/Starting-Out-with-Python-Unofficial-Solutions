#Question 4

def main():
    nums = get_input()
    lowest = min(nums)
    highest = max(nums)
    total = get_total(nums)
    avg = get_avg(nums)

    print("\nThe lowest number:", lowest, \
          "\nThe highest number:", highest, \
          "\nThe total:", total, \
          "\nThe average:", avg)

def get_input():
    nums = [0] * 20
    for index in range(len(nums)):
        nums[index] = float(input("Enter #" + str(index+1) + " "))

    return nums

def get_total(nums):
    total = 0
    for index in range(len(nums)):
        total += nums[index]

    return total

def get_avg(nums):
    total = 0
    for index in range(len(nums)):
        total += nums[index]

    avg = total / len(nums)
    return avg


main()
