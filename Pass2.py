data = {"Username":"","Password":""}
a = input("Username: ")
b = input("Password: ")
c = input("Confirm Password: ")
count = 3
if b==c:
     data["Username"]= a
     data["Password"]= b
    # print(data)
else:
    while True: 
        for i in range(1,count):
            print("Passwords do not much.\nTry Again!\n")
            b = input("Password: ")
            c = input("Confirm Password: ")
            if b==c:
                data["Username"]= a
                data["Password"]= b
                print(data)
                break
            
        print("\nYou have no more attempts!!!")  
        break
new_data = {"Email":"frarthur1230@gmail.com"}
data.update(new_data)

##newly updated
data.update(Phone="0549987904")
print(data)