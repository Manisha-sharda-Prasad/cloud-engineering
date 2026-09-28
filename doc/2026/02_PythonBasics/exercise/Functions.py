# ⭐️ ::::::: Functions ::::::::

#🔸 Function Types PURPOSE: no input-output, only input, input & output, return, multiple outputs:::::::::::::::::::::::::::::::::::::::::::::

# ▪️Parameters and Local Variable ::::::::::::::::::
#  Local Var - accessed inside function only: ('name','cleaned'):
print('------------Parameters & Local Variable--------------')

def clean_name(name):
    cleaned = name.strip().lower()
    #Raw Vs Processed data
    print("Raw :",name)
    print("Cleaned :",cleaned)

clean_name("  MaRia    ")

#print("Raw :",name), print("Cleaned :",cleaned) - error not accessible


# ▪️Global Access Variable ::::::::::::::::::::
# Available entire script: ('case_rule')
print('--------------Global Access Variable----------------')

case_rule = "lower"
def clean(name):
    cleaned = name.strip()
    if case_rule == "lower":
        cleaned = cleaned.lower()
    print("Cleaned :",cleaned)

clean("  SaMia    ")



# ▪️Parameters & Arguments ::::::::::::::::::::
print('---------------Parameters & Arguments----------------')

def full_name_cleaner(first_name, last_name=None, country="n/a"):
    cleaned_first= first_name.strip().capitalize()
    cleaned_last= last_name.strip().capitalize()
    cleaned_full_name = cleaned_first + " " + cleaned_last
    print("Full Name :", cleaned_full_name," From ", country)

    #print(cleaned_first, cleaned_last)

# Positional Arguments: Right Order - No. of Parameters must match No. of Arguments
full_name_cleaner("MARia ", " janE ", "USA")

# Keyword Arguments: Parameters= Arguments - Safety and Readability
full_name_cleaner(country="USA", first_name= "MARia ", last_name= " janE ")

# Mixed Arguments: Not Ideal
full_name_cleaner("MARia "," janE ", country="USA")
#full_name_cleane(firstname="MARia "," janE ", "USA")  : Rule - cannot start with Keyword= At first

# No Arguments/Default: If not passing Arg, throws no error (= default value)
full_name_cleaner("kumar", "abhi")




# ▪️*args & **kwargs ::::::::::::::::::::
# Allow functions to accept unknown no. of args
print('-----------------*args & **kwargs------------------')

def total_sum(a=0, b=0, c=0):
    summ = a + b + c
    print("Total Sum : ", summ)

total_sum(1, 2, 3)

# *args : pass multiple 'Args' with 'Similar Values' (only 1 type: int/string)
def total(*args):
    print(type(args))                                  #type-tuple()
    print("Total sum() *args: ", sum(args))

total(1,22,44,7)

# **kwargs : pass multiple 'Args' with 'Different Names & Values' (any type: int,string)
def user(**kwargs):
    print(type(kwargs))                               #type-dictionary{}
    print(kwargs)

user(name= "Manisha ", id= 123, age = 45, country="USA" )

# ▪️Return ::::::::::::::::::::




# 🔸Function : Action, Validation, Transformation, Orchestration:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

# ▪️Action Functions ::::::::::::::::::::
# Operation which changes outside function : print-Output, connect-Database, send-Msg/Email, call-Api
print('-----------------Action Functions------------------')

#Task -store application log message as app.log in a 'File' -
# with, open(), "a" append, as, write(), file

def write_log(message):
    with open("/Users/manishaprasad/Documents/try/app.log", "a") as file:
        file.write(message + "\n")

#write_log("App Started")                            #commit otherwise: will run each time you run whole program
#write_log("User Logged in")

#note:
#For Windows - (r "C:\Users\manishaprasad\Documents\try\app.log") as file:    Windows file paths starts with C:\, r"specifies not special chars"
#For macOS - ("/Users/manishaprasad/Documents/try/app.log", "a") as file:     uses / forward slash


# ▪️Transformation Functions ::::::::::::::::::::
# 'Raw data' goes in, gets transformed and returns 'processed data'
print('-----------------️Transformation Functions------------------')

#Task - clean email, split it into username and domain
def clean_split_email(email):
    cl_email = email.strip().lower()

    username, domain = cl_email.split("@")
    return {"username": username,
            "domain": domain}

print(clean_split_email(" MANISHA@gmail.com "))


# ▪️Validation /Checker Functions ::::::::::::::::::::
# checks input, rules, permission
print('-----------------️Validation Functions------------------')

#Task - check if password meets the minimum length of 8
def is_valid_password(password):
    len_pass  = len(password) >= 8
    return len_pass

print(is_valid_password("resh567"))
print(is_valid_password("resh56789"))

#Task - check if email has a valid format
def is_valid_email(email):
    return "@" in email and "." in email and ".com" in email #and "yahoo" or "gmail.com"

print(is_valid_email("hoshkl.co"))
print(is_valid_email("hoshkl@gmail.com"))


# ▪️Orchestration Functions ::::::::::::::::::::
# Calling other functions (workflow)
print('-----------------️Orchestration Functions------------------')

#Task- Orchestrator Function
def process_user_email(email):

    write_log("App Started")
    # We must check if it is Valid, If email not valid, we log the problem
    # If Valid, clean it store Structured Information

    if not is_valid_email(email):
        write_log(f"Invalid email received: {email}")
    else:
        clean_email = clean_split_email(email)
        write_log(f"Processed Email: {clean_email}")
    # We log what happened
    write_log("App stopped")


# Input: We receive an email from a user
email = input("Please enter your Email:")

process_user_email(email)