import string

def ispangram(str)
   alphabet="abcdefghijklmnopqrstuvwxyz"
   for char in alphabet:
       if char not in str.lower():
          return False

   return True

#driver code
string = 'the quick brown fox jumps over the lazy dog'
if(ispangram(string)==True):
    print("Yes, it is a pangram")
else:
    print("No, it is not a pangram")
