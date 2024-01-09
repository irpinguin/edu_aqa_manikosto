import os


this_file_dir = os.path.dirname(__file__)
project_root = os.path.dirname(this_file_dir)
data = os.path.join(project_root, 'downloads', 'foto.jpg')

print(this_file_dir)
print(project_root)
print(data)
print(os.path.dirname(os.getcwd()))

