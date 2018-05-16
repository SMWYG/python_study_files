def grade(n):
    """
    90점 이상이면 A, 70점 이상이면 B, 60점 이상이면 C, 
    50점 이상이면 D, 그 외에는 F를 반환하는 함수를 작성하시오.
    단, 점수 n은 0이상 100이하의 정수이다.
    """
    if n >= 90:
        return 'A'
    elif n >= 70:
        return 'B'
    elif n >= 60:
        return 'C'
    elif n >= 50:
        return 'D'
    else:
        return 'F'

for n in [100, 95, 27, 44, 56, 62, 50, 70, 0]:
    print("%3d --> %s" % (n, grade(n)))

""" 수행 예:
100 --> A
 95 --> A
 27 --> F
 44 --> F
 56 --> D
 62 --> C
 50 --> D
 70 --> B
  0 --> F
"""
