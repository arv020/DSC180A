# 1) choose base container
# generally use the most recent tag

# data science notebook
# https://hub.docker.com/repository/docker/ucsdets/datascience-notebook/tags
ARG BASE_CONTAINER=ucsdets/datascience-notebook:2020.2-stable

# scipy/machine learning (tensorflow)
# https://hub.docker.com/repository/docker/ucsdets/scipy-ml-notebook/tags
# ARG BASE_CONTAINER=ucsdets/scipy-ml-notebook:2020.2-stable

FROM $BASE_CONTAINER

LABEL maintainer="UC San Diego ITS/ETS <ets-consult@ucsd.edu>"

# 2) change to root to install packages
USER root

RUN	apt-get install htop

# 3) install packages
RUN pip install --no-cache-dir pandas numpy pylab mode python-louvain

# 4) change back to notebook user
COPY /run_jupyter.sh /
USER $NB_UID

# Override command to disable running jupyter notebook at launch
# CMD ["/bin/bash"]




#run the following code to define all the functions 

import pandas as pd
import numpy as np
import pylab as pl
from statistics import mode


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
    
def prop_pksize_dir12(tbl):
    proportion = tbl[tbl["packet_sizes"] < 200]["packet_dir"].value_counts()[2]/ tbl[tbl["packet_sizes"] < 200]["packet_dir"].value_counts()[1]
    
    if proportion < .15:
        return "Streaming"
    else:
        return "Not Streaming"
        
def binarymin_packetsizes(modified_data):
    output = (modified_data["packet_sizes"].min() <= 32)
    if output == 1:
        return "Streaming"
    else:
        return "Not Streaming"
        
def binary_max_pksz(tbl):
    num_packets = tbl[tbl["packet_sizes"] >= 1400].size
    if num_packets > 0:
        return "Streaming"
    else:
        return "Not Streaming"
        
        
def prop_range200_400_dir1(tbl):
    a = len(tbl[(tbl["packet_sizes"] > 200) & (tbl["packet_sizes"] < 600) & (tbl["packet_dir"] == 1)])
    b = len(tbl[tbl["packet_dir"] == 1])
    if (a/b) < .15:
        return "Not Streaming"
    else:
        return "Streaming"
        
        
def classifier(raw_data):
    #should input features that take data as a parameter
    #this will create a list of 1/0 's
    feature1 = prop_pksize_dir12(modify_data(raw_data))
    feature2 = binarymin_packetsizes(modify_data(raw_data))
    feature3 = binary_max_pksz(modify_data(raw_data))
    feature4 = prop_range200_400_dir1(modify_data(raw_data))
    return mode([feature1, feature2, feature3, feature4])

#after running all of these functions....
#you just have to run classifier(raw_data) with raw data being a network stats data. It will output Streaming/NoStreaming
classifier(raw_data)
#with raw_data being the network_stats data. 
