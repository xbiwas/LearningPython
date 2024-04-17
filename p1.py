# finding difference 
'''
def hello(name):
    print("HELLO", name)

hello('Asish')
# return hello("asish") learned that return function can only be used inside a function
'''

# def function(parameter):
#     print("Something that we pass inside a function is parameter,", parameter)

# function("result pass")


import random

def getAnswer(ans):
    if ans == 1:
        return 'It is certain'
    elif ans == 2:
        return 'It is two'
    elif ans == 3:
        return "It is three"
    elif ans == 4:
        return 'It is four'
    elif ans == 5:
        return "It is five"

r = random.randint(1,5)
correctAnswer = getAnswer(r)
print(correctAnswer)
    


