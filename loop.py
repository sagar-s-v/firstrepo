data = [1,2,3,4,5]
for num in data:
    print(num,end = ' ')  # This will print each number in the list.
print('\n')  # This will print a newline after the loop.
for num in data:
    if num == 3:
        continue  # This will skip the number 3.
    print(num,end = ' ')  # This will print each number except 3.
print('\n')  # This will print a newline after the loop.
for num in data:
    if num == 4:
        break  # This will stop the loop when it reaches the number 4.
    print(num,end = ' ')  # This will print each number until it reaches 4.
print('\n')  # This will print a newline after the loop.
for i in range(2,10,2):
    print(i, end=' ')  # This will print even numbers from 2 to 8.
print('\n')  # This will print a newline after the loop.
for i in data:
    pass  # This will do nothing for each element in the list.
print("Loop completed without any action.")  # This will print a message indicating the loop is done.
#-----------------------------------------------------------------------------------------#
x = 0
while x < 10:
    print(x)
    x += 1