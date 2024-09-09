def biggest(*numers):
    return not numers and None or max(numers)

print(biggest(35, 32, 1, 9))
print(biggest(4, 9, 45, 3))