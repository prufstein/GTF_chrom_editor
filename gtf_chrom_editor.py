#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:42:29 2024

@author: prufstein
"""


import pandas as pd

# Read the key table
assembly_report = pd.read_table('/path/to/assembley_report')

# Create a mapping from old_code to new_code
code_mapping = dict(zip(assembly_report['RefSeq-Accn'], assembly_report['Assigned-Molecule']))

# Function to replace chromosome numbers
def replace_chromosome(line, mapping):
    fields = line.split('\t')
    if fields[0] in mapping:
        fields[0] = mapping[fields[0]]
    return '\t'.join(fields)

# Read the GTF file, replace chromosome numbers, and write to a new file
with open('path/to/gtf/example.gtf', 'r') as infile, open('path/to/output/out.gtf', 'w') as outfile:
    for line in infile:
        if not line.startswith('#'):
            line = replace_chromosome(line, code_mapping)
        outfile.write(line)

print("Chromosome numbers have been updated and saved to 'out.gtf'.")
