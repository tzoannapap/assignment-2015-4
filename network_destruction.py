
import sys



def size_print_tree(input_file):
	file_to_read=open(input_file,"r")

	temp='a'
	nodes=[]
	other_list=[]
#adjacency list creation
	while temp!=[]:
		temp=file_to_read.readline()
		temp=temp.split()
		nodes.append(temp)
		
	nodes=nodes[:-1]

	for k in nodes:
		for m in k:
			if m not in other_list:
				other_list.append(m)

	other_list=map(int,other_list)
	other_list.sort()

	size=len(other_list)
	
	print "Size : %d members : %s " %(size,other_list) #lista kombwn
	
	return(nodes,size)
	
	#noumero geitonikwn kombwn
def find_connection_weights(node_list,size):
	syndeseis=[]
	for k in range(0,size):
		syndeseis.append(0)
	
	for k in node_list:
		syndeseis[int(k[0])-1]=syndeseis[int(k[0])-1]+1
		syndeseis[int(k[1])-1]=syndeseis[int(k[1])-1]+1
		

	return (syndeseis)



	
# ypothetoume -c epilogi gia tin prwti methodo #

iterations=sys.argv[2]
input_file=sys.argv[3]

#i prwti epanalipsi - afairesi prwtou kombou

node_list,size=size_print_tree(input_file)
vari=find_connection_weights(node_list,size)

timh_eksodou=max(vari)
thesi=vari.index(6)+1
print timh_eksodou,thesi
		
	
	
	
	
	
	
	
	
	
	
	
