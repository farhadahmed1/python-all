# country = "Bangladesh"
# for letter in country:
#     print(letter)
#range(start , end , inceres)

# for number in range(10 ,40 ,5) :
# print(number)   


# number pattern using loop 
# 
#   

rows = int (input("Enter number ot rows: "))

for i in  range(rows):
    for j in range(i + 1):
       # print(j+1 , end=" ")
       print("*" , end=" ")

    print('\n')