def pal(str):
    if(str==str[::-1]):
	print("YES, your string is palindrome")
    else:
	print("NO, your string is not palindrome")


str=input("enter the string")
pal(str)
