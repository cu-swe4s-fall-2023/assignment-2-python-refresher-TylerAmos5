test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_get_column_australia_fires_mean python ../../src/print_fires.py --file_name=functional_test_data.csv \
                       --query_column=0 --query_value="Australia" \
                       --result_column=3 \
                       --operation=mean
assert_in_stdout 4364.741935483871
assert_exit_code 0

run test_get_column_china_fires_mean python ../../src/print_fires.py --file_name=functional_test_data.csv \
                       --query_column=0 --query_value="China" \
                       --result_column=3 \
                       --operation=mean
assert_in_stdout 850.0322580645161
assert_exit_code 0

run test_get_column_australia_fires_mean python ../../src/print_fires.py --file_name=functional_test_data.csv \
                       --query_column=0 --query_value="Australia" \
                       --result_column=3 \
                       --operation=mean
assert_in_stdout 4364.741935483871
assert_exit_code 0

run test_get_column_china_fires_mean python ../../src/print_fires.py --file_name=functional_test_data.csv \
                       --query_column=0 --query_value="China" \
                       --result_column=3 \
                       --operation=mean
assert_in_stdout 850.0322580645161
assert_exit_code 0

run test_get_column_australia_fires_median python ../../src/print_fires.py --file_name=functional_test_data.csv \
                       --query_column=0 --query_value="Australia" \
                       --result_column=3 \
                       --operation=median
assert_in_stdout 3480
assert_exit_code 0

run test_get_column_china_fires_mean python ../../src/print_fires.py --file_name=functional_test_data.csv \
                       --query_column=0 --query_value="China" \
                       --result_column=3 \
                       --operation=median
assert_in_stdout 760
assert_exit_code 0

run test_get_column_australia_fires_stdv python ../../src/print_fires.py --file_name=functional_test_data.csv \
                       --query_column=0 --query_value="Australia" \
                       --result_column=3 \
                       --operation=stdv
assert_in_stdout 4099.9081287897325
assert_exit_code 0

run test_get_column_china_fires_stdv python ../../src/print_fires.py --file_name=functional_test_data.csv \
                       --query_column=0 --query_value="China" \
                       --result_column=3 \
                       --operation=stdv
assert_in_stdout 416.74144533279207
assert_exit_code 0