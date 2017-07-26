import sys
def readTab(infile): # read in txt file
    with open(infile, 'r') as input_file:
    # read in tab-delim text
        output = []
        for input_line in input_file:
            input_line = input_line.strip()
            temp = input_line.split('\t')
            output.append(temp)
    return output
def write_tab(DF,filename):
	with open(filename,"w") as x:
		for i in DF:
			x.write("\t".join(i)); x.write("\n")
node_attr = readTab(sys.argv[1])
edges = readTab(sys.argv[2])

mods = {}
mods2 = {}
comm_pos = node_attr[0].index("comm")
name_pos = node_attr[0].index("name")
for i in node_attr[1:]:
	mods[i[name_pos]] = i[comm_pos]
	mods2[i[comm_pos]] = i[name_pos]
mod_size = {}
for i in mods2.keys():
	cnt=0
	for j in node_attr[1:]:
		if i in j:
			cnt+=1
	mod_size[i] = cnt
reduced_edges = [["comm1","comm2",'size']]
for i in mods2.keys():
	for j in mods2.keys():
		if i != j:
			reduced_edges.append([i,j,0])
for i in reduced_edges[1:]:
	for j in edges:
		if mods[j[0]] in i:
			if mods[j[1]] in i:
				if mods[j[0]] != mods[j[1]]:
					i[2] = i[2] + 1
for i in reduced_edges[1:]:
	i[0] = "Module "+i[0]
	i[1] = "Module "+i[1]
	i[2] = str(i[2])
final_edges = [["comm1","comm2",'size']]
for i in reduced_edges[1:]:
	if i[2] != "0":
		final_edges.append(i)
reduced_mods = [["comm1","Size"]]
for i in mods2.keys():
	reduced_mods.append(["Module "+i,str(mod_size[i])])
write_tab(final_edges,"reduced_network_edges.txt")
write_tab(reduced_mods,"reduced_network_nodes.txt")
