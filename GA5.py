# age = ... # int: Read a number as integer from standard input
# dob = ... # str: Read a string of format dd/mm/yy from standard input
# day, month, year = ... # int, int, int: Get the correct parts from dob as int

# fifth_birthday = ... # str: fifth birthday formatted as day/month/year 

# last_birthday = ... # str: last birthday formatted as day/month/year

# tenth_month = ... # str: dob same day after 10 months formatted as day/month/year

# # print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
# print(...)

# weight = ... # float: Read a number as float from stdin(Standard input)

# weight_readable = ... # str: reformat weight of format 55 kg 250 grams

# # print weight_readable 
# print(...)







# age = int(input()) # int: Read a number as integer from standard input
# dob = input() # str: Read a string of format dd/mm/yy from standard input
# day, month, year = int(dob[:2]), int(dob[3:5]), int(dob[6:]) # int, int, int: Get the correct parts from dob as int

# fifth_birthday = str(day)+"/"+str(month)+"/"+str(year+5) # str: fifth birthday formatted as day/month/year 

# last_birthday = str(day)+"/"+str(month)+"/"+str(year+age) # str: last birthday formatted as day/month/year

# month += 10
# month, year = (month-1)%12+1, year+(month-1)//12
# tenth_month = str(day)+"/"+str(month)+"/"+str(year) # str: dob same day after 10 months formatted as day/month/year

# # print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
# print(tenth_month,fifth_birthday,last_birthday, sep=", ")

# weight = float(input()) # float: Read a number as float from stdin(Standard input)

# kg = int(weight)  # Get the integer part (kg)
# grams = int((weight - kg) * 1000)  # Get the fractional part converted to grams

# weight_readable = str(kg)+" kg "+str(grams)+" grams" # str: reformat weight of format 55 kg 250 grams

# # print weight_readable 
# print(weight_readable)


# novel="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# novel=list(novel.split(" "))
# print(novel)
# d={}
# for x in novel:
#     d[x]=0
# max=0
# answer= ' '
# for x in novel:
#     d[x]=d[x]+1
#     if (d[x])>max:
#         max=d[x]
        
lst=[1,2,3,4,5,6,7,8,9]
new=[ ]
for i in lst:
    if i%2 !=0:
        new.append(i)
print(new)

f=open('newfile.txt','w')
f.write('this is the first line')



