from classdefinitions import Subject, Stimuli
from bodyfunctions import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Gather subjects into one dict
dataloc = '/Users/juusu53/Documents/projects/biofeedback/data/processed/'
maskloc = '/Users/juusu53/Documents/projects/biofeedback/code/minimal_bodyspm/masks/'
subnums = ['15742','218646','951417'] # you can just as easily read in subject names from a file

# combine data
#full_dataset = combine_data(dataloc, subnums)

# sanity check visualisation on the full data set
mask_one = read_in_mask(maskloc + 'mask_front_new.png')
stim = Stimuli(fileloc=dataloc, from_file=True)
datafile = get_latest_datafile(dataloc)
#
# # TODO: make easy sanity check figures, maybe as a function?
fig, axes = plt.subplots(figsize=(24, 10), ncols=len(stim.all.keys())+1, nrows=1)

cmap = plt.get_cmap('RdBu_r')
vmin = -1
vmax = 1
for i, cond in enumerate(stim.all.keys()):
    print('reading in ' + cond)
    with h5py.File(datafile, 'r') as h:
        data = h[cond].value
        all_n = np.count_nonzero(~np.isnan(data[:,1,1]))
        all_figs = np.nanmean(binarize(data.copy()), axis=0)
        masked_data = np.ma.masked_where(mask_one != 1,all_figs)
    im = axes[i].imshow(masked_data, cmap = cmap, vmin=vmin, vmax=vmax)
    axes[i].set_xticklabels([])
    axes[i].set_yticklabels([])
    axes[i].set_axis_off()
    axes[i].set_title(stim.all[cond]['show_name'],fontsize=30)

#im=axes[i+1].imshow(np.zeros((masked_data.shape[1],1)), cmap=cmap, vmin=vmin, vmax=vmax)
axes[i+1].set_xticklabels([])
axes[i+1].set_yticklabels([])
axes[i+1].set_axis_off()
divider = make_axes_locatable(axes[i+1])
cax = divider.append_axes('right', size='50%', pad=0.15)

fig.colorbar(im, cax=cax, shrink=0.1)

plt.show()



