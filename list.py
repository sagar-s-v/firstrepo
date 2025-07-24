car =  ['bmw', 'audi', 'ford', 'tesla']
#car2 = ['bmw', 'audi', 'ford', 'tesla']
print(car[2]) # This will print 'ford', which is the third element in the list.
print(car[1:3]) # This will print ['audi', 'ford'], which are the second and third elements in the list.
print(car[-1]) # This will print 'tesla', which is the last element in the list.
print(car[-2:]) # This will print ['ford', 'tesla'], which are the last two elements in the list.
print(car[1:4:2]) # This will print ['audi', 'tesla'], which are the second and fourth elements in the list.
print(car[1:]) # This will print ['audi', 'ford', 'tesla'], which are all elements from the second to the end of the list.
if 'audi' in car: # This will check if 'audi' is in the list.
    print("Yes, 'audi' is in the list.")
else:
    print("No, 'audi' is not in the list.")
print(car + ['toyota', 'honda']) # This will concatenate the list with another list.
car.append('toyota') # This will add 'toyota' to the end of the list.
print(car) # This will print the updated list with 'toyota' added.
car.insert(2, 'honda') # This will insert 'honda' at index 2.
print(car) # This will print the updated list with 'honda' inserted.
car.remove('ford') # This will remove 'ford' from the list.
print(car) # This will print the updated list with 'ford' removed.
car[1] = 'mercedes' # This will change the second element to 'mercedes'.
print(car) # This will print the updated list with 'mercedes' as the second element
car[1:3] = ['volvo', 'jaguar'] # This will change the second and third elements to 'volvo' and 'jaguar'.
print(car) # This will print the updated list with 'volvo' and 'jaguar'.
car[2] = ['land rover', 'porsche'] # This will change the third element to a list containing 'land rover' and 'porsche'.
print(car) # This will print the updated list with the third element as a list.
car.pop() # This will remove the last element from the list.
print(car) # This will print the updated list with the last element removed.
car.pop(1) # This will remove the element at index 1.
print(car) # This will print the updated list with the element at index 1 removed.
del car[1] # This will delete the element at index 1.
for x in car: # This will iterate through each element in the list.
    print(x) # This will print each element in the list.