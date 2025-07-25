student = {'name':'sagar', 'Age':21, 'sub':['eng','phy','maths']}
print(student)
print(student['name']) # Accessing value using key
print(student.get('Age')) # Accessing value using get method
print(student.get('phone', 'not found')) # Accessing non-existing key with default value
student['phone'] = 1234567890 # Adding new key-value pair
student['Age'] = 22 # Modifying existing key-value pair
student['sub'] = student['sub'] + ['chemistry'] # Modifying list in dictionary
student['subject'] = student['sub'] #renaming key
del student['sub'] #Need to delete old key or syntax for deleting key-value pair
print(student.keys()) # Printing all keys
print(student.values()) # Printing all values
print(student.items()) # Printing all key-value pairs
for key in student:
    print(key) # Iterating through keys and prints only keys
for key, value in student.items():
    print(f"{key}: {value}") # Iterating through key-value pairs and prints both
student.update({'name': 'ABCD', 'Age': 22, 'phone': 1234,}) # Updating dictionary
print(student) # Printing updated dictionary
del student['subject'] # Deleting key-value pair
age = student.pop('Age') # Removing key-value pair and returning value
print(student) # Printing dictionary after deletion
print(age) # Printing the value that was removed
#------------------------------------------------------------------------------------------------#
#nested dictionary#
nested_dict = { 'student1': {'name': 'sagar', 'Age': 21, 'sub': ['eng', 'phy', 'maths']},
                'student2': {'name': 'john', 'Age': 22, 'sub': ['chemistry', 'biology']}}
print(nested_dict) # Printing nested dictionary
print(nested_dict['student1']) # Accessing nested dictionary 
print(nested_dict['student1']['name']) # Accessing nested dictionary value
print(nested_dict['student2']['sub']) # Accessing nested dictionary list
print(nested_dict['student2']['sub'][0]) # Accessing nested dictionary list element
print(nested_dict['student1'].get('Age')) # Accessing nested dictionary value using get method
#print(nested_dict.get(student1.get('Age'))) # this line is incorrect and will raise an error