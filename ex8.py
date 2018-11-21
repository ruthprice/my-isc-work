## Exercise 8.1
#
#def double_it(number):
#    return 2 * number
#
#an_int = 3
#a_float = 5.0
#a_string = "hello"
#
#print("doubling int... ", double_it(an_int))
#print("doubling float... ", double_it(a_float))
#print("doubling string... ", double_it(a_string))

# Exercises 8.2 and 8.3

def calc_hypo(a, b):
    if type(a) not in (float, int) or type(b) not in (float, int) or a <= 0 or b <= 0:
        print("Bad argument")
        return False
    hypo = (a**2 + b**2)**0.5
    return hypo

print(calc_hypo(3, 4))
print(calc_hypo(-2, 1))
print(calc_hypo("three", 4))
