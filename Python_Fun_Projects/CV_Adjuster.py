import os
from docx import Document


# Define placeholders
PLACEHOLDER = "[position]"
COMPANY = "[company]"

document = Document('/Users/bartlomiejszafran/Desktop/CV/CV.docx')

# Get user input
position = input("What is the position: ")
company = input("What is the name of the company: ")

# Path to the original .docx CV file
with open('/Users/bartlomiejszafran/Desktop/CV/CV.docx') as cv_file:
    document = cv_file.read()
    print(document)
    new_cv = document(PLACEHOLDER, po