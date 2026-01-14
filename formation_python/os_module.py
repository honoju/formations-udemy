import os

pwd = os.getcwd()
new_directories = os.path.join(pwd, "test", "sous_test")
os.makedirs(new_directories, exist_ok=True)
