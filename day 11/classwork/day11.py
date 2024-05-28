authorized=False
password= "sabasaba123"
while authorized != True:
    user_input= input("do you want to log in:  ")
    if user_input == "yes":
        

        print("ok")
        while authorized != True:
          user_input= input("please enter your password:  ")
if user_input == password:
             print("Acces Granted") 
else:
             print("incorrect try again") 

          
             authorized = True