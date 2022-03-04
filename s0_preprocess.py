import os
import sys
import pandas as pd
from classdefinitions import Subject, Stimuli
from bodyfunctions import combine_data, preprocess_subjects, make_qc_figures
import matplotlib.pyplot as plt
import numpy as np

# set up stimuli description
data_names = ['0', '1', '2', '3', '4','5','6', '7','8','9','10','11','12']
# these need to be in the same order as in the words.txt file - feel free to double and triple check!
data_labels = ['neutral','radsla','ilska','avsky','sorg','gladje','forvaning','karlek',
               'skam','avund','skuld','intersse','impuls att skada']

# define the inputs
dataloc = '/Users/juusu53/Documents/projects/biofeedback/data/raw/'
outdataloc = '/Users/juusu53/Documents/projects/biofeedback/data/processed/'
subnums = ['15742','218646','951417'] # you can just as easily read in subject names as a list

# define stimulus set
stim = Stimuli(data_names, onesided=True, show_names=data_labels)

# read subjects from web output and write out to a more sensible format
preprocess_subjects(subnums, dataloc, outdataloc, stim)

# draw each subject's each map for visual quality control
make_qc_figures(subnums, dataloc, stim, outdataloc)
# if there are subjects whose QC does not pass muster,
# take the corresponding sub id numbers off the subs.txt file
# before moving on to s0_combine_preprocessed

