[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# Python-Refresher with Best Practices
## How to Install
Download the repository from Github using ssh
```
git clone git@github.com:cu-swe4s-fall-2023/assignment-2-python-refresher-TylerAmos5.git
```
Navigate to the src folder
```
cd <path>/assignment-2-python-refresher-TylerAmos5/src
```
## How to run print_fires.py
Modify run.sh to set the parameters to query the csv appropriate for your interest
The --operation parameter is optional. Specify the statistic you would like to calculate.
If no --operation parameter is given, a list of integers will be returned.
```
python3 print_fires.py --file_name=<file_name>.csv \
                       --query_column=<column_index> \
                       --query_value="Specific value to match in query column" \
                       --result_column=<column_index>
                       --operation=[mean,median,stdv]
```
## Example
```
python3 print_fires.py --file_name=Agrofood_co2_emission.csv \
                       --query_column=0 --query_value="United States of America" \
                       --result_column=3 --operation=stdv
```
## Testing Instructions
Run the functional tests from the /test/func folder with:
```
bash test_print_fires.sh
```
Run the unit tests from /test/unit_test folder with:
```
python -m unittest test_utils.py
```

## my_utils.py
**Contains the function get_column, which can returns corresponding values from a queried column and value of interest.**
## print_fires.py
**Reads in command line arguments and runs the main function to report data from the csv file provided**
## run.sh
**Contains 3 test cases to show the functionality of print_fires.**
1. Runs correctly, reporting forrest fires for the United States of America.
2. Produces a FileNotFound exception since the csv file is spelled incorrectly
3. Produces an Exception since values that aren't numbers can't by typecasted to floats or ints.




## Notes from development
### HW2 (9/13): 
Completed get_columns function to return specified values that correspond to queried column and value.
Updated print_fires.py to use get_column correctly from my_utils.
Ensured my_utils.py only runs if main and that all python code satisfies pycodestyle. 
Changed results_column param in get_column to be a named parameter that defaults to 1. 
Created run.sh to execute print_fires.py.

### HW3 (9/26):
Added try except blocks to get_columns function to handle file and type casting errors
print_fires now takes named command line arguments using argparse.
Test cases were added to run.sh.

### HW4 (10/4):
Added statistical calculations to my_utils.
Mean, median, and standard deviation can be calculated for the result column
Added unit and functional tests
print_fires now takes an optional operation parameter that can calculate statistics about the result column. 