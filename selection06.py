gradeArr = [
    (range(0, 60), 'F'),
    (range(60, 70), 'D'),
    (range(70, 80), 'C'),
    (range(80, 90), 'B'),
    (range(90, 101), 'A')
]

def letterGrade(numGrade):
    if numGrade > 100 or numGrade < 0:
        return 'invalid grade'
    
    for range, letterGrade in gradeArr:
        if numGrade in range:
            return f'{letterGrade}'

print(letterGrade(75)) #returns 'C'
print(letterGrade(98)) #returns 'A'
print(letterGrade(60)) #returns 'F'