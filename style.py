import pycodestyle

#creating a StyleGuide instance
style_checker = pycodestyle.StyleGuide()

#Run pep8 on multiple files
result = style_checker.check_files(['console.py',])

print(result.messages)