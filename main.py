import os
from pprint import pprint

import numpy as np
import matplotlib.pyplot as plt

from srim import TRIM, SR, Ion, Layer, Target
from srim.output import Results

# Construct a 3MeV Nickel ion
ion = Ion('He', energy=4.87e6)

# Construct a layer of nick 20um thick with a displacement energy of 30 eV
Al = Layer({
        'Al': {
            'stoich': 1.0
        }
}, density=8.9, width=5100000.0)

Textolit_1 = Layer({
        'N': {
            'stoich': 0.01
            },
        'H': {
            'stoich': 0.0036
        },
        'O': {
            'stoich': 0.9114
        },
        'Si': {
            'stoich': 0.035
        },
        'O': {
            'stoich': 0.04
        }
}, density=8.9, width=7000000.0)

Cu = Layer({
        'Cu': {
            'stoich': 1.0
            }
}, density=8.9, width=350000.0)
           
Textolit_2 = Layer({
        'N': {
            'stoich': 0.01
            },
        'H': {
            'stoich': 0.0036
        },
        'O': {
            'stoich': 0.9114
        },
        'Si': {
            'stoich': 0.035
        },
        'O': {
            'stoich': 0.04
        }
}, density=8.9, width=7000000.0)

Si = Layer({
        'Si': {
            'stoich': 1.0,
            }
}, density=2.5, width=15000.0)

Glass = Layer({
            'Si': {
                'stoich': 1.0,
                }
}, density=2.5, width=5000000.0)

target = Target([Glass, Si])

# Initialize a TRIM calculation with given target and ion for 25 ions, quick calculation
trim = TRIM(target, ion, number_ions=20000, calculation=1)

# Specify the directory of SRIM.exe
# For windows users the path will include C://...
# The directory must have SRIM 2013 installed. TRIM.exe should be in this folder
srim_executable_directory = './tmp/srim' 

# takes about 10 seconds on my laptop
results = trim.run(srim_executable_directory)
# If all went successfull you should have seen a TRIM window popup and run 25 ions!

 # equivalent to results variable gotten from `trim.run`
srim_executable_directory = './tmp/srim' 
results = Results(srim_executable_directory)
print('Number of Ions: {}'.format(results.ioniz.num_ions))
results.__dict__
output_directory = './tmp/srim_outputs'
os.makedirs(output_directory, exist_ok=True)
print('Before:', os.listdir(output_directory))
TRIM.copy_output_files('./tmp/srim', output_directory)
print('After:', os.listdir(output_directory))
