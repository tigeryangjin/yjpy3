filename = 'learning_python.txt'

print('--- Reading in the entire file:')
with open(filename) as f:
    contents = f.read()
print(contents.replace('Python','C'))


