import csv as csv
import numpy as np

# used [this](https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3) tutorial for working with external modules as GridPlot and the EigenValues

# import BosonEigenvalues as bos
# import GridPlot as grid


def GenerateFileNames(n, file_id):
    names = []
    for id in range(n):
        name = '../../Reports/LambdaOutput/'+file_id+'-'+str(id+1)+'.csv'
        names.append(name)
    return names


filenames = GenerateFileNames(10, 'Lambda-idx')


def ReadFile(filenames, n):
    qvalues = []
    lambdas = []

    # first create q-array
    # this can be done in a single loop, since the values of the q-parameter are the same across each file.
    with open(filenames[0]) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            qvalues.append(round(float(row[0]), 3))

    # create the lambda-array
    # array of arrays, where each sub-array contains all the values of lambda_id, evaluated at certain q
    count = 0
    for filename in filenames:
        lamda_local = []
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                lamda_local.append(float(row[1]))
                # lamda_local.append(qvalues[count])
        lambdas.append(lamda_local)
        count = count+1
    # print(lambdas)

    # data = [qvalues, lambdas]
    print(f'Only {n} arrays will be stored in the container...')
    return lambdas


n_grid = 3
ReadFile(filenames, n_grid*n_grid)


# grid.CreateGridPlot(2,)
