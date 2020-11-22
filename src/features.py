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
