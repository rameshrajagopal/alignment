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

               Command Line Alignment Application
               ----------------------------------
This is simple command line application which sets up arbitory solar system
based on the provided configuration files. It also allows to run the plugin 
during runtime to decide the alignment of planets based on the decision made 
by plugins.

Design Decisions: 

1) Arbitory Solar System is setup based on the given system config file. It
also exposes APIs for dynamically adding planet and removing planet from the 
solar system. Hence in order to add/search/remove quickly, the planet
information has been kept under dictionary. 

2) Current Arbitory Solar System planet's doesn't orbit the sun. It just gives 
information from the initial position where it will be after the 'time' ticks. 
This can be extended by having start() method to orbit the sun. 

3) It is assumed that the period and 'time' ticks comes from the command line, has been
considered having some units of measurement. This assumption makes the
calculation easy without need to conversion.

4) InputParser class has been created to handle multiple file formats. Current
one just supports yaml parser, since we are dealing with only yaml files as of
now. This class can be extended to parse different file format as well. 

5) It is assumed the plugin's file will make all the decision about whether
two planets are aligned with respect to the sun. Only desired property from
the plugin that it has to expose, print_alignment() function which prints the
alignment of planets at the point. It is with respect to plugin to decide and
print the alignment of the planets based on the input provided by alignment
application. This gives the flexiblity for the plugin developer to change
their decision as an when required.  

6) Module "pyyaml" is used for parsing *.yaml file

7) Module "argparse" is used for command line parsing.




