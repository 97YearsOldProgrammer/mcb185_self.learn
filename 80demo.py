
import sys

print(sys.argv)

print(sys.argv[0][3])

d = [
    'hello',
    (3.14, 'pi'),
    [-1, 0, 1],
    {'year': 2000, 'month': 7}
]
print(d[0][4], d[1][0], d[2][2], d[3]['month'])