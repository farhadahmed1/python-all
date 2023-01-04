# Input: command = "G()()()()(al)"
# Output: "Gooooal"

def interpret(command):
    command = command.replace('()' , 'o')
    command = command.replace('(al)' , 'al')
    return command
 
command = "G()()()()(al)" 
output =  interpret(command)
print(output)
