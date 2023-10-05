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

run test_get_column_aust_fires python ../../src/print_fires.py --file_name=functional_test_data.csv \
                       --query_column=0 --query_value="Australia" \
                       --result_column=3
assert_in_stdout [4240, 4240, 4240, 4240, 4240, 4240, 6379, 9571, 7442, 10069, 3480, 2236, 4315, 7573, 757, 711, 5823, 2102, 471, 3405, 542, 1083, 1675, 2839, 2192, 1358, 1768, 1119, 1815, 20157, 10985]
assert_exit_code 0

run test_get_column_column_DNE python ../../src/print_fires.py --file_name=functional_test_data.csv \
                       --query_column=100 --query_value="Australia" \
                       --result_column=3
assert_exit_code 1

run test_get_column_not_real_oper python ../../src/print_fires.py --file_name=functional_test_data.csv \
                       --query_column=0 --query_value="Australia" \
                       --result_column=3 --operation=subtract
assert_exit_code 1

run test_get_column_no_file python ../../src/print_fires.py --file_name=functional_test_data \
                       --query_column=0 --query_value="Australia" \
                       --result_column=3 --operation=subtract
assert_exit_code 1

run test_get_column_missing_arg python ../../src/print_fires.py --file_name=functional_test_data.csv \
                       --query_value="Australia" \
                       --result_column=3 --operation=subtract
assert_in_stderr print_fires

