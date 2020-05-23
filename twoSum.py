def twoSum (nums, target):
    finalArray = []
    for i in range(0, len(nums)) :
        for j in range(0, len(nums)) :
            if nums[i] + nums[j] == target and i != j:
                finalArray.append(i)
                finalArray.append(j)
                return finalArray

    return "None add up to target :("

def main ():
    nums = [1, 4, 7, 11, 15]
    target = 8
    print (twoSum(nums, target))

main()
