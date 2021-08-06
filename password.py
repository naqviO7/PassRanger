# => Password Generator and Manger
# => Will Generates passowrd according to user's choice and amange them
# => save passwords in a file and when user wants to see it will show them
# => convertes plain text password into encrypted password

import random
import array
import string 
from cryptography.fernet import Fernet


#function to get key from file
#without key encryption would not be possibel
def Reterive_Key():
    file= open('key.key','rb')
    key=file.read()
    file.close()
    return key  


# => function to print menu
def MENU():
    # => printing menu title
    print("="*49)
    print("="*20,"M E N U","="*20)
    print("="*49)
    
    print(" -> Press 1 to Generate Simple Password!")
    print(" -> Press 2 to Generate Strong Password!")
    print(" -> Press 3 to View Password!")
    print(" -> Press 0 to Quit!")
    
    print("="*49)
    
    # => defining heading of username and password
    file = open("pwds.txt","w")
    file.write("Usernames\t\t" + " | " + "\tEncrypted Passwords"+"\n\n")


    
# => function will generate strong password
# => password will be generated randomly
# => passwords will be composed of characters and symbols
def Generate_Strong_Password():
    # => maximum length of password needed
    # => this can be changed to suit your password length
    MAX_LEN = 12
    # => fixed length of 12 characters to make strong passwords

    # => declare arrays of the character that we need in out password
    # => Represented as characterss to enable easy string concatenation
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
      
    lowcase_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  
    uppercase_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
  
    symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', 
               '|', '~', '>', '*', '(', ')', '<']
  
    # => combines all the character arrays above to form one array
    combined = digits + uppercase_characters + lowcase_characters + symbols
  
    # => randomly select at least one character from each character set above
    rand_digit = random.choice(digits)
    rand_upper = random.choice(uppercase_characters)
    rand_lower = random.choice(lowcase_characters)
    rand_symbol = random.choice(symbols)
  
    # => combine the character randomly selected above
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
  
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(combined)
  
        # => converting temporary password into array  
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)
  
    # => traverse the temporary password array and append the characters
    # => to form the new password
    password = ""
    
    for x in temp_pass_list:
        password = password + x
    
    username=input("Enter Username: ")      
    # => printing passwords
    
    key=Reterive_Key()
    
    # => intialize fernet module
    fer=Fernet(key)
    
    print("Generated Password:",password)
    
    # => opeining file in a loop
    # => it will continuosuly add passwords
    
    with open("pwds.txt","a+") as file:
        file.write(username + "\t\t\t"  + str(fer.encrypt(password.encode())) + "\n")

    file.close()


# => this function will generate simple 
# => string based passwords excluding characters, digits and symbols
def Generate_Simple_Password():
    # => taking input from user
    username=input("Enter Username: ")
    
    # => generating random passwords
    password = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(12))
    
    # => printing passwords
    print("Generated Password:",password)
    
    key=Reterive_Key()
    #intialize fernet module
    fer=Fernet(key)

    # => opeining file in a loop
    # => it will continuosuly add passwords
    with open("pwds.txt","a+") as file:
        file.write(username + "\t\t\t"  + str(fer.encrypt(password.encode())) + "\n")
    
    file.close()


# => function to generate random key
# => it will generate key and store it in a sperate file
# => this function should be called once otherwise it will cause errors
def Write_Key():
    key=Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)


    
# => function to display usernames
# => and passwords in python code
def View_Password():
    # => opening file 
    # => for viewing passwords and usernames
    
    key=Reterive_Key()
    # => intialize fernet module
    fer=Fernet(key)
    
    with open("pwds.txt","r") as file:
        for line in file.readlines():
            data=line.rstrip()
            username,password=data.split("|")
       
            # => printing usernames and passwords
            print("UserName: ",username,"| Decrypted Passowrd: ",fer.decrypt(password.encode().decode))
       

# => user defined main function 
# => where execution starts 
def Main_Function():
    MENU()
    opt=int(input('Enter Key to Perform Operation: '))
    
    if opt==1:
        Generate_Strong_Password()
    
    elif opt==2:
        Generate_Simple_Password()
        
    elif opt==3:
        View_Password()
    
    elif opt==0:
        exit()
        
    else:
        print("OOps...Invalid Option!")
        
# => calling main function        
Main_Function()
