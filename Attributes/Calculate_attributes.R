library(igraph)
library(dplyr)
library(ggplot2)

calculate_attributes <- function(nodes,edges,centrality = "eigenvector",community="fastgreedy") {
  graph <- graph.data.frame(edges, directed = FALSE, vertices = nodes)
  if(community == "optimal"){V(graph)$comm <- membership(optimal.community(graph))} # computationally intensive
  if(community == "fastgreedy"){V(graph)$comm <- membership(fastgreedy.community(graph))} # for larger datasets
  if(centrality == "closeness"){V(graph)$closeness <- centralization.closeness(graph)$res}
  if(centrality == "betweenness"){V(graph)$betweenness <- centralization.betweenness(graph)$res}
  if(centrality == "eigenvector"){V(graph)$eigen <- centralization.evcent(graph)$vector}
  
  write.table(get.data.frame(graph, what = "vertices"),file="node_attr.txt",quote=FALSE,sep="\t",row.names=FALSE)
}
#calculate_attributes(nodes,edgelist,centrality = "betweenness",community="fastgreedy")
args <- commandArgs(trailingOnly = TRUE)
edgelist <- read.table(file=as.character(args[1]), stringsAsFactors = FALSE,sep="\t",header=FALSE)
nodes <- data.frame(V1 = unique(c(edgelist$V1,edgelist$V2)))
calculate_attributes(nodes,edgelist,args[2],args[3])