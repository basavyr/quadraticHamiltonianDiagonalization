import csv as csv
import numpy as np

# used [this](https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3) tutorial for working with external modules as GridPlot and the EigenValues

# import BosonEigenvalues as bos
import GridPlot as grid


def GenerateFileNames(n, file_id):
    names = []
    for id in range(n):
        name = '../../Reports/LambdaOutput/'+file_id+'-'+str(id+1)+'.csv'
        names.append(name)
    return names


filenames = GenerateFileNames(10, 'Lambda-idx')


def ReadFile(filenames, n):
    qvalues = []
    # store the even values for lambda
    lambdas = []
    # store the odd values for lambda
    odd_lambdas = []

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
        lambda_local = []
        odd_lambda_local = []
        with open(filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                lambda_local.append(round(float(row[1]), 3))
                odd_lambda_local.append(round(float(row[2]), 3))
                # lamda_local.append(qvalues[count])
        lambdas.append(lambda_local)
        odd_lambdas.append(odd_lambda_local)
        count = count+1

    # # solutions container before trimming
    # print(f'Before trimming: \n {lambdas}\n')

    # # solutions container after trimming
    # print(f'After trimming: \n {lambdas[:n]}\n')

    # data trimming
    lambdas = lambdas[:n]

    odd_lambdas = odd_lambdas[:n]

    # print(len(lambdas), len(odd_lambdas))
    # generate the container for storing each solution of the Boson Hamiltonian
    data = [qvalues, lambdas, odd_lambdas]

    # create a data sampling, storing less values in a reduced size container
    sampled_data = []
    size = len(qvalues)
    cutting_factor = 4
    sampled_q = qvalues[::cutting_factor]
    sampled_lambdas = []
    sampled_odd_lambdas = []
    for id_x in range(len(lambdas)):
        sampled_lambdas.append(lambdas[id_x][::cutting_factor])
        sampled_odd_lambdas.append(odd_lambdas[id_x][::cutting_factor])

        # return [len(sampled_q), len(sampled_lambdas[0])]

    sampled_data = [sampled_q, sampled_lambdas, sampled_odd_lambdas]
    return sampled_data


plot_grid_size = 1
data_to_grid = ReadFile(filenames, plot_grid_size*plot_grid_size)

# print(data_to_grid)

grid.CreateGridPlot(plot_grid_size, data_to_grid)
