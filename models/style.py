import pycodestyle

#creating a StyleGuide instance
style_checker = pycodestyle.StyleGuide()

#Run pep8 on multiple files
result = style_checker.check_files(['test_base_model.py',])

print(result.messages)