"""Program care primeste ca input un tip de fisier si are ca output alt tip de fisier"""
import pandas as pd

def text_to_csv(file_name: str):
    """Function that convert a txt in a csv file"""
    with open(file_name, 'r') as fr:
        content = fr.read().split()
        content_series = pd.Series(content)
    ind_pct = file_name.rfind('.')
    return content_series.to_csv(file_name[0:ind_pct] + '.csv')


def csv_to_excel(file_name: str):
    """Function that convert a csv file in a excel file"""
    content_csv = pd.read_csv(file_name)
    ind_pct = file_name.rfind('.')
    return content_csv.to_excel(file_name[0:ind_pct] + '.xlsx', index=None, header=True)

def text_to_excel(file_name: str):
    """Function that convert a text file in a excel file"""
    with open(file_name, 'r') as fr:
        content = fr.read().split()
        contentSeries = pd.Series(content)
    ind_pct = file_name.rfind('.')
    return contentSeries.to_excel(file_name[0:ind_pct] + '1.xlsx')

def csv_to_text(file_name: str):
    content_csv = pd.read_csv(file_name)
    ind_pct = file_name.rfind('.')
    return content_csv.to_csv(file_name[0:ind_pct] + '1.txt', index=None, sep=',')


def excel_to_text(file_name: str):
    content_excel = pd.read_excel(file_name)
    ind_pct = file_name.rfind('.')
    return content_excel.to_csv(file_name[0:ind_pct] + '-newtxt.txt', index=None, sep='\t')

def excel_to_csv(file_name: str):
    content_excel = pd.read_excel(file_name)
    ind_pct = file_name.rfind('.')
    return content_excel.to_csv(file_name[0:ind_pct] + '-newcsv.csv', index=None, sep='\t')


if __name__ == '__main__':
    file = 'nume.txt'
    print(text_to_csv(file))
    print(csv_to_excel('nume.csv'))
    print(text_to_excel(file))
    print(csv_to_text('nume.csv'))
    print(excel_to_text('nume.xlsx'))
    print(excel_to_csv('nume.xlsx'))