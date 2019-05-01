# Test mule for code

# import os
print("File Management Mule")

#line_list[0]=" "
with open('data.txt', 'w') as f1:
    data = 'some data to be written to the file '
    byte_count = f1.write(data + str(len(data))+'\n')
    byte_count = f1.write(f"bytes in the string = {byte_count}\n")
    data = 'A new line '
    byte_count = f1.write(data + str(len(data))+'\n')
    byte_count = f1.write(f"bytes in the string = {byte_count}\n")

with open('data.txt', 'r') as f3:
    #    byte_count = len(f3.read())
    #    print(f"Total bytes in the file is {byte_count}")

    line_list = 0
    for line in f3:
        print(line, end='')
        # line_list += enumerate(line)
        print(range(len(line)))
    x = [10, 204, 31]
    for i, item in enumerate(x):
        print(i, item)
