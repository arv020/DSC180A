import pandas as pd
import numpy as np
import pylab as pl
import os
from sklearn.ensemble import RandomForestClassifier


def filter_out(x):
    return ('._' in x) or (' ' in x)

def filter_out_table():
    filepath = '/teams/DSC180A_FA20_A00/b05vpnxray/data/unzipped'
    data = os.listdir(filepath)
    df = pd.DataFrame({"input": data})
    df['remove'] = df['input'].apply(filter_out)
    df = df[df['remove'] == False]
    df = df.drop(columns = ["remove"])
    df.reset_index(drop=True, inplace=True)
    return df
    
def classify_training(x):
    return ('novideo' in x) or ('browsing' in x) or ('internet' in x)
    

def table_output_col(df):
    
    df['output'] = df['input'].apply(classify_training).replace({True: 'Not Streaming', False: 'Streaming'})
    return df
    
def modify_data(raw_data):
    #we are separating the column "packet sizes"
    new_pksize = []
    for i in raw_data["packet_sizes"]:
        arr = i.split(";")
        for j in arr[:-1]:
            new_pksize.append(j)

    #we are separating the column "packet dir"
    new_pkdir = []
    for i in raw_data["packet_dirs"]:
        arr = i.split(";")
        for j in arr[:-1]:
            new_pkdir.append(j)

    modified_data = pd.DataFrame({'packet_sizes': pd.to_numeric(new_pksize), 'packet_dir': pd.to_numeric(new_pkdir)})
    return modified_data
    
def prop_pksize_dir12(tbl, num):
    proportion = tbl[tbl["packet_sizes"] < num]["packet_dir"].value_counts()[2]/ tbl[tbl["packet_sizes"] < num]["packet_dir"].value_counts()[1]
    
    return proportion
    
    
    
def binarymin_packetsizes(modified_data, num):
    output = (modified_data["packet_sizes"].min() <= num)
    if output == 1:
        return "Streaming"
    else:
        return "Not Streaming"
        
        
 def binary_max_pksz(tbl, num):
    num_packets = tbl[tbl["packet_sizes"] >= num].size
    if num_packets > 0:
        return "Streaming"
    else:
        return "Not Streaming"
        
def prop_range200_400_dir1(tbl, num1, num2):
    a = len(tbl[(tbl["packet_sizes"] > num1) & (tbl["packet_sizes"] < num2) & (tbl["packet_dir"] == 1)])
    b = len(tbl[tbl["packet_dir"] == 1])
    return a/b
    
def prop_200toentire(tbl, num):
    proportion = tbl[tbl["packet_sizes"] < num]["packet_dir"].size/tbl["packet_sizes"].size
    return proportion
    
    
def prop_1200toentire(tbl, num):
    proportion = tbl[tbl["packet_sizes"] > num]["packet_dir"].size/tbl["packet_sizes"].size
    return proportion
    
def classifier_model(raw_data):
    raw_data = pd.read_csv('/teams/DSC180A_FA20_A00/b05vpnxray/data/unzipped/' + raw_data)
    
    #should input features that take data as a parameter
    #this will create a list of 1/0 's
    feature1 = prop_pksize_dir12(modify_data(raw_data))
    feature2 = binarymin_packetsizes(modify_data(raw_data))
    feature3 = binary_max_pksz(modify_data(raw_data))
    feature4 = prop_range200_400_dir1(modify_data(raw_data))
    feature5 = prop_200toentire(modify_data(raw_data))
    feature6 = prop_1200toentire(modify_data(raw_data))
   
    output =  [feature1, feature2, feature3, feature4, feature5, feature6]
    return output

def filter_lst(lst):
    for i in range(len(lst)):
        if lst[i] == 'Not Streaming':
            lst[i] = 0
        if lst[i] == 'Streaming':
            lst[i] = 1
        else:
            
            lst[i] = float(lst[i])
    return lst
    
def classifier_input(raw_data):
    
    #should input features that take data as a parameter
    #this will create a list of 1/0 's
    feature1 = prop_pksize_dir12(modify_data(raw_data))
    feature2 = binarymin_packetsizes(modify_data(raw_data))
    feature3 = binary_max_pksz(modify_data(raw_data))
    feature4 = prop_range200_400_dir1(modify_data(raw_data))
    feature5 = prop_200toentire(modify_data(raw_data))
    feature6 = prop_1200toentire(modify_data(raw_data))   
    output =  [feature1, feature2, feature3, feature4, feature5, feature6]
    return [filter_lst(output)] 

def build_df(df):
    ft1 = []
    ft2 = []
    ft3 = []
    ft4 = []
    ft5 = []
    ft6 = []

    for i in range(len(df['input'])):
        fts = classifier(df['input'][i])

        ft1.append(fts[0])
        ft2.append(fts[1])
        ft3.append(fts[2])
        ft4.append(fts[3])
        ft5.append(fts[4])
        ft6.append(fts[5])


    df['feature1'] = ft1
    df['feature2'] = ft2
    df['feature3'] = ft3
    df['feature4'] = ft4
    df['feature5'] = ft5
    df['feature6'] = ft6
    
    return df


def build_model(df, input_data):
    
    X = df.drop(columns = ["output", 'input'])
    y = df['output']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)


    clf = RandomForestClassifier(max_depth=2, random_state=0)
    clf.fit(X_train, y_train)
    output = clf.predict(classifier_input(input_data))
    if output == 1:
        output = "Streaming"
    if output == 0:
        output = "Not Streaming"

    return "This model has predicted this dataset to be: " + str(output)
