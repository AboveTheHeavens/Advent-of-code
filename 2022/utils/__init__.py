import sys
import os

def __get_file_data(filepath: str) -> list[str]:
    with open(filepath,'r',encoding="utf-8") as f:
        return f.readlines()

def get_demo_data():
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    filepath = os.path.join(path,'demo-input.txt')
    return __get_file_data(filepath)

def get_input_data():
    path = os.path.abspath(os.path.dirname(sys.argv[0]))
    filepath = os.path.join(path,'input.txt')
    return __get_file_data(filepath)