str = 'Hello'
curr_char = 'l'
new_char = 's'
result = ''

for char in str:
    if char == curr_char:
        result += new_char
    else:
        result += char    

# str = str.replace(curr_char, new_char)
print(result)

           

