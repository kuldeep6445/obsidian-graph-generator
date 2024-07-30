import pathlib
import re

folder_path = '/home/nether/Documents/Obsidian Vault'
word_dict = {}

def findall(x):
    reading = False
    tags = []
    temp = ''
    for i in range(len(x)):
        if reading:
            if x[i]==' ':
                reading = False
                if len(temp)!=0 and temp not in tags:
                    tags.append(temp)
                temp = ''
            elif x[i]=='#':
                reading = False
                
        else:
            if x[i]=='#':
                reading = True


def find_tags(file_path):
    with open(file_path,'r') as fp:
        code_block = 0
        for line in fp:
            try: 
                if '```' in line:
                    code_block = (code_block + 1)%2
                matches = findall(line)
                for match in matches:
                    word_dict[match].append(str(file_path)) 
                    print(f"match -> {match}, file path -> {file_path}")
            except:
                continue

def read_files_recursively(folder_path):
    folder = pathlib.Path(folder_path)

    for file_path in folder.rglob('*.md'):
        if file_path.is_file():
            find_tags(file_path)
            #print(file_path)

read_files_recursively(folder_path)

