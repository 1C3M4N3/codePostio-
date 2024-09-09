def smallest(*numers):
    return not numers and None or min(numers)

print(smallest(35, 32, 1, 9))
print(smallest(4, 9, 45, 3))