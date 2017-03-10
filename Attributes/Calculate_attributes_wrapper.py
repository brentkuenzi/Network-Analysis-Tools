import sys
import os
import subprocess
edgeList = sys.argv[1]
centrality = sys.argv[2]
community = sys.argv[3]
os.system(r"Rscript "+"Calculate_attributes.R "+ str(edgeList) + r" " + str(centrality)+ r" " + str(community))