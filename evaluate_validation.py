import subprocess
import os
import sys

### SETTINGS ###################################

exp_type = sys.argv[1] # verifier / dbs / aggr
exp_name = sys.argv[2]
num_to_run = 1 # 1, 2, 3

split = sys.argv[3] # test / val (dev in ebank flag)
log_path = '/scratch/gpfs/eonal/nlproofs/NLProofS/prover/lightning_logs/'
out_path = '/scratch/gpfs/eonal/nlproofs/entailment_bank/outputs/'

################################################

split_name = 'test' if split == 'test' else 'dev'

dbs_exps = {'d_n100.0b_2': ['47413238_2'],
            'd_n10.0b_2': ['47413243_2'],
            'd_n5.0b_2': ['47413244_2'],
            'd_n2.0b_2': ['47413245_2'],
            'd_n0.8b_2': ['47413247_2'],
            'd_n0.5b_2': ['47413249_2'],
            'd_n0.2b_2': ['47413250_2'],
            'd_p0.0b_2': ['47413258_2'],
            'd_p0.2b_2': ['47413261_2'],
            'd_p0.5b_2': ['47413330_2'],
            'd_p0.8b_2': ['47413263_2'],
            'd_p2.0b_2': ['47413266_2'],
            'd_p5.0b_2': ['47413276_2'],
            'd_p10.0b_2': ['47413279_2'],#
            'd_n100.0b_5': ['47413238_5'],
            'd_n10.0b_5': ['47413243_5'],
            'd_n5.0b_5': ['47413244_5'],
            'd_n2.0b_5': ['47413245_5'],
            'd_n0.8b_5': ['47413247_5'],
            'd_n0.5b_5': ['47413249_5'],
            'd_n0.2b_5': ['47413250_5'],
            'd_p0.0b_5': ['47413258_5'],
            'd_p0.2b_5': ['47413261_5'],
            'd_p0.5b_5': ['47413330_5'],
            'd_p0.8b_5': ['47413263_5'],
            'd_p2.0b_5': ['47413266_5'],
            'd_p5.0b_5': ['47413276_5'],#
            'd_p10.0b_5': ['47413279_5'],
            'd_n100.0b_10': ['47413238_10'],
            'd_n10.0b_10': ['47413243_10'],
            'd_n5.0b_10': ['47413244_10'],
            'd_n2.0b_10': ['47413245_10'],
            'd_n0.8b_10': ['47413247_10'],
            'd_n0.5b_10': ['47413249_10'],
            'd_n0.2b_10': ['47413250_10'],
            'd_p0.0b_10': ['47413258_10'],
            'd_p0.2b_10': ['47413261_10'],
            'd_p0.5b_10': ['47413330_10'],
            'd_p0.8b_10': ['47413263_10'],
            'd_p2.0b_10': ['47413266_10'],
            'd_p5.0b_10': ['47413276_10'],#
            'd_p10.0b_10': ['47413279_10']}

verifier_exps = {'0.0': ['47400912', '47400913', '47400914'],
                 '0.1': ['47400919', '47400920', '47400921'],
                 '0.2': ['47400925', '47400926', '47400927'],
                 '0.3': ['47400928', '47400930', '47400931'],
                 '0.4': ['47400932', '47400933', '47400934'],
                 '0.5': ['47400935', '47400936', '47400937'],
                 '0.6': ['47400940', '47400941', '47400942'],
                 '0.7': ['47400943', '47400948', '47400949'],
                 '0.8': ['47400950', '47412389', '47412392'],
                 '0.9': ['47413081_0', '47413081_1', '47413081_2'],
                 '1.0': ['47413083_0', '47413083_1', '47413083_2']}

aggr_exps = {'min_sp': ['47308015', '47357884', '47357885'],
             's*min_p': ['47308010', '47357887', '47357888'],
             's^k*min_p_2': ['47308077', '47357892', '47357893'],
             's^k*min_p_3': ['47354716', '47357895', '47357896'],
             's*p': ['47357898', '47357899', '47400882'],
             'min1_sp*min2_sp': ['47392929', '47399890', '47399938'],
             'min*max': ['47392978', '47399969', '47399983'],
             'min1*min2*max1*max2': ['47392988', '47400252', '47400253'],
             'min_exp_step_score': ['47400325', '47400528', '47400529'],
             'min_s_weighted': ['47400497', '47400525', '47400526'],
             'weighted_nr_ancestors': ['47432835','47413490'],
             'av_nr_ancestors': ['47432845','47413507']}

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
    out_dir = out_dir + '/' + str(i)

    print('Starting exp ', exp_ids[i])

    subprocess.run(f'python eval/run_scorer.py \
                    --task "task_2" \
                    --split {split_name} \
                    --prediction_file {tsv_paths[i]} \
                    --output_dir {out_dir}  \
                    --bleurt_checkpoint checkpts/bleurt-large-512', shell=True)
