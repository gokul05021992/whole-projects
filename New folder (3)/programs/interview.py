#palindrome string
#pattern number loop


# palindrome

str =input('enter the string')
reversedstring = str[::-1]
print("reversed string",reversedstring)
if str == reversedstring:
    print("string is palindrome")
else:
    print("string is not palindrome")