"""
(Display four patterns using loops)
"""

# Pattern A
print('Pattern A')
for i in range(1, 7):
    for j in range(1, i+1):
        print(j, end=' ')

    print()

# Pattern B
print('-------')
print('Pattern B')
for i in range(6):
    for j in range(1, 7 - i):
        print(j, end=' ')

    print()

# Pattern C
print('-------')
print('Pattern C')
for i in range(1, 7):
    for j in range(1, 7):
        pass


# Pattern D
print('-------')
print('Pattern D')
for i in range(7, 0, -1):
    for j in range(1, i):
        print(j, end=' ')
    print()
