import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def pktdir_vs_pktsze_int(modified_data):
  modified_data[modified_data["packet_dir"] == 1]["packet_sizes"].plot(kind = "hist")
  modified_data[modified_data["packet_dir"] == 2]["packet_sizes"].plot(kind = "hist")
  pl.title('Packet Directions vs Packet Size: internet browsing data with VPN')
  pl.xlabel('Packet Size')
  pl.ylabel('Frequency')
  pl.legend(["1->2", "2->1"])

def pktdir_vs_pktsze_vid(modified_data):
  modified_data[modified_data["packet_dir"] == 1]["packet_sizes"].plot(kind = "hist")
  modified_data[modified_data["packet_dir"] == 2]["packet_sizes"].plot(kind = "hist")
  pl.title('Packet Directions vs Packet Size: video streaming data with VPN')
  pl.xlabel('Packet Size')
  pl.ylabel('Frequency')
  pl.legend(["1->2", "2->1"])
