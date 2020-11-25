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
    models_config = json.load(open('config/models-params.json'))
    

    if 'data' in targets:
        
        # create the symlink
   
        filepath = '/teams/DSC180A_FA20_A00/b05vpnxray/data/unzipped'
        data = os.listdir(filepath)
        
        model_df = filter_out_table()
        
        #this creates the data df that builds the model
        model_df = table_output_col(model_df)
        

        
        #data = generate_data(**data_config)
        #save_data(data, **data_config)
        
        
            
     
            
     if 'models' in targets:
        
        build_df(model_df)
        
        #at this point we have a logistic regression model (reg)
        build_model(model_df)
     
    
     #at the end, we want to return Streaming/Not streaming an input
     return "success"
        
        
        


if __name__ == '__main__':

    targets = sys.argv[1:]
    main(targets)
