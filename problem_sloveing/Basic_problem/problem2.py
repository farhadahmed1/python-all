# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"

def formatIpAddress(address):
    ipAddress = ""
    for character in address:
        if(character == '.'):
            ipAddress += "[.]"
        else:       
            ipAddress += character
    return ipAddress; 


address = "255.100.50.0"
result = formatIpAddress(address)
print(result)
                    
