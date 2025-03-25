x1 = input()
x2 = input()
y1 = input()
y2 = input()
y3 = input()
z = input()

# swap the values of `x1` and `x2`

# do a circular swap of `y1`, `y2` and `y3`  like y1 = y2, y2 = y3, y3 = y1 

# create a new variable `a` with the value of `z`

# delete the variable `z`

print(x1)
print(x2)
print(y1)
print(y2)
print(y3)
print(a)









x1 = input()
x2 = input()
y1 = input()
y2 = input()
y3 = input()
z = input()

# swap the values of `x1` and `x2`
x1,x2 = x2,x1

# do a circular swap of `y1`, `y2` and `y3`  like y1 = y2, y2 = y3, y3 = y1 
y1,y2,y3 = y2,y3,y1

# create a new variable `a` with the value of `z`
a = z

# delete the variable `z`
del z

print(x1)
print(x2)
print(y1)
print(y2)
print(y3)
print(a)


#GA-2

# A single quote ' and a double quote "
output1 = ...

# A forward slash / and a backward slash \
output2 = ...

# Three single quotes ''' and three double quotes """
output3 = ...

# Double forward slash // and Double backward slash \\
output4 = ...




# A single quote ' and a double quote "
output1 = 'A single quote \' and a double quote "'

# A forward slash / and a backward slash \
output2 = 'A forward slash / and a backward slash \\' 

# Three single quotes ''' and three double quotes """
output3 = "Three single quotes ''' and three double quotes \"\"\"" 

# Double forward slash // and Double backward slash \\
output4 = "Double forward slash // and Double backward slash \\\\"




#GA-3

# part 1 - If pattern
word = "glow" # str
continuous_tense = True # bool

# part 2
age = 5 # int
is_member = True # bool

# part 3

color_code = "R" # str: valid values are R-red, G-green and B-blue

time = "02 PM" # str, format:[2-digit hour][space][AM or PM]
# Morning (6 AM - 12 PM) (including the start and excluding the end)
# Afternoon (12 PM - 6 PM) 
# Evening (6 PM - 12 AM)
# Night (12 AM - 6 AM)

# <eoi>

# part 1 - basic if

new_word = word # donot remove this line

# remove the "ing" suffix from `new_word` if it is there
if ... :
    ...

# add the suffix "ing" to `new_word` if `continuous_tense` is True
# write the whole if else block here

# part 2 - If else pattern

# age_group:str should be "Adult" or "Child" based on the age. assume age greater than or equal to 18 is adult.
if ...:
    ...
else:
    ...

# applicant_type:str should be age goup with the member status like "Adult Member" or "Child Non-member"
# write the whole if else block

# part 3 if ... elif .. else

# based on the value of `color_code` assign the `color` value in lower case and "black" if `color_code` is none of R, B and G

if ...
elif ...:
        ...
elif ...:
    ...
else:
    ...

is_time_valid = ... # bool: True if time is valid (should be ranging from 1 - 12 both including) else False 

# time_in_hrs:int should have the time in 24 hrs format . Try to do this in a single expression
time_in_hrs = ...

# time_of_day:str should have the time of the day as Morning, etc.. use "Invalid" if not withing the acceptable range

# write your code here





# part 1 - If pattern
word = "glow" # str
continuous_tense = True # bool

# part 2
age = 5 # int
is_member = True # bool

# part 3

color_code = "R" # str: valid values are R-red, G-green and B-blue

time = "02 PM" # str, format:[2-digit hour][space][AM or PM]
# Morning (6 AM - 12 PM) (including the start and excluding the end)
# Afternoon (12 PM - 6 PM) 
# Evening (6 PM - 12 AM)
# Night (12 AM - 6 AM)

# <eoi>

# part 1 - basic if

new_word = word # donot remove this line

# remove the "ing" suffix from `new_word` if it is there
if new_word[-3:] == "ing" :
    new_word = new_word[:-3]

# add the suffix "ing" to `new_word` if `continuous_tense` is True
# write the whole if else block here

if continuous_tense:
    new_word=new_word+"ing"

# part 2 - If else pattern

# age_group:str should be "Adult" or "Child" based on the age. assume age greater than or equal to 18 is adult.
if age<18:
    age_group = "Child"
else:
    age_group = "Adult"

# applicant_type:str should be age goup with the member status like "Adult Member" or "Child Non-member"
# write the whole if else block

if is_member:
    applicant_type = age_group+" "+"Member"
else:
    applicant_type = age_group+" "+"Non-member"

# part 3 if ... elif .. else

# based on the value of `color_code` assign the `color` value in lower case and "black" if `color_code` is none of R, B and G

if color_code=="R":
    color = "red"
elif color_code == "G":
        color = "green"
elif color_code == "B":
    color = "blue"
else:
    color = "black"

is_time_valid = 0<int(time[:2])<=12 # bool: True if time is valid (should be ranging from 1 - 12 both including) else False 

# time_in_hrs:int should have the time in 24 hrs format . Try to do this in a single expression
time_in_hrs = int(time[:2])%12 + (time[-2:] == "PM") * 12

# time_of_day:str should have the time of the day as Morning, etc.. use "Invalid" if not withing the acceptable range

# write your code here

if not is_time_valid:
    time_of_day = "Invalid"
elif 0 <= time_in_hrs < 6:
    time_of_day = "Night"
elif 6<= time_in_hrs < 12:
    time_of_day = "Morning"
elif 12<= time_in_hrs < 18:
    time_of_day = "Afternoon"
elif 18<= time_in_hrs < 24: # you could also use else here.
    time_of_day = "Evening"






# #GA-4 Problem Type: Standard Output - Standard Output

# You are tasked with creating a multi-purpose application that performs various operations based on user input. The application should take the operation name from the input and execute the corresponding task.

# The operations your application should support are as follows:

# Odd number checker: Check whether the input number is odd.
# Name: odd_num_check
# Inputs: number:int
# Output: "yes" if the number is odd, "no" otherwise.
# Perfect square checker: Check whether the input number is a perfect square.
# Name: perfect_square_check
# Inputs: number:int
# Output: "yes" if the number is a perfect square, "no" otherwise.
# Vowel checker: Check if a string has a vowel in it.
# Name: vowel_check
# Inputs: text:str
# Output: "yes" if the string contains a vowel, "no" otherwise.
# Divisibility checker: Check if a number is divisible by 2 or 3.
# Name: divisibility_check
# Inputs: number:int
# Output: "divisible by 2" if the number is divisible by 2, "divisible by 3" if divisible by 3, "divisible by 2 and 3" if divisible by both, "not divisible by 2 and 3" otherwise.
# Palindrominator: Takes a string and joins it with the same string reversed. Eg. "cal" -> "calac".
# Name: palindrominator
# Inputs: text:str
# Output: string representing the input string joined with its reverse(the last characte should not be repeated twice)
# Simple interest calculator with inputs with a higher interest rate if long term.
# Name: simple_interest
# Inputs: principal_amount:int, n_years:int (number of years)
# Output: Simple interest with a 5% interest rate if less than 10 years, else 8%. Round the result to integer using round function.
# If the operation name is not any of the above print "Invalid Operation".



# Take operation name from input
operation = input()

if operation == "odd_num_check":
    # Odd number checker
    number = int(input())
    if number % 2 == 0:
        print("no")
    else:
        print("yes")

elif operation == "perfect_square_check":
    # Perfect square checker
    number = int(input())
    if int(number**0.5)**2 == number:
        print("yes")
    else:
        print("no")

elif operation == "vowel_check":
    # Vowel checker
    string = input().lower()
    if ("a" in string or "e" in string or "i" in string or "o" in string or "u" in string) :
        print("yes")
    else:
        print("no")

elif operation == "divisibility_check":
    # Divisibility checker
    number = int(input())
    if number % 2 == 0:
        if number % 3 == 0:
            print("divisible by 2 and 3")
        else:
          print("divisible by 2")
    elif number % 3 == 0:
        print("divisible by 3")
    else:
        print("not divisible by 2 and 3")

elif operation == "palindrominator":
    # Palindrominator
    string = input()
    palindrome = string + string[-2::-1]
    print(palindrome)

elif operation == "simple_interest":
    # Simple interest calculator
    principal_amount = float(input())
    n_years = int(input())
    if n_years < 10:
        interest_rate = 0.05
    else:
        interest_rate = 0.08
    simple_interest = principal_amount * interest_rate * n_years
    print(int(simple_interest))

else:
    print("Invalid Operation")





#GA-5
main_dish = input()
time_of_day = int(input())
has_voucher =   ...
is_card_payment = ...

if main_dish == "panner tikka":
    cost = 250
    elif main_dissh == "butter chikcen":
        cost == 240
    elif main_dish = "masal dosa":
        cost = 200
    else: # if main dish is invalid print invalid dish and exit the code.
       print("Invalid main dish")
       exit() 

    if time_of_day >= 12 and time_of_day =< 15:
        total_cost = (1 - 0.15) * cost

    eles
        total_cost = cost

    if has_voucher
        total_cost =* 0.9  # Apply voucher discount

    if is_card_payment  # service charge for card payments
        service_charge = 0.05 * total_cost
        total_cost =+ servcie_charge

    print(f"{total_cost:.02f}")



main_dish = input()
time_of_day = int(input())
has_voucher = input() == "True"
is_card_payment = input() == "True"

if main_dish == "paneer tikka":
    cost = 250
elif main_dish == "butter chicken":
    cost = 240
elif main_dish == "masala dosa":
    cost = 200
else:
    print("Invalid main dish")
    exit()

if time_of_day >= 12 and time_of_day <= 15:
    discount = 0.15 * cost
    total_cost = cost - discount
else:
    total_cost = cost

if has_voucher:
    total_cost *= 0.9  # Apply voucher discount

if is_card_payment:  # service charge for card payments
    service_charge = 0.05 * total_cost
    total_cost += service_charge

print(f"{total_cost:.02f}")







