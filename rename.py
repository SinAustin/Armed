import os
path = 'Path to images'
files = os.listdir(path)
i = 1

for file in files:
    os.rename(os.path.join(path, file), os.path.join(path, 'What to rename images.' '.image type'))
    i = i+1
