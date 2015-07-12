A small commandline application which sets up arbitory solar system based on
the config file provided. It also prints the alignment of the planets based on
plugins provided.

Installing the application:
--------------------------

a) tar xjvf alignment-0.1.tar.gz
b) cd alignment
c) python setup.py install

How to run the application:
--------------------------

python alignment.py --config <sample_config_file> --plugins <plugin1> <plugin2> <plugin3> --time 10
e.g:
python alignment.py --config plugins/sample.yaml --plugins plugins/five_degree_alignment.py --time 10
