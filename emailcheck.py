print("Hello to the email checker")
print("This is the version 4 ")

Email = input("emter the email id you want to check ")

parts = Email.split('@')
x=0
for i in range(len(parts)):

    if any(char.isdigit() for char in parts[i]):
            x=1
            break
    else:
         x=0
            
              
if(x==1):
    print("Sorry this is not a valid email.")
else:
     print("This is a valid email")



