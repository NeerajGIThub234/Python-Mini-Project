import random
import time


OPERATORS = ["+", "-", "*",] # we don't use / bcz the way we write code it's not working
MIN_OPERANND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERANND, MAX_OPERAND)
    right = random.randint(MIN_OPERANND, MAX_OPERAND)
    operator = random.choice(OPERATORS)  # give random element from list

    expr = str(left) + " " + operator+ " " + str(right)
    answer = eval(expr)  # eval function is used to evaluate a string as it was a valid python expression
    return expr , answer


wrong = 0
input("Press enter to start!")
print("-------------------------")

start_time = time.time() # return current time in seconds


for i in range(TOTAL_PROBLEMS):
    expr , answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i+1) + ": "+ expr + "= ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2) # give value of 2 digit after decimal 

print("-------------------------")
print("Nice Work! You finished in", total_time,"seconds!")
print("You only gave wrong answer", wrong , "times!")