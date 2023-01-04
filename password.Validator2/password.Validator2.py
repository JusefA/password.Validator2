#get password
password = input()

#checks if it has atleast 7 characters
if len(password) < 7:
    print("weak")
    exit()

#count numbers
numbers = 0;
for i in password:
    if i.isnumeric():
        numbers += 1

#check if password has atleast 2 numbers
if numbers < 2:
    print("weak")
    exit()

#all special characters
special = ["!","@",",","#","$","%","&","*"]

#counts special digits
speacial_count = 0;
for i in password:
    for j in special:
        if i == j:
            speacial_count += 1

#check if password has atleast 2 special characters
if(speacial_count < 2):
       print("weak")
       exit()

#all checks passed
print("Strong")
exit()
