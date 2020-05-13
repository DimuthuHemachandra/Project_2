#from brainspace.datasets import load_conte69
#from brainspace.plotting import plot_hemispheres
#from brainspace.datasets import load_group_fc, load_parcellation
import matplotlib.pyplot as plt
#from brainspace.gradient import GradientMaps
import numpy as np
#from brainspace.utils.parcellation import map_to_labels
import scipy.io as sio
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from nilearn.image import load_img
import nibabel as nib
import os
import glob

from mapalign.embed import DiffusionMapEmbedding

from scipy.io import loadmat

subject = 'CT01'


def get_df(mat_path):
	#Reads a .mat file obtained from diffparc and conver it to a panda df
	#mat_path = path to the .mat file

	file_mat = loadmat(mat_path)
	conn = file_mat['connmap_feats'] #Extracting the table named connmap_feat from the .mat file
	df = pd.DataFrame(conn.T)  #Transposing and converting to a df

	return df


def split_df(df,headsize):
	#Splits a df into two parts. This is to seperate left and right from the df.

	left = df.head(headsize)
	right = df.tail(len(df)-headsize)

	return left, right


def get_gradients(matrix, gradient_n):
	#Calculating the diffusion gradients
	#matrix: nxm matrix
	#gradient_n: gradient componanat (int 1 to n). I have set n = 5 here.

	sim_matrix = cosine_similarity(matrix)  #Calculating the cosine similarity matrix

	#plt.imshow(sim_matrix)
	#plt.show()

	de = DiffusionMapEmbedding(alpha=0.5, diffusion_time=10, affinity='markov', n_components=5).fit_transform(sim_matrix.copy())

	grad=de[:,gradient_n-1] #-1 to fix for the index

	return grad


def get_diffusion_maps(path_to_mat_R,path_to_mat_L, componanat):
	#Calculate the diffusion gradients for LEft and Right sides.
	#subject: string of the subject ID
	#componanat: int (1-5). Can change the upper limit (5) by editing get_gradinets().

	Right_matrix = glob.glob(path_to_mat_R) #finding all the mat files
	Left_matrix = glob.glob(path_to_mat_L)
	#Left_matrix = glob.glob("../data/matrices/Left/"+'*'+subject+'*'+'.mat') #finding all the mat files

	R_matrix = get_df(Right_matrix[0])
	L_matrix= get_df(Left_matrix[0])

	left,true_right = split_df(R_matrix, 180)
	true_left,right = split_df(L_matrix, 180)

	#plt.imshow(true_right*1000,aspect="auto")
	#plt.show()

	R_gradient = get_gradients(true_right, componanat)
	L_gradient = get_gradients(true_left, componanat)

	print("Right gradient is processed for shape:",np.shape(R_gradient))
	#print("Left gradient is processed for "+subject+" with shape:",np.shape(L_gradient))

	grad_df = pd.DataFrame({'R_gradient': R_gradient, 'L_gradient': L_gradient})

	return grad_df



grad_df = get_diffusion_maps(snakemake.input.Right,snakemake.input.Left,1)

grad_df.to_csv(snakemake.output.gradient, index=False)

#np.savetxt(snakemake.output.gradient,R_gradient)





"""
def get_projections():

  img = load_img("HCP-MMP1.nii.gz")
  data = (img.get_data())
  x = np.shape(data)[0]
  y = np.shape(data)[1]
  z = np.shape(data)[2]
  R_rois = np.loadtxt("R_coords.txt")
  L_rois = np.loadtxt("L_coords.txt")
  #rois = coords.values
  R_vals = np.column_stack((R_gradient, R_rois))
  L_vals = np.column_stack((L_gradient, L_rois))


  new_img = data
  for i in range(x):
     for j in range (y):
             for k in range (z):
                 if data[i,j,k] in R_vals[:,1].tolist():
                     index = np.where(R_vals[:,1] == data[i,j,k])[0][0]
                     #print(val.index(data[i,j,k]))
                     new_img[i,j,k]=R_vals[index,0]*1000

                 elif data[i,j,k] in L_vals[:,1].tolist():
                     index = np.where(L_vals[:,1] == data[i,j,k])[0][0]
                     #print(val.index(data[i,j,k]))
                     new_img[i,j,k]=L_vals[index,0]*1000
                 else:
                     new_img[i,j,k]=3000

  final_img = nib.Nifti1Image(new_img, img.affine, img.header)
  nib.save(final_img,"final_image.nii")


get_projections()"""






