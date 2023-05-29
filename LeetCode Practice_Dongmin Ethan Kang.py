# 412. Fizz Buzz
class Solution(object):
    def fizzBuzz(self, n):
        answer = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append('FizzBuzz')
            elif i % 3 == 0:
                answer.append('Fizz')
            elif i % 5 == 0:
                answer.append('Buzz')
            else:
                answer.append(str(i))
        return answer

# 1342. Number of Steps to Reduce a Number to Zero
class Solution(object):
    def numberOfSteps(self, num):
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            steps += 1
            continue
        return steps
    
# 1480. Running Sum of 1d Array
class Solution(object):
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

# 1672. Richest Customer Wealth
class Solution(object):
    def maximumWealth(self, accounts):
        wealth = []
        for customer in accounts:
            wealth.append(sum(customer))
        return max(wealth)