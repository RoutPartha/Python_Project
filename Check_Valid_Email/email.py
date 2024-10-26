email=input("Enter Your Email: ")#g@g.in-->Closest function of gmail
k,j,d=0,0,0
if len(email) >=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if(email[-4]==".") ^ (email[-3]=="."):
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Error due to space or upper case")
                else:
                    print("Right Email")
            else:
                print("Error due to dot is not present in right position")
        else:
            print("@ is missing or more @ is present")

    else:
        print("Correct the starting letter of the email")
else:
    print("error due to size")
