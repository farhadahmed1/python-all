# data encryption and decryption

data = 'goodmorning'
# shift how many bytes shaft data
shift = 4
encryption  = ''
for character in data: 
    encryption += chr ((ord(character)+shift-97) % 26+97)

print(encryption)    
