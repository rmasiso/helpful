from mayavi import mlab
from surfer import Brain, project_volume_data
import scipy
import matplotlib.pyplot as plt
import nibabel as nib
import numpy as np
import sys
import deepdish as dd
import os
from os.path import expanduser

#
# run with 'python pysurfer_mni.py' in terminal // some people use pythonw 
#

subject_id = "fsaverage"
hemi = 'split' #"lh"
surf = "inflated"

"""
Bring up the visualization.
"""
#you can use your BIDS --> fmriprep output --> freesurfer directory
#os.environ['SUBJECTS_DIR'] = expanduser('/Volumes/rmasis/MemPal/data/BIDS/derivatives/freesurfer/')

os.environ['FREESURFER_HOME'] = expanduser('/Applications/freesurfer/')

# #reg_file = os.environ['FREESURFER_HOME']

os.environ['SUBJECTS_DIR'] = expanduser('/Applications/freesurfer/subjects')


#mri_file = '/Volumes/norman/rmasis/MemPal/analysis/PythonData/' + 'testMNIpathvideoNii.nii.gz'
mri_file =  '/Volumes/norman/rmasis/MemPal/analysis/PythonData/troubleshoot/' + 'PV1_isc' + '.nii.gz'

reg_file = '/Applications/freesurfer/average/mni152.register.dat'

data = nib.load(mri_file)

brain = Brain(subject_id, hemi, surf, background="white")

minval = 0.0 #np.min(data.get_data())
maxval = np.max(data.get_data()) 

surf_data_lh = project_volume_data(mri_file,"lh", reg_file) #uses freesurfers mri_vol2surf
surf_data_rh = project_volume_data(mri_file,"rh", reg_file)

brain.add_overlay(surf_data_lh,min=minval,max=maxval,name="thirty_sec_lh", hemi='lh',sign="pos")
brain.add_overlay(surf_data_rh,min=minval,max=maxval,name="thirty_sec_rh", hemi='rh',sign="pos")

mlab.show()


