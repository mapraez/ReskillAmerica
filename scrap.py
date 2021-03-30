age = 35

if age < 45:
    print("yes")


crate = ['sand', 'water', 7, 5.9, True]
print(crate[1])
crate.append('mike')
print(crate[5])
name = crate[5]
print("His name is %s and he is %d years old" % (name, age))

sampleList = ['mike', 'love', 'dove']

print("some text %s" % sampleList)

string = "I am a string"
print(string.index('t'))
print(string.count('a'))
print(string[1:6])

print(string[::-1])

print(string.startswith("I"))

print(crate * 2)
print(' ')
print(' ')
print(' ')


age = False
height = 5

if(age >= 18 and height >= 5):
    print("Customer can purchase ticket")
elif(age < 18 or height < 5):
    print('Customer is not allowed to purchase a ticket')
else:
    print('Error: Something went wrong')




