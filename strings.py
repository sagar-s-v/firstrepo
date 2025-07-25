x='Sagar'
print(x[-1:-3]) # This will print an empty string because the slice is in reverse order.
print(x[-3:-1]) # This will print 'ag' as it slices from index 2 to 3.
print(x[0:4:2]) # This will print 'a' as it starts at index 1 and goes to index 3 with a step of 5.
print(x.replace('S','m'))
s=x.replace('S','m')
print(s.capitalize())
print(s.count('a'))
print(s.find('m'))
print(s+'sv')
print(len(s))
print(s.endswith('s'))
y=5
a=f""" this contains "verified" {y} string.""" # This will format the string with the value of y.If f is not used, it will not format.
print(a)
d=""
print(bool(d))