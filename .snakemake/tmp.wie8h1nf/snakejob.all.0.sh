#!/bin/sh
# properties = {"type": "single", "rule": "all", "local": true, "input": ["../derivatives/analysis/gradients/sub-CT01/gradient_image.nii.gz"], "output": [], "wildcards": {}, "params": {}, "log": [], "threads": 1, "resources": {"mem_mb": 4000}, "jobid": 0, "cluster": {}}
 cd /scratch/dimuthu1/project2/Project_2 && \
/home/dimuthu1/py3/bin/python \
-m snakemake all --snakefile /scratch/dimuthu1/project2/Project_2/Snakefile \
--force -j --keep-target-files --keep-remote \
--wait-for-files /scratch/dimuthu1/project2/Project_2/.snakemake/tmp.wie8h1nf ../derivatives/analysis/gradients/sub-CT01/gradient_image.nii.gz --latency-wait 5 \
 --attempt 1 --force-use-threads \
--wrapper-prefix https://github.com/snakemake/snakemake-wrappers/raw/ \
   --allowed-rules all --nocolor --notemp --no-hooks --nolock \
--mode 2  --use-singularity  --singularity-args "\-e" --use-envmodules --default-resources "mem_mb=4000"  && touch /scratch/dimuthu1/project2/Project_2/.snakemake/tmp.wie8h1nf/0.jobfinished || (touch /scratch/dimuthu1/project2/Project_2/.snakemake/tmp.wie8h1nf/0.jobfailed; exit 1)

