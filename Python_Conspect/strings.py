'''
    upper() - This method converts all characters into upper case
    lower() - This method converts all characters into lower case
    swapcase() - This method converts all lower-case characters to uppercase and all upper-case characters to lowercase
    title() - This method converts all character to title case (The first character in every word will be in upper case and all remaining characters will be in lower case)
    capitalize() - Only the first character will be converted to upper case and all remaining characters can be converted to lowercase.
'''

loc1 = """XYZ company
        While Field
        Bangalore"""
loc2 = """XYZ company
        Banglore
        Human tech park"""
        
print(loc1)
print(loc2)


s1 = "Welcome to 'python' learning"
s2 = 'Welcome to "python" learning'
s3 = """Welcome to 'python' learning"""

print(s1)
print(s2)
print(s3)

print('----------')

# String slicing

wish = "Hello World"
print(wish[::])
print(wish[:])
print('0:9', wish[0:9])
print('0:9:1', wish[0:9:1])
print('0:9:2', wish[0:9:2])
print('2:4:1', wish[2:4:1])
print('::2', wish[::2])
print('2::', wish[2::])
print(':4:', wish[:4:])
print('-4:-1', wish[-4:-1])

name = "Balayya"
name2 = "Balayya"
print(id(name))
print(id(name2))

message="Python programming language,Python is easy"
n=message.split(",")
print(n)

profile = ['Roshan', 'Actor', 'India']
candidate = '-'.join(profile)
print(profile)
print(candidate)

