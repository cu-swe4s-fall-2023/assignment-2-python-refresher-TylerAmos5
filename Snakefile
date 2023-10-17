def read_queries(file_name):
    queries = []
    with open(file_name) as f:
        for line in f:
            queries.append(line.rstrip())
    return queries

rule all:
    input:
        expand('output/{query}.png', query=read_queries('countries.txt'))

rule download_data:
    output:
        'Argrofood_co2_emission.csv'
    shell:
        'wget -O {output} "https://docs.google.com/uc?export=download&id=1Wytf3ryf9EtOwaloms8HEzLG0yjtRqxr"'

rule make_output_folder:
    input:
        'Argrofood_co2_emission.csv'
    shell:
        'mkdir output'

rule plot_data:
    output:
        'output/{x}.png'
    input:
        'Argrofood_co2_emission.csv'
    shell:
        'python src/print_fires.py --file_name={input} --query_column=0 ' \
        '--query_value="{wildcards.x}" --result_column=3 --toPlot=True'