print('PART ONE')
print('--------')

nums = []
with open("day_01_input", "r") as f:
    for line in f:
        nums.append(int(line))

nums.sort()

for x in range(0, len(nums)):
    for y in range(len(nums) - 1, x, -1):
        if nums[x] + nums[y] == 2020:
            print("found " + str(nums[x]) + " + " + str(nums[y]) + " = " + "2020")
            print("solution is " + str(nums[x] * nums[y]))

print('\n')
print('PART TWO')
print('--------')

nums = [x for x in nums if x < 1250]

for x in range(0, len(nums)):
    for y in range(len(nums) - 1, x, -1):
        for z in range(x, y + 1):
            if nums[x] + nums[y] + nums[z] == 2020:
                print("found " + str(nums[x]) + " + " + str(nums[y]) \
                    + " + " + str(nums[z]) + " = " + "2020")
                print("solution is " + str(nums[x] * nums[y] * nums[z]))

