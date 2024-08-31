#with open('/Users/bartlomiejszafran/Desktop/text.txt') as file:
    #read = file.read() #Read the file
#write = file.write("Add new text here") #Add new text in the bracket. Remember to add mode = "w"(change the whole text) or 'a' (append). open('text.txt, mode='w')

    #print(read)
  
PLACEHOLDER = "[name]"
    
with open ("/Users/bartlomiejszafran/Desktop/Mail Merge Project Start/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    print(names)
    
with open("/Users/bartlomiejszafran/Desktop/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"/Users/bartlomiejszafran/Desktop/Mail Merge Project Start/Output/ReadyToSend/letter_for_{stripped_name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)