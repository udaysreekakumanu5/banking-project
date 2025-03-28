# import random
# password ="ABCDEFGHIJKLMNOPQRSTUV1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+}{:~*/-+?><|"
# # print("enter the password":,end=":")
# # input()
# length_password = int(input("enter the lenght of the password:"))
# a = "".join(random.sample(password,length_password))
# print("your password is", a)

##########################################################################################################################


u =0
l = 0
s= 0
n = 0
passw=(input("enter the password"))
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

small = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
spcl = "~!@#$%^&*()_-+=*/|}{][/<>,.:;`'"

if len(passw)<=10:
    for i in passw:
        if i in caps:
            u += 1
        if i in small:
            l += 1
        if i in num:
             n += 1
        if i in spcl:
            s += 1
    if (u>=1 and l>=1 and s >= 1 and n >= 1):
        print("valid password")
    else:
        if u<1:
            print("atleast 1 uppercase letter is requires")
        if n<1:
            print("atleast 1 number letter is requires")
        if s<1:
            print("atleast 1 spcl letter is requires")
else:
    print("invalid passsword")
           
            
    
    
   
    
        
# if (i in caps and len(passw) <= 10)and ( passw in small and len(passw) <=10 ) and ( passw in num and len(passw)<=10) and ( passw in spcl and len(passw)<=10):
#     print("valid password")
# else:
#     print("invalid password")
    
         
       
    
    
    

    

