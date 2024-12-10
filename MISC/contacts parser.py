file = open("C:/Users/carso/Documents/Cam_contacts.txt")

name = ""
phone_num = ""

for line in file:
    if not line.strip():  # Check if the line is empty
        continue  # Skip to the next iteration
    if line[0] == " ":  # Check if the line starts with a space
        continue
    line_break = line.split(':')
    line_1 = line_break[0]
    line_2 = line_break[1]


    if line_1 == "FN":
        name = line_2
    if line_1 == "TEL;CELL":
        phone_num = line_2
        finished_line = name + " : " + phone_num
        print(finished_line) 