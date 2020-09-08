import csv as csv
import numpy as np


def ReadFile(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
        print(f'Processed {line_count} lines.')


def GenerateFileNames(n, file_id):
    names = []
    for id in range(n):
        name = '../../Reports/LambdaOutput/'+file_id+'-'+str(id+1)+'.csv'
        names.append(name)
    return names


filenames = GenerateFileNames(10, 'Lambda-idx')

for file_id in filenames:
    ReadFile(file_id)
