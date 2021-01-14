#%%
# 1. Basic
""" Print all integers from 0 to 150 
"""
def basic():
    for i in range(150):
        print(i)
#basic()
#%%

# 2. Multiples of Five
"""
Print all the multiples of 5 from 5 to 1,000
"""
def multiplesOfFive():
    for i in range(5,1005,5):
        print(i)
#multiplesOfFive()

#%%
# 3. Counting, Dojo Way
"""
Print integers 1 to 100. 
If divisible by 5, print "Coding" instead. 
If divisible by 10, print "Coding Dojo".
"""
def countDojoWay():
    for i in range(5,100,5):
        if ((i%10 == 0) & (i%5==0)):
            print(str(i) + ":","Coding Dojo")
        elif (i%5==0):
            print(str(i) + ":", "Coding")
#countDojoWay()

#%%
# 4. Whoa, that suckers huge
"""
Add odd integers from 0 to 500,000, 
and print the final sum
"""
def hugeSucker():
    tot = 0
    for i in range(500001):
        if (i%2 != 0):
            tot = tot + i
    print(tot)
#hugeSucker()

#%%
# 5. Countdown by Fours
"""
Print positive numbers starting at 2018, 
counting down by fours
"""
def countBy4():
    for i in range(2018,0,-4):
        print(i)
#countBy4()

#%%
# 6. Flexible Counter
"""
Set three variables: lowNum, highNum, mult. 
Starting at lowNum and going through highNum, 
print only the integers that are a multiple of mult. 
For example, if lowNum=2, highNum=9, and mult=3, 
the loop should print 3, 6, 9 (on successive lines)
"""
def flexible_counter():
    lowNum = 2
    highNum = 9
    mult = 3
    for i in range(lowNum,highNum+1,1):
        if(i%mult==0):
            print(i)
#flexible_counter()
