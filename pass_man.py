#project by: Daniel A. dos Santos

#import module
import random
#assistant variable and array
save = []
cont = 0
#password components
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "!@#$%^*()_+="
#password composition
for_pass = upper_case + lower_case + numbers + symbols
password_length = 12
#password generating and saving
answer = input("Generate a password? Y-Yes or N-No \n")
while ((answer == 'Y') or (answer == 'y')):
    password = "".join(random.sample(for_pass, password_length))
    print ("  Generated password: ", password)
    save_option = input("Save this password? Y-Yes or N-No \n")
    if ((save_option == 'Y') or (save_option == 'y')): 
        save.insert(cont, password) 
        cont += 1
    generate_new_password = input("Generate a new password? Y-Yes or N-No :   \n" )
    if ((generate_new_password == 'Y') or (generate_new_password == 'y')):
        generate_new_password = answer
    else:
        break
#show saved passwords slots
load_pass = input("Consult saved passwords? Y-Yes or N-No \n")
if ((load_pass == 'Y') or (load_pass == 'y')): 
    for i in range (len (save)):
        print ("  Slot",i,":",save[i])
    if not save:
        print ("\n No saved passwords \n")
else:
    exit ()