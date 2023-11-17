import os
import shutil
import sys


def validate_arguments(args):
    if len(args) < 4:
        print("引数が足りません。")
        return False
    if args[1] not in ["reverse", "copy", "duplicate-contents", "replace-string"]:
        print("無効な操作です。")
        return False
    if not os.path.exists(args[2]):
        print("入力ファイルが存在しません。")
        return False
    return True

def reverse_file(input_path, output_path):
    with open(input_path, "r") as input_file:
        contents = input_file.read()
    with open(output_path, "w") as output_file:
        output_file.write(contents[::-1])

def copy_file(input_path, output_path):
    shutil.copyfile(input_path, output_path)

def duplicate_contents(input_path, n):
    with open(input_path, "r") as input_file:
        contents = input_file.read()
    with open(input_path, "w") as output_file:
        for i in range(n):
            output_file.write(contents)

def replace_string(input_path, needle, new_string):
    with open(input_path, "r") as input_file:
        contents = input_file.read()
    with open(input_path, "w") as output_file:
        output_file.write(contents.replace(needle, new_string))

if __name__ == "__main__":
    args = sys.argv
    if validate_arguments(args):
        operation = args[1]
        input_path = args[2]
        output_path = args[3]
        if operation == "reverse":
            reverse_file(input_path, output_path)
        elif operation == "copy":
            copy_file(input_path, output_path)
        elif operation == "duplicate-contents":
            n = int(args[4])
            duplicate_contents(input_path, n)
        elif operation == "replace-string":
            needle = args[4]
            new_string = args[5]
            replace_string(input_path, needle, new_string)


# コマンド例1 copy
# command = ""python3 /home/kanata99/filemanipulatorprogram/File-manipulator-Program/file_manipulator.py copy input.txt output2.txt


