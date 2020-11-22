import sys
import json
import pandas as pd

sys.path.insert(0, 'src')
from data import get_data modify_data
from analysis import no_streaming_viz streaming_viz pktdir_vs_pktsze_int pktdir_vs_pktsze_vid
from features import big_byte_count_feature binarymean_packetsizes binarymin_packetsizes
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
