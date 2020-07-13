# Write a program determine whether the given number is Armstrong number or not.
# The program should return true or false
def checkArmstrong(num):
        # Your code goes here
        s = 0
        temp = num
        while temp > 0:
                rem = temp % 10
                s += rem ** 3
                temp = temp // 10
        return num == s