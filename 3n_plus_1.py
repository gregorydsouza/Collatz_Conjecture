import matplotlib.pyplot as plt

# plt.scatter(x,y) to plot points

start_number = input("Input a starting number: ")

if start_number.isnumeric():
    start_number = int(start_number)
else:
    quit()

MAX_ITERATIONS = 200

new_number = start_number
repeat_pattern = [4, 2, 1]
test_pattern = []
plt.plot(0, start_number)
for i in range(MAX_ITERATIONS):
    prev_number = new_number
    if new_number % 2 == 0:
        new_number /= 2
    else:
        new_number = (3 * new_number) + 1
    
    if new_number in repeat_pattern:
        test_pattern.append(new_number)
    if len(test_pattern) >= 3:
        if test_pattern == repeat_pattern:
            break
        else:
            test_pattern.clear()
    
    plt.plot((i-1, i), (prev_number, new_number))

plt.show()
