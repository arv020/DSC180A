import pandas as pd
import numpy as np
import pylab as pl
from statistics import mode
from sklearn.linear_model import LogisticRegression
import os
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

sys.path.insert(0, 'src')
from data import modify_data
from analysis import pktdir_vs_pktsze_int pktdir_vs_pktsze_vid
from features import binarymean_packetsizes binary_max_pksz prop_pksize_dir12 prop_pksize_dir12 classifier
from models import filter_out filter_out_table classify_training table_output_col build_df build_model final_output
from utils import convert_notebook



def main(targets):

    data_config = json.load(open('config/data-params.json'))
    analysis_config = json.load(open('config/analysis-params.json'))
    features_config = json.load(open('config/features-params.json'))
    

    if 'data' in targets:
        
        # create the symlink
   
        link = os.symlink(data_config['raw_data'], outdir, target_is_directory = True)
        data = get_data(link)
        data = modify_data(data)

        
        #data = generate_data(**data_config)
        #save_data(data, **data_config)

    if 'analysis' in targets:
        
        findings = analysis_config['dataset']
        
        

#         try:
#             data
#         except NameError:
#             data = pd.read_csv(data_config['raw_data'])

#         generate_stats(data, **eda_config)
        
#         # execute notebook / convert to html
#         convert_notebook(**eda_config)
        
     if 'features' in targets:
            
            new_features = features_config["mean_num"]


if __name__ == '__main__':

    targets = sys.argv[1:]
    main(targets)
