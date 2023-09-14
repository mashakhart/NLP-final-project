import subprocess
import os
import numpy as np

vals = np.arange(0.0, 1.1, 0.1)
weights_list = []
for v in vals:
    weights_list += [v]*3

idx = int(os.environ["SLURM_ARRAY_TASK_ID"])

subprocess.run(f'python main.py validate --config cli_task2_stepwise_t5-large.yaml \
    --ckpt_path /scratch/gpfs/eonal/nlproofs/NLProofS/data/ebank_task2_prover.ckpt \
    --model.verifier_weight {weights_list[idx]} --model.verifier_ckpt /scratch/gpfs/eonal/nlproofs/NLProofS/data/ebank_task2_verifier.ckpt \
    --model.proof_search true --model.aggregation_method min_sp', shell=True)
