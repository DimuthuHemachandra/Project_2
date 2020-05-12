from brainspace.datasets import load_conte69
from brainspace.plotting import plot_hemispheres
from brainspace.datasets import load_group_fc, load_parcellation
import matplotlib.pyplot as plt
from brainspace.gradient import GradientMaps
import numpy as np
from brainspace.utils.parcellation import map_to_labels
import scipy.io as sio
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from nilearn.image import load_img
from nilearn import plotting
import nibabel as nib
import os
import glob

from mapalign.embed import DiffusionMapEmbedding

from scipy.io import loadmat

subject = 'CT01'


def get_projections(grad_file):


	grads = pd.read_csv(grad_file) 

	R_gradient = grads['R_gradient']
	L_gradient = grads['L_gradient']



	img = load_img("../Data/T1s/HCPNATIVE/HCP-MMP1.nii.gz")
	data = (img.get_data())
	x = np.shape(data)[0]
	y = np.shape(data)[1]
	z = np.shape(data)[2]
	R_rois = np.loadtxt("R_coords.txt")
	L_rois = np.loadtxt("L_coords.txt")
	#rois = coords.values
	R_vals = np.column_stack((R_gradient, R_rois))
	L_vals = np.column_stack((L_gradient, L_rois))

	#np.place(data, data==1, 1)

	subcortical_ROIs = np.linspace(0,255,256)

	for i,val in enumerate(R_rois):
		np.place(data, data==val, (R_gradient[i]*1000) +1000)

	for i,val in enumerate(L_rois):
		np.place(data, data==val, (L_gradient[i]*1000)+1000)

	for i,val in enumerate(subcortical_ROIs):
		np.place(data, data==val, 600)

	final_img = nib.Nifti1Image(data, img.affine, img.header)
	nifty_name = "final_image.nii.gz"
	nib.save(final_img,snakemake.output.projected_image)
	

	display = plotting.plot_img(snakemake.output.projected_image,
	                   cut_coords=(14, 10, 0),
	                   threshold = 601,
	                   title="Diffusion Gradient",cmap='gist_rainbow', colorbar = True)

	display.savefig(snakemake.output.projected_plot) 



	#plotting.show()






#get_projections(snakemake.input[0])

get_projections(snakemake.input[0])






