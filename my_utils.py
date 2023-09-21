import sys


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
                    return None
            return result_values
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occured")
