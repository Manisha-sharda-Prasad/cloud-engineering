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

#store application log message as app.log in a 'File' -
# with, open(), "a" append, as, write(), file

def write_log(message):
    with open("/Users/manishaprasad/Documents/try/app.log", "a") as file:
        file.write(message + "\n")

#write_log("App Started")                            #commit otherwise: will run each time you run whole program
#write_log("User Logged in")


#note:
#For Windows - (r "C:\Users\manishaprasad\Documents\try\app.log") as file:    Windows file paths starts with C:\, r"specifies not special chars"
#For macOS - ("/Users/manishaprasad/Documents/try/app.log", "a") as file:     uses / forward slash