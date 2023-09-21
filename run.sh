#!/bin/bash

set -e
set -u

echo ..Running print_fires.py with good inputs..
python3 print_fires.py --file_name=Agrofood_co2_emission.csv \
                       --query_column=0 --query_value="United States of America" \
                       --result_column=3
echo Done!

echo ..Running print_fires.py with bad file name..
python3 print_fires.py --file_name=Agrofood_co2_emission \
                       --query_column=0 --query_value="United States of America" \
                       --result_column=3
echo Done!

echo ..Running print_fires.py with a typecasting error..
python3 print_fires.py --file_name=Agrofood_co2_emission \
                       --query_column=0 --query_value="United States of America" \
                       --result_column=0
echo Done!