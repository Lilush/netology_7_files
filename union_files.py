import os
import pathlib

def union_files(path):
    files_data = []
    directory = pathlib.Path(path)
    for file_object in directory.iterdir():
        with open(file_object) as file:
            data = file.readlines()
            files_data.append((file_object.name , len(data), data))
    files_data.sort(key=lambda x: x[1])

    result_file_name = os.path.join(path, 'result.txt')
    with open(result_file_name, 'w+') as file:
        for file_data in files_data:
            file.write(f"{file_data[0]}\n")
            file.write(f"{file_data[1]}\n")
            for line in file_data[2]:
                file.write(f"{line.strip()}\n")

path = os.path.join(os.getcwd(), 'sorted')
union_files(path)

