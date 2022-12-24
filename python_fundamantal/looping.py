numbers =[23, 4, 5, 66, 78, 96,97,7,9]
marks  = { "math":88 , 'english':90 , 'physics':85 ,'chemistry':76 }
# total  = sum(numbers)
# print(total)

#  list 
# loop through the numbers and print and sum 

total = 0
for i in numbers:
    total += i
    # print(i)
print(f'Sum of the total values : {total}')    

# set 
num_set = { 23, 4, 5, 66, 78, 96,97,7,9, 69 }


for num  in num_set:
    total += num
print(f'Sum of the total set values : {total}')    

# tuple loop through
num_tuple = 23, 4, 5, 66, 78, 96,97

for nums in num_tuple:
    total+= nums
print(f'Sum of the total tuple value: {total}')    

for mark in marks:
    value = marks[mark]
    print(mark , value)

for subject, mark in marks.items():
    print(subject, mark)


# enumerate use for index 

for index , num in enumerate(numbers):
    print(index ,num)

    



