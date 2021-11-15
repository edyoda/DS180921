# what is debugging?
# Finding and Fixing Errors
breakpoint()
a = input()
b = input()

def sum_of_the_values(a,b):
    print('We are inside the function')
    print(a+b)

sum_of_the_values(a,b)

# pdb console appears whereever it sees breakpoint()
# c(continue) => continues all the leftover code wherever
# we are
# n(next) => runs the very next piece of code
# s(step inside) => to step inside the fuction such that 
# enter will work like showing us the line executing

# We can use print() method in pdb console
