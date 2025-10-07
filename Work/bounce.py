# bounce.py
#
# Exercise 1.5

init_height = 100
height = 0

for i in range(0, 11):
    if i == 0:
        height = init_height

    print(f"{i} : {height}")
    height = round(height * (3 / 5), 4)
