import sys
import os
def readTab(infile): # read in txt file
    with open(infile, 'r') as input_file: 
    # read in tab-delim text
        output = []
        for input_line in input_file:
            input_line = input_line.strip()
            temp = input_line.split('\t')
            output.append(temp)
    return output
def network2Adjacency(infile):
	network = readTab(infile)
	edges = {}
	nodes = []
	node_num = {}
	node_rev = {}
	cnt = 1
	for i in network:
		for j in i:
			if j not in nodes:
				nodes.append(j)
				node_num[j] = cnt
				node_rev[str(cnt)] = j
				cnt+=1
	for i in nodes:
		for j in network:
			if i in j:
				if i in edges:
					temp = edges[i]
					for k in j:
						if k != i:
							if k not in temp:
								temp.append(k)
					edges[i] = temp
				else:
					temp = []
					for k in j:
						if k != i:
							temp.append(k)
					edges[i] = temp
	output = []
	for i in nodes:
		edge = edges[i]
		edge_num = []
		for j in edge:
			edge_num.append(str(node_num[j]))
		output.append([str(node_num[i])," ".join(edge_num)])
	with open("tmpOutput.txt", "w") as x:
		for i in output:
			x.write(" ".join(i))
			x.write("\n")
	return node_rev
def calculateCollectiveInfluence(networkFile,circleRadius):
	nodes = network2Adjacency(networkFile)
	os.system("~/CI tmpOutput.txt " + str(circleRadius))
	CI = readTab("INFLUENCERS_0_lvl_" + str(circleRadius) + ".txt")
	CI = CI[7:]
	output = [["Score","Node","Degree","Component"]]
	for i in CI:
		output.append([i[0],nodes[i[1].replace(" ","")],i[2],i[3]])
	with open("Network_CI.txt","w") as x:
		for i in output:
			x.write("\t".join(i))
			x.write("\n")
	os.remove("tmpOutput.txt")

calculateCollectiveInfluence(sys.argv[1],sys.argv[2])
