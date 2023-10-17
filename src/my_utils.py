import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



def get_column(file_name, query_column, query_value, result_column=1):
    """Return the values of interest from a csv that correspond to the queried
    columns and values.

    Parameters
    ---------
    file_name : name of file to read
        csv file
    query_column : index of column to query
        Non-negative integer
    query_value : specific value of interest to find corresponding results
        Any data type. However typically a string
    result_column : index of desired result to find
        Non-negative integer

    Returns
    ------
    result_values
        Values from desired column that correspond to query column and value

    """
    result_values = []
    try:
        with open(file_name, 'r') as f:
            next(f)  # skip header
            for line in f:
                A = line.rstrip().split(',')
                try:
                    if A[query_column] == query_value:
                        result_values.append(int(float((A[result_column]))))
                except ValueError:
                    print("Error type-casting to integer")
                    sys.exit(1)
                except IndexError:
                    print("Column index is out of range")
                    sys.exit(1)
            return result_values
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
    except Exception as e:
        print("An error occured")
        sys.exit(1)

def get_data_columns(file_name):
    with open(file_name, 'r') as f:
        columns = f.readline()
        columns = columns.rstrip().split(',')
        return columns


def mean(data):
    """Return the mean of a list of integers

    Parameters
    ----------
    data : list of integers

    Returns
    ----------
    mean of dataset
    """
    if not (all(isinstance(i, int) for i in data)):
        raise ValueError("Data are not all integers")
        sys.exit(1)

    if len(data) == 0:
        raise ValueError("Expected a non-empty list")
        sys.exit(1)
    return sum(data)/len(data)


def median(data):
    """Returns the median of a list of integers

    Parameters
    ----------
    data : list of integers

    Returns
    ----------
    median of the dataset
    """
    if not (all(isinstance(i, int) for i in data)):
        raise ValueError("Data are not all integers")
        sys.exit(1)

    if len(data) == 0:
        raise ValueError("Expected a non-empty list")
        sys.exit(1)

    data.sort()
    num_elem = len(data)
    if num_elem % 2 == 0:
        # floor division prevents float indexes to access the middle elements
        return (data[num_elem // 2 - 1] + data[num_elem // 2]) / 2
    else:
        return data[num_elem // 2]


def stdv(data):
    """Returns the standard deviation of a list of integers

    Parameters
    ----------
    data : A list of integers

    Returns
    ----------
    standard deviation of the dataset
    """
    if not (all(isinstance(i, int) for i in data)):
        raise ValueError("Data are not all integers")
        sys.exit(1)

    if len(data) == 0:
        raise ValueError("Expected a non-empty list")
        sys.exit(1)

    num_elem = len(data)
    avg = mean(data)
    # sum of squared differences from the mean using in-line for loop
    squared_d = sum((x - avg) ** 2 for x in data)
    variance = squared_d / (num_elem - 1)
    return variance ** 0.5


def plot_boxplot(data, x_axis="x-axis", title='Title'):
    if not data:
        raise ValueError("Expected a non-empty list")
        sys.exit(1)

    fig, ax = plt.subplots()
    ax.boxplot(data)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel(x_axis)
    ax.set_ylabel('Freq.')
    ax.set_title(title)
    
    output_folder = '../output'
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
    except OSError:
        print("Error creating directory")
    
    file_name = '{}.png'.format(title)
    file_path = os.path.join(output_folder, file_name)
    try:
        plt.savefig(file_path, bbox_inches='tight')
    except OSError:
        print("Error saving file")
        return
