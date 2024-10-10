    # eMAIL sLICER
email = input("Enter your email: ")
eDict = dict()
def eMailSlicer( self, eDict ):
    User_name , Domain_name = self.split("@")
    print(f"username = {User_name}\ndomain_name = {Domain_name}")
    if User_name not in eDict:
        eDict[f"{User_name}"] = f"{Domain_name}"
    else :
        print("Error, Username already exist in record")
    return eDict
itrator = int(input("\nTo seprate user name and domain name enter 1 , to exit enter 0: "))
while itrator:
    eDict = eMailSlicer(email,eDict)
    itrator = int(input("\nTo carry on enter 1 , to exit enter 0: "))
else:
    print("End")