# We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

# bunny_line: [1, 2, 3, 4, 5, .... ,n]
# odd_bunny = 2 ears
# even_bunny = 3 ears
# print like this: SUM[2 "ears", 3 "ears", 2, 3, 2, 3, 2 ....]

def ear_calculator(bunnies):
    if bunnies == 0:
        return 0
    elif bunnies % 2 == 0:
        return 3 + ear_calculator((bunnies) - 1)
    else:
        return 2 + ear_calculator((bunnies) - 1)

print(ear_calculator(2))
