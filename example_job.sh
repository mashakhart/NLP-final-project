#!/bin/bash
#SBATCH --job-name=d_n10.0b_2-d_p10.0b_2 # create a short name for your job
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem-per-cpu=10G         # memory per cpu-core (4G is default)
#SBATCH --time=12:00:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=all        # send email when job begins
#SBATCH --mail-user=eonal@princeton.edu

module purge
module load anaconda3/2022.5
conda activate entbank

export PYTHONPATH=/scratch/gpfs/eonal/nlproofs/entailment_bank

python evaluate_validation.py dbs d_n10.0b_2 val
python evaluate_validation.py dbs d_n5.0b_2 val
python evaluate_validation.py dbs d_n2.0b_2 val
python evaluate_validation.py dbs d_n0.8b_2 val
python evaluate_validation.py dbs d_n0.5b_2 val
python evaluate_validation.py dbs d_n0.2b_2 val
python evaluate_validation.py dbs d_p0.0b_2 val
python evaluate_validation.py dbs d_p0.2b_2 val
python evaluate_validation.py dbs d_p0.5b_2 val
python evaluate_validation.py dbs d_p0.8b_2 val
python evaluate_validation.py dbs d_p2.0b_2 val
python evaluate_validation.py dbs d_p5.0b_2 val
python evaluate_validation.py dbs d_p10.0b_2 val
