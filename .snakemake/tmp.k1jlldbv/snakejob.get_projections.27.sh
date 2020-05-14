#!/bin/sh
# properties = {"type": "single", "rule": "get_projections", "local": false, "input": ["../derivatives/analysis/gradients/sub-PD19/gradients.csv", "/home/dimuthu1/scratch/project2/derivatives/diffparc_dev/work/sub-PD19/labels/t1/HCPNATIVE/HCP-MMP1.nii.gz"], "output": ["../derivatives/analysis/gradients/sub-PD19/gradient_image.nii.gz", "../derivatives/analysis/gradients/sub-PD19/gradient_image_plot.png"], "wildcards": {"subject": "PD19"}, "params": {}, "log": [], "threads": 1, "resources": {"mem_mb": 4000}, "jobid": 27, "cluster": {}}
 cd /scratch/dimuthu1/project2/Project_2 && \
/home/dimuthu1/py3/bin/python \
-m snakemake ../derivatives/analysis/gradients/sub-PD19/gradient_image.nii.gz --snakefile /scratch/dimuthu1/project2/Project_2/Snakefile \
--force -j --keep-target-files --keep-remote \
--wait-for-files /scratch/dimuthu1/project2/Project_2/.snakemake/tmp.k1jlldbv ../derivatives/analysis/gradients/sub-PD19/gradients.csv /home/dimuthu1/scratch/project2/derivatives/diffparc_dev/work/sub-PD19/labels/t1/HCPNATIVE/HCP-MMP1.nii.gz --latency-wait 5 \
 --attempt 1 --force-use-threads \
--wrapper-prefix https://github.com/snakemake/snakemake-wrappers/raw/ \
   --allowed-rules get_projections --nocolor --notemp --no-hooks --nolock \
--mode 2  --use-singularity  --singularity-args "\-e" --use-envmodules --default-resources "mem_mb=4000"  && touch /scratch/dimuthu1/project2/Project_2/.snakemake/tmp.k1jlldbv/27.jobfinished || (touch /scratch/dimuthu1/project2/Project_2/.snakemake/tmp.k1jlldbv/27.jobfailed; exit 1)

