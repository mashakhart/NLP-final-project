import subprocess
import os
import sys

### SETTINGS ###################################

exp_type = sys.argv[1] # verifier / dbs / aggr
exp_name = sys.argv[2]
num_to_run = 3 # 1, 2, 3

split = 'test'
log_path = '/scratch/gpfs/eonal/nlproofs/NLProofS/prover/lightning_logs/'
out_path = '/scratch/gpfs/eonal/nlproofs/entailment_bank/outputs_test/'

################################################

split_name = 'test' if split == 'test' else 'dev'

# TEST DICTS ===================================================:
dbs_exps = {'d_n100.0b_2':['47476985_1','47476985_2', '47437814_0'],
            'd_n0.2b_2':['47476993_1','47476993_2','47437821_0'],
            'd_n0.5b_2':['47476994_1','47476994_2','47437822_0'],
            'd_n0.8b_2':['47477002_1','47477002_2','47437826_0'],
            'd_n2.0b_2':['47477011_1','47477011_2','47437830_0'],
            'd_n5.0b_2':['47477029_1','47477029_2','47437834_0'],
            'd_n10.0b_2':['47477036_1','47477036_2','47437835_0'],
            'd_p0.8b_2':['47477038_1','47477038_2','47437843_0']}
verifier_exps = {'0.2':['47477060_1','47477060_2','47437537_0'],
                 '0.3':['47477069_1','47477069_2','47437546_0'],
                 '0.7':['47477085_1','47477085_2','47437556_0'],
                 '0.8':['47477086_1','47477086_2','47437560_0']}
aggr_exps = {'min_exp_step_score':['47477118_1','47477118_2','47437451_0'],
             'min_sp':['47477146_1','47477146_2','47437479_0'],
             'min1_spXmin2_sp':['47477336_1','47477336_2','47437494_0'],
             's_kXmin_p':['47477357_1','47477357_2','47437512_0'],
             's_4Xmin_p':['47512479_1', '47512479_2', '47512329_0'],
             's_2Xmin_p':['47512285_0', '47512285_1', '47512285_2']}

exp_dict = {'verifier': verifier_exps, 'dbs': dbs_exps, 'aggr': aggr_exps}

exp_ids = exp_dict[exp_type][exp_name]
tsv_paths = [log_path + 'version_' + id + '/results_'+split+'.tsv' for id in exp_ids]

print(f'Found {exp_type} exp; exp_name = {exp_name} ID(s) = {exp_ids}')
print(f'num_to_run = {num_to_run}')
exp_ids = exp_ids[:num_to_run]
print(f'Running {exp_ids}')

for i in range(num_to_run):

    out_dir = out_path
    if not os.path.isdir(out_dir + exp_type):
        os.mkdir(out_dir + exp_type)
    out_dir = out_dir + exp_type
    if not os.path.isdir(out_dir + '/' + exp_name):
        os.mkdir(out_dir + '/' + exp_name)
    out_dir = out_dir + '/' + exp_name
    if not os.path.isdir(out_dir + '/' + str(i)):
        os.mkdir(out_dir + '/' + str(i))
    out_dir = out_dir + '/' + str(i+1)
    print('Starting exp ', exp_ids[i])
    print('Saving to ', out_dir)
    subprocess.run(f'python eval/run_scorer.py \
                    --task "task_2" \
                    --split {split_name} \
                    --prediction_file {tsv_paths[i]} \
                    --output_dir {out_dir}  \
                    --bleurt_checkpoint checkpts/bleurt-large-512', shell=True)
