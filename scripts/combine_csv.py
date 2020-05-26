import pandas as pd
import os
import glob
import io 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()


#path_lh ='/home/dimuthu1/scratch/project2/derivatives/hcp_360/work/MyWorkflow/_sub_id_*/parce/out_put/*/tables/table_lh.txt'

#path_rh ='/home/dimuthu1/scratch/project2/derivatives/hcp_360/work/MyWorkflow/_sub_id_*/parce/out_put/*/tables/table_rh.txt'

hcp_lh = '../../derivatives/analysis/hcp_stat/sub-CT01/CT01_hcp_stat_lh.csv'
gradient = '../../derivatives/analysis/gradients/sub-CT01/gradients.csv'




grads = pd.read_csv(gradient)
stats_lh = pd.read_csv(hcp_lh) 

stats_lh = stats_lh.drop(['Num_of_vertices','thickness_mm', 'ROI_name'], axis = 1) 

gradient_lh = grads[['L_grad_1','L_grad_2','L_grad_3','L_grad_4']]

#print(stats_lh['thickness_mm'])

"""splitted_vals = [i.split(' ') for i in stats_lh['thickness_mm'].values]
thickness = np.array(splitted_vals)[:,0]
error = np.array(splitted_vals)[:,1]

#Note: Not using error column atm. Will add the error bars later.

thick_df = pd.DataFrame({'thickness': thickness})

stats_lh['thickness_mm'] = thick_df['thickness']   #.astype(float)

header = list(stats_lh)"""

#for cols in header:

#	stats_lh['thickness_mm'] = thick_df['thickness'].astype(float)


gradient_lh = gradient_lh.drop([0]).reset_index(drop=True)


combined_lh = pd.concat([stats_lh, gradient_lh], axis=1, sort=False)



sns_plot = sns.pairplot(combined_lh)
plt.show()
sns_plot.savefig("all_CT.png")

#sns_plot_1 = sns.jointplot("L_grad_2", "thickness", data=combined_lh, kind="reg", truncate=False)
#plt.show()
#sns_plot_1.savefig("thick_vs_g2_PD.png")

#plt.show()

def make_out_dir(out_path):

	#Make subdirectories to save files
	filename = out_path
	if not os.path.exists(os.path.dirname(filename)):
	    try:
	        os.makedirs(os.path.dirname(filename))
	    except OSError as exc: # Guard against race condition
	        if exc.errno != errno.EEXIST:
	          raise

#make_out_dir(snakemake.params.stat_out_path)












