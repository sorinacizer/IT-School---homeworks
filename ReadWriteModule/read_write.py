"""Text file reader class"""
import os
import sys
from pathlib import Path
import time


class FileNameError(Exception):
    pass


class FileExtensionError(Exception):
    pass


class TextFileReader:
    """Text File Reader class
        Atrtibutes:
            - file_name
        Methods:
            - size
            - read_content
            """

    def __init__(self, file_name):
        p = Path(__file__)
        self.file_name = file_name
        self.file_path = str(p.parent / self.file_name)

    def size(self):
        """Return file size"""
        try:
            return os.path.getsize(self.file_name)
        except FileNotFoundError:
            print(f'Cannot get size because {self.file_name} file does not exist@')
            sys.exit(2)

    def read_content(self):
        """Return file content"""
        try:
            with open(self.file_name, 'r') as f_read:
                content = f_read.read()
                return content
        except FileNotFoundError:
            print(f'Cannot get the content of {self.file_name} File does not exist!')
            sys.exit(2)

    @classmethod
    def from_file(cls, files):
        objects = []
        try:
            with open(files, 'r') as f_read:
                for file in f_read:
                    content = file.strip()
                    obj = cls(content)
                    objects.append(obj)
            return objects

        except FileNotFoundError:
            print('The file is missing!')



class TextFileWriter:
    """Text File Writer class
            Attributes:
                - file_name
            Methods:
                 - write_content
                  """

    def __init__(self, file_name):
        """Initialize objects"""
        p = Path(__file__)
        self.file_name = file_name
        if not isinstance(self.file_name, str):
            raise FileNameError('File name needs to be string!')
        if os.path.splitext(self.file_name)[1] != '.txt':
            raise FileExtensionError('File extension must be txt!')
        self.file_path = str(p.parent / self.file_name)

    def write_content(self):
        """Write data to file"""
        text = input('Enter info that you want to enter in file: ')
        with open(self.file_name, 'a') as fw:
            content = fw.write(text + "\n")
        return content

    @classmethod
    def from_file(cls, files):
        objects = []
        try:
            with open(files, 'r') as f_read:
                for file in f_read:
                    content = file.strip()
                    obj = cls(content)
                    objects.append(obj)
            return objects

        except FileNotFoundError:
            print('The file is missing!')


if __name__ == '__main__':
    # text_file = TextFileReader('test.txt')
    # print(__file__)
    # print(text_file.file_name)
    # print(text_file.file_path)
    # print(text_file.size())
    #
    # # with open(text_file.file_path, 'a') as fw:
    # #     fw.write('Irina\nDaniela\nBianca\n')
    #
    # print(text_file.size())
    # print(text_file.read_content())
    #
    # readme = TextFileReader('README.md')
    # print(readme.read_content())
    # print(readme.size())
    #
    # readme1 = TextFileReader('README1.md')
    # print(readme1.read_content())
    # print(readme1.size())


    try:
        text_file1 = TextFileWriter('test1.txt')
        print(text_file1.write_content())

        files = 'files.txt'
        obj = TextFileReader.from_file(files)
        print(TextFileReader.current_time())
        for ob in obj:
            print(f'{ob.file_name}')

        obj1 = TextFileWriter.from_file(files)
        for i in obj1:
            print(i.write_content())




    except FileNameError:
        print('Wrong name!')
    except FileExtensionError:
        print('Wrong extension!')
