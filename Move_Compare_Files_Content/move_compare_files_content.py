"""Move/Compare Files Content"""
import csv
import sys
import pandas as pd


def read_content_txt(file_name):
    """Return content of a text file"""
    try:
        with open(file_name, "r") as f_read:
            content = f_read.read()
        return content
    except FileNotFoundError as e:
        print('The txt file is missing!')


def read_content_csv(file_name):
    """Return content of a csv file"""
    try:
        lst = []
        with open(file_name, "r") as f_read:
            content = csv.reader(f_read)
            for row in content:
                lst.append(row)
        return lst
    except FileNotFoundError:
        print('The csv file is missing!')


def move_content_txt(file_name1, operator, file_name2):
    """Function that returns the content of the file_name1 in the file_name2"""
    if operator == '>':
        content_file_txt = read_content_txt(file_name1)

        with open(file_name2, 'w') as f_write:
            content_file2 = f_write.write(content_file_txt)

    else:
        raise UnboundLocalError('If you want to move content from first file in second, use the right operator: >')

    return content_file2


def move_content_csv(file_name1, operator, file_name2):
    """Function thet returns the content of the file1 in file 2"""
    content_file_csv = read_content_csv(file_name1)
    with open(file_name2, "a", newline='') as fw:
        writer = csv.writer(fw)
        writer.writerows(read_content_csv(file_name1))
    return writer


def compare_content(file_name1, operator, file_name2):
    """Function that returns TRUE if the content of the both files is the same and FALSE if otherwise"""
    file1 = read_content_txt(file_name1)
    file2 = read_content_txt(file_name2)

    file1_csv = read_content_csv(file_name1)
    file2_csv = read_content_csv(file_name2)

    file1_excel = pd.read_excel(file_name1)
    file2_excel = pd.read_excel(file_name2)

    if file1 == file2 or file1_csv == file2_csv or file1_excel.equals(file2_excel):
        return True
    else:
        return False


if __name__ == "__main__":
    print(sys.argv[1], sys.argv[2], sys.argv[3])
    extensie = sys.argv[1][sys.argv[1].rfind('.')::]
    if sys.argv[2] == '>' and extensie == '.txt':
        move_content_txt(sys.argv[1], sys.argv[2], sys.argv[3])
    elif sys.argv[2] == '>' and extensie == '.csv':
        move_content_csv(sys.argv[1], sys.argv[2], sys.argv[3])
    if sys.argv[2] == '==':
        print(compare_content(sys.argv[1], sys.argv[2], sys.argv[3]))
