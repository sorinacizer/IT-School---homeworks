"""Create a function/method/attribute that returns the network element name (e.g dummy_network_element) from the input text."""
import pandas as pd
import os


class ReadNetworkElement:
    """ReadNetwoekElement class
        Attributes: - net_elem_name
        Methods:
                 - get_column_by_name"""

    def __init__(self, net_elem_name):
        """Initialize the constructor"""
        self.network_elem_name = net_elem_name

    # def get_column_name(self, column_name):
    #     """Function that returns all data under a specified column"""
    #     with open(self.network_elem_name, 'r') as f_read:
    #         content = f_read.readlines()
    #
    #     ind = [7, 9, 10, 11, 12, 13, 14, 15]
    #     new_content = ''.join(content[i] for i in ind)
    #     # new_content = content[7].__add__(content[9]).__add__(content[10]).__add__(content[11]).__add__(content[12]).__add__(content[13]).__add__(content[14]).__add__(content[15])
    #
    #
    #     with open('column_info.txt', 'w') as f_write:
    #         f_write.write(new_content)
    #
    #     data_frame = pd.read_csv('column_info.txt', delimiter='\t')


    @classmethod
    def from_file(cls, file):
        """Alternative constructor
            Read object attributes from a .txt file
            Return a list with the objects"""
        if not os.path.exists(file):
            return FileNotFoundError(f'The file {file} does not exist!')
        file_objects = []
        with open(file, 'r') as f_read:
            content1 = f_read.readline()
            content2 = f_read.readline()
            content3 = f_read.readline()
            content4 = f_read.readline()

        ind = content1.rfind('        ')
        obj = content1[7:ind]

        obj1 = content4[13:32]

        file_objects.append(cls(obj.strip()))
        file_objects.append(cls(obj1.strip()))

        return file_objects


if __name__ == "__main__":
    file_objects = ReadNetworkElement.from_file('network_element_data.txt')
    for obj in file_objects:
        print(f'{obj.network_elem_name}')

    # object = ReadNetworkElement('network_element_data.txt')
    # print(object.get_column_name('Column_3'))
