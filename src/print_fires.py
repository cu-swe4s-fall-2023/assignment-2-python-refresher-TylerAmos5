import my_utils
import argparse


def get_args():
    """Collect arguments to query a .csv file"

    Returns
    -------
    args
        arguments input by the user
    """
    parser = argparse.ArgumentParser(description='Query a column '
                                     'of a csv and return desired result',
                                     prog='print_fires')
    parser.add_argument('--file_name',
                        type=str,
                        help='.csv File',
                        required=True)

    parser.add_argument('--query_column',
                        type=int,
                        help='Column index containing countries',
                        required=True)

    parser.add_argument('--query_value',
                        help='Value to match in the query column',
                        required=True)

    parser.add_argument('--result_column',
                        type=int,
                        help='Index of column containing deisred result',
                        required=True)
    
    parser.add_argument('--operation',
                        type=str,
                        help='Choose to perform the mean, median, ' 
                        'or standard deviation (stdv) on the result column')
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    result = []
    result = my_utils.get_column(args.file_name, args.query_column,
                        args.query_value,
                        result_column=args.result_column)
        
    if result is None:
        pass
    else:
        if args.operation == 'mean':
            calc = my_utils.mean(result)
            print(calc)
        elif args.operation == 'median':
            calc = my_utils.median(result)
            print(calc)
        elif args.operation == 'stdv':
            calc = my_utils.stdv(result)
            print(calc)
        else:
            print(result)


if __name__ == '__main__':
    main()
