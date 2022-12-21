# data ="aNtEtirodtU\n\p\t>>"
# new_data = data.lower()
# output_data = ''
# for character in new_data:
#     if(character== 'a' or character=="e" or character=="i" or character=="o" or character=='u'):
#       output_data += character + " "
#     #   print(f"{character}")
# print(output_data)    

address = "1.1.1.1"
out_put = ""
for new_address in address:
    if(new_address == '.'):
       out_put +="[.]"
print(out_put)       
