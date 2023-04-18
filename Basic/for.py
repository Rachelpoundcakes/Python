points = [30, 40 , 50, 60 , 70, 80, 90, 100]

person = 0

"""
for point in points:
    person += 1
    if point >= 60:
        print("%d번 학생은 합격점입니다."%person)
"""

for person in range(len(points)):
    if points[person] >= 60:
        print("%d번 학생은 합격점입니다."%(person+1))