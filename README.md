Network Analysis Tools
----------------------

This repository contains functions to analyze the community structure & centrality metrics of an undirected network and visualize the outputs. Options for module detection include:
- optimal
	- WARNING: computational time increases exponentially with number nodes! Works well with < 40 nodes.
- fast.greedy
- edge.betweenness
- walk.trap
- spin.glass
- leading.eigenvector
- label.propagation
- multilevel

Options for centrality include:
- eigenvector
- betweenness
- closeness

Interactive networks are visualized using D3.js and returned as an HTML file containing both the input data and javascript to render the graph. Visualizations were adapted using Mike Bostock's examples (https://bl.ocks.org/mbostock). Visualizations include:
- Force directed network
- Force directed network (nodes scaled with centrality)
- Clustered adjacency matrix
- Hierarchical edge bundling
