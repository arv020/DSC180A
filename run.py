import pandas as pd
import numpy as np
import pylab as pl
import os
from sklearn.ensemble import RandomForestClassifier

sys.path.insert(0, 'src')
from all_features import filter_out_table table_output_col build_df build_model

from utils import convert_notebook



def main(targets):

    data_config = json.load(open('config/data-params.json'))
    analysis_config = json.load(open('config/analysis-params.json'))
    features_config = json.load(open('config/features-params.json'))
    models_config = json.load(open('config/models-params.json'))
    

    filepath = '/teams/DSC180A_FA20_A00/b05vpnxray/data/unzipped'
    data = os.listdir(filepath)
    
    if 'data' in targets:

        model_df = build_df(table_output_col(filter_out_table()))
        
        #this creates the data df that builds the model

            
     if 'models' in targets:
        
        #here we have a Random Forest Classifier Model built
        output = build_df(model_df, input_data)
        
        
    
     #at the end, we want to return Streaming/Not streaming an input
     return output
        
        
        


if __name__ == '__main__':

    targets = sys.argv[1:]
    main(targets)
