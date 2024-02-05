""" Creati un modul care contine doua clase, una de citire din fisier si alta care scrie in fisier"""
class WriteFile:
    """Write class"""
    def __init__(self, file_name):
        self.file_name = file_name

    def write_content(self):
        text = input('Enter your text: ')
        with open(self.file_name, "a") as f_write:
            content = f_write.write(text + "\n")
        return content

class ReadFile:
    """Read file class"""
    def __init__(self, file_name):
        self.file_name = file_name

    def read_content(self):
        with open(self.file_name, "r") as f_read:
            content = f_read.read()
        return content



if __name__ == "__main__":
    file_1 = WriteFile('../new_text_doc.txt')
    print(file_1.write_content())
    file_2 = ReadFile('../new_text_doc.txt')
    print(file_2.read_content())

