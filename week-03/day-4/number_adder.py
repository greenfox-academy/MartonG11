
# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.


def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)

print(sum(0))
