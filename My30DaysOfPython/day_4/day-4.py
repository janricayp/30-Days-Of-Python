# 1 Concatenate the string
full_text = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python' 
print(full_text)

# 2 Concatenate the string
full_text = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(full_text)

# 3 Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4 Print the variable company using print().
print(company)

# 5 Print the length of the company string
print(len(company))

# 6 Change all the characters to uppercase
print(company.upper())

# 7 Change all the lowercase to uppercase
print(company.lower())

# 8 Use capitalize(), title(), swapcase() methods 
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9 Cut(slice) out the first word of Coding For All string.
print(company[7:])

# 10 Check if Coding For All string contains a word Coding
print(company.find('Coding'))
print(company.index('Coding'))

# 11 Replace the word coding
print(company.replace('Coding', 'Python'))

# 12 Change Python for Everyone to Python for All 
text = 'Python for Everyone'
print(text)
print(text.replace('Everyone', 'All'))

# 13 Split the string 'Coding For All' using space as the separator (split()) 
company = company.split()
print(company)

# 14 split the string at the comma.
company = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company.split(','))

# 15 What is the character at index 0 in the string Coding For All.
company = "Coding For All"
print(company[0])

# 16 What is the last index of the string Coding For All.
print(company[-1])

# 17 What character is at index 10
print(company[10])

# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
py4e = "Python For Everyone"
acronym = py4e.split()
for word in acronym:
    print(word[0], end='')
print()

# 19 Create an acronym or an abbreviation for the name 'Coding For All'.
company = "Coding For All"
acronym = company.split()
for word in acronym:
    print(word[0], end='')
print()

# 20 Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

# 21 Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

# 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))

# 23 
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# 24 
print(sentence.rindex('because'))

# 25
start = sentence.find('because because because')
end = start + len('because because because')
new_sentence = sentence[:start] + sentence[end:].strip()
print(new_sentence)

# 26
print(sentence.index('because'))

# 28 
print(company.startswith('Coding'))

# 29 
print(company.startswith('coding'))

# 30 
text = '   Coding For All      '
print(text.strip())

# 31 
challenge = '30DaysOfPython'
print(challenge.isidentifier()) 
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) 

# 32 
python_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# ' + " # ".join(python_lib))

# 33
print('I am enjoying this challenge. \nI just wonder what is next.')

# 34
print('Name\t\tAge\tCountry\t\tCity\nAsabeneh\t250\tFinland\t\tHelsinki')

# 35
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square.'.format(radius, area))

# 36
x = 8
y = 6
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y:.2f}")
print(f"{x} % {y} = {x % y}")
print(f"{x} // {y} = {x // y}")
print(f"{x} ** {y} = {x ** y}")