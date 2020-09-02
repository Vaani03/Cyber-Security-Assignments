def case(a):
    u=0
    l=0
    for i in a:
        if(i.isupper()):
            u=u+1
        elif(i.islower()):
            l=l+1
        else:
             pass
        return u,l
a=input("enter your string")
u,l=case(a)
print("number of upper case : ",u)
print("number of lower case : ",l)
