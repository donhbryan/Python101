# Test mule for code

# import os
print("File Management Mule")

#line_list[0]=" "
with open('data.txt', 'w') as f1:
    data = 'some data to be written to the file\n'
    byte_count = f1.write(data)
    byte_count = f1.write(f"bytes in the string = {byte_count}\n")
    data = 'A new line\n'
    byte_count = f1.write(data)
    byte_count = f1.write(f"bytes in the string = {byte_count}\n")

with open('data.txt', 'r') as f3:
#    byte_count = len(f3.read())
#    print(f"Total bytes in the file is {byte_count}")
    
    for line in f3:
            line_list: list
            print(line, end='')
            line_list += [line]
#print(line_list)
