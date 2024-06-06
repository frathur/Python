data = {"Username":"","Password":""}
Username = input("Username: ")
Password = input("Password: ")
Confirm_Password = input("Confirm Password: ")
count = 3
if Password==Confirm_Password:
     data["Username"]= Username
     data["Password"]= Password
    # print(data)
else:
    while True: 
        for i in range(1,count):
            print("Passwords do not much.\nTry Again!\n")
            b = input("Password: ")
            Confirm_Password = input("Confirm Password: ")
            if b==Confirm_Password:
                data["Username"]= Username
                data["Password"]= Password
                print(data)
                break
            
        print("\nYou have no more attempts!!!")  
        break
new_data = {"Email":"preach.342.55@gmail.com"}
data.update(new_data)

##newly updated
data.update(Phone="0543730305")
#print(data)
print("\nWelcome ",Username, ". Your information is safe with us.")
for (a,b) in data.items():
    print(a ,": ",b)