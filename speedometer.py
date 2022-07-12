"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #2 - Bill's Speedometer (speedometer.py)


Author: Paul Thai

Difficulty Level: 2/10

Background: Bill is driving his brand new car down the street. Every 5 minutes, 
a special instrument records the current speed on his speedometer. After X minutes 
the instrument stops and all the speed recorded is stored into an array (python list). 

Prompt: Given an array of Bill's different speed, the target speed is given at
random.  Traverse through the array and find two numbers that add up to the total speed. 
If the two elements are found, return the two position of the elements as a list. 
If there are no elements that add to the value of the total speed, return false. 

Constraints: N/A

Test Cases:
Input: ary = [1,2,3,4,5] ; target = 6 ;     Output = [0,4]
Input: ary = [2,7,11,15] ; target = 18 ;    Output = [1,2]
Input: ary = [3,1,7] ; target = 4 ;         Output = [0,1]
"""

class Solution:
    def two_numbers(self, ary, target):
        # type ary: list
        # type target: int
        # return type: list or bool

       # TODO: Write code below to return a list with the solution to the prompt
        returnlist = []

        for number in ary: 
            for addition in ary: 
                if number != addition and number + addition == target and len(returnlist) < 2: 
                    returnlist.append(number)
                    returnlist.append(addition)

        if len(returnlist) > 0:
            return returnlist 
        else: 
            return False 


def main():
    # array = input().split(" ")
    array = [1,2,3,4,5]
    for x in range (len(array)):
        array[x] = int(array[x])
    #target = int(input())
    target = int(6)

    tc1 = Solution()
    ans = tc1.two_numbers(array, target)
    print(ans)

if __name__ == "__main__":
    main()