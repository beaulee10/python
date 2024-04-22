import os

def main():
    try:
        os.mkdir('MyFiles')
    except FileExistsError:
        print("'MyFiles' already exists")

    subdirectories = ['Docs', 'Images', 'Videos']
    for s in subdirectories:
        try:
            os.mkdir(f'MyFiles/{s}')
        except FileExistsError:
            print(f"Directory '{s}' already exists.")

    files = os.listdir()

    for file in files:
        if file.endswith('.txt'):
            os.mkdir(file, f"Docs/{file}")
            print(f"Moved {file} to MyFiles/Docs/")
        elif file.endswith('.jpg'):
            os.mkdir(file, f"Images/{file}")
            print(f"Moved {file} to MyFiles/Images/")
        elif file.endswith('.mp4'):
            os.mkdir(file, f"Videos/{file}")
            print(f"Moved {file} to MyFiles/Videos/")
        else:
            print(f"File '{file}' matches none of the criteria.")

main()
