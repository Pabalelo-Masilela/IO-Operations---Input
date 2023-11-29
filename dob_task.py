'''This progran is designed to call a file containing information stored 
and print out categorised parts of this information in a line by line form'''
# open file named DOB.txt with reading mode of access
# Create empty variable for 'Name"
# Create empty variable for 'Birthdate'
# Use a loop to exceute the following:
    # Print each line of the file as a seperate string
    # Seperate elements of this string by each space character
    # Use indexing for range[0-2] to add those characters to 'name'
    # Use indexing for range[2-4] to add those characters to 'birthdate'
dob_info = open('DOB.txt','r+')
name = "Name"
birthdate = "Birthdate"
for line in dob_info:
    line_string_list = line.split()
    name = f"{name}\n{line_string_list[0]} {line_string_list[1]}."
    birthdate = f"{birthdate}\n{line_string_list[2]} {line_string_list[3]} {line_string_list[4]}."
print(f"{name} \n\n{birthdate}")
dob_info.close()