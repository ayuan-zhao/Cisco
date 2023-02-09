# 众数（英语：mode）指一组数据中出现次数最多的数据值。例如{8，7，7，8，6，5，5，8，8，8}中，出现最多的是8，因此众数是8，众数可能是一个数（数据值），但也可能是多个数（数据值）。若数据的数据值出现次数相同且无其他数据值时，则不存在众数。例如{5，2，8，2，5，8}中，2、5、8出现次数相同且没有其他数，因此此数据不存在众数。
# Question:
# the arithmetic mean of N numbers is the sum of all the numbers, divided by N. The mode of N numbers is the most frequently occurring number. 
# Write an algorithm to find the mean and mode of a set of given numbers. 

# Input: the first line of input consists of an integer inputNum, representing the number of elements in the set(N).

# The next line consists of N space-separated integers representing the elements of the given set. 

# outputs: print space-separated integers where the first number is the mean of the input numbers, and the second number is the mode(where k = 2)
# from collections import Counter

# def mean_and_mode(inputNum, numbers):
#     # Calculate the mean
#     mean = sum(numbers) / inputNum
    
#     # Count the frequency of each number
#     frequency = Counter(numbers)
    
#     # Find the mode
#     mode = max(frequency, key=frequency.get)
    
#     return mean, mode

# # Read inputNum
# inputNum = int(input().strip())

# # Read numbers
# numbers = list(map(int, input().strip().split()))

# # Get the mean and mode
# mean, mode = mean_and_mode(inputNum, numbers)

# # Print the result
# print(mean, mode)


class Solution:
    def findMean(self,inputNum,nums):
        numSum,numMean = 0,0
        for num in nums:
            numSum += num
        numMean = numSum/inputNum
        return numMean

    # def mode(self,inputNum,nums):
    #     modeMap = {}
    #     for num in nums:
    #         modeMap[num]= 1 + modeMap.get(num,0)
    #     mostFrequency = max(modeMap.values())
    #     # modeValue = max(modeMap, key=modeMap.get)
    #     for num,freq in modeMap.items():
    #         if freq == mostFrequency:
    #             return num
   

    def findMode(self,nums):
        print("--------nums:-------") 
        print(nums)
        freqMap = {}
        if not nums:
            return None
        for num in nums:
            freqMap[num] = 1 + freqMap.get(num,0)
        max_frequency = max(freqMap.values())
        # print(freqMap)
        mode = []
        for num,count in freqMap.items():
            if count ==max_frequency:
                mode.append(num)
        # print(mode)
        if len(mode) == len(nums):
            return None
        elif len(mode) ==1:
            return mode[0]
        else:
            return mode


        

so = Solution()
inputNum = 6
nums = [1,1,1,3,3,3]
nums1 = [1]
nums2= []
nums3=[1,2,3,4]
nums4=[1,1,2,2,4]
nums5= [1,1,1,2,4]

mean = so.findMean(inputNum,nums)
print(mean)
mode = so.findMode(nums)
print(mode)

mode = so.findMode(nums1)
print(mode)


mode = so.findMode(nums2)
print(mode)

mode = so.findMode(nums3)
print(mode)

mode = so.findMode(nums4)
print(mode)

mode = so.findMode(nums5)
print(mode)








