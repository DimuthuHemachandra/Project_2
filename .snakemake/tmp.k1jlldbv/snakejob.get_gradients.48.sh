#!/bin/sh
# properties = {"type": "single", "rule": "get_gradients", "local": false, "input": ["/home/dimuthu1/scratch/project2/derivatives/diffparc_dev/matrices/Right/sub-PD06_space-T1w_res-2_seed-CIT168_striatum-hcpmmp_connMap.mat", "/home/dimuthu1/scratch/project2/derivatives/diffparc_dev/matrices/Left/sub-PD06_space-T1w_res-2_seed-CIT168_striatum-hcpmmp_connMap.mat", "../derivatives/analysis/gradients/"], "output": ["../derivatives/analysis/gradients/sub-PD06/gradients.csv"], "wildcards": {"subject": "PD06"}, "params": {}, "log": [], "threads": 1, "resources": {"mem_mb": 4000}, "jobid": 48, "cluster": {}}
 cd /scratch/dimuthu1/project2/Project_2 && \
/home/dimuthu1/py3/bin/python \
-m snakemake ../derivatives/analysis/gradients/sub-PD06/gradients.csv --snakefile /scratch/dimuthu1/project2/Project_2/Snakefile \
--force -j --keep-target-files --keep-remote \
--wait-for-files /scratch/dimuthu1/project2/Project_2/.snakemake/tmp.k1jlldbv /home/dimuthu1/scratch/project2/derivatives/diffparc_dev/matrices/Right/sub-PD06_space-T1w_res-2_seed-CIT168_striatum-hcpmmp_connMap.mat /home/dimuthu1/scratch/project2/derivatives/diffparc_dev/matrices/Left/sub-PD06_space-T1w_res-2_seed-CIT168_striatum-hcpmmp_connMap.mat ../derivatives/analysis/gradients/ --latency-wait 5 \
 --attempt 1 --force-use-threads \
--wrapper-prefix https://github.com/snakemake/snakemake-wrappers/raw/ \
   --allowed-rules get_gradients --nocolor --notemp --no-hooks --nolock \
--mode 2  --use-singularity  --singularity-args "\-e" --use-envmodules --default-resources "mem_mb=4000"  && touch /scratch/dimuthu1/project2/Project_2/.snakemake/tmp.k1jlldbv/48.jobfinished || (touch /scratch/dimuthu1/project2/Project_2/.snakemake/tmp.k1jlldbv/48.jobfailed; exit 1)

