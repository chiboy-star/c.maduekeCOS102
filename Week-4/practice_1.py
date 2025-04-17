def printme(str):
    #this is a print function 
    print(str)
    return str

printme("I'm first call to user defined function!")
printme("Again second call to the same function")

'''
def calculate_area():
    redius = int(input("What is the radius of the circle: "))
    area = 3.14 *(redius**2)
    return area

print(calculate_area())


def find_factors():
    number = int(input("Give me a number to find all the list of factors: "))
    i = 1
    factor = []
    while i <= number:
        if(number % i == 0):
            print(f"the number {i} is a factor of the number {number}")
            i = i + 1
            factor.append(i)
        else:
            print(f"the number {i} is not a factor of the number {number}")
            i = i + 1
    return factor

print(find_factors())

def is_palindrome():
    old_word = input("Give me a word to check: ")
    new_word = []

    for char in old_word[::-1]:
        new_word.append(char)
    new_word = ''.join(new_word)

    if old_word == new_word:
        print("Yes this word is read the same backward as it is forward")
        print(f"normal word {old_word}")
        print(f"reversed word {new_word}")
    else:
        print("no this word is read the same backward as it is forward")
        print(f"normal word {old_word}")
        print(f"reversed word {new_word}")


print(is_palindrome())

def sawp_first_last(swap):
    print(f'This is the list before the swap{swap}')
    temp = swap[-1]
    swap[-1] = swap[0]
    swap[0] = temp
    print(f'This is the list after the swap{swap}')


sawp_first_last([1,2,3,4,5,6,7,8,9,10])

def greet(name,greeting):
    print(f'{greeting} {name}')
    return f'{greeting} {name}'

greet("chinemerem","good day")
'''