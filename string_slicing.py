mystr = "kuntal is a good boy"
print(len(mystr)) # length of strings including spaces
print(mystr[0:19])

# if I want to skip characters
print(mystr[0:5:2]) # skips two characters
print(mystr[0::2]) # skips two characters for the entire string
print(mystr[:5:2]) # skips two characters till length 5

print(mystr[-4:-2])

print(mystr.isalnum()) # test if it is alphanumeric
print(mystr.count("o")) # counts the number of 0
print(mystr.find("is")) # find the "is" string in the string
print(mystr.upper()) # converts to uppercase
print(mystr.replace("is","are")) # replaces is to are 


