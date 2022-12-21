input_number = int(input("Enter the number : "))
num = 0
while num <=input_number:
    print(num)
    num = num + 1

for  num  in input_number:
     num = num + 1
     print(num)

# total calculation or total number calculation

total = 0
while num <= input_number:
    total = total + num
    print(num)
    num +=1
print(f"sum of the total number : {total}")    

# even and odd numbers
sum =0
while num <= input_number:
    num += 1
    if num % 2 == 1:
        continue
    sum += num
    print(num)
print(f"sum of the even number : {sum}")
# even  and odd numbers sum together
even_sum = 0
odd_sum = 0
while num < input_number:
    num += 1
    if num % 2 == 0:
        odd_sum += num
        # print(f'even number : {num}')
    else:
        even_sum += num
       # print(f'odd number : {num}')

print(f" even sum {even_sum} and also odd sum {odd_sum}")











    

   

