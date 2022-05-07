##############Original code without lambda expressions###################################
numbers = [1, 2, 3, 4]
total = 0
for number in numbers:
    total += number
print(total)
##############Code with lambda expressions###############################################
sum_it = lambda x: sum(x)
print(sum_it(numbers))
