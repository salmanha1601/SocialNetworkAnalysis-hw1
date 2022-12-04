import pandas as pd
import numpy as np

inNodes = {}
outNodes = {}
wightsEdges = {}
node_name_to_number = {} #dictionary - put an existing nodes name and gets it relevant number
page_rank_arr =[]


'''
@input: path of the csv file 
@output: None
we declare 3 dictionary:
the inNodes dictionary- the key is Target node and at the value is a list of Source nodes 
the outNodes dictionary- the key is Source node and at the value is a list of Target nodes 
the wightsEdges dictionary- the key is tuple of (Source Node,Target Node) and at the value the wight of the edge between the 2 nodes
'''
def load_graph(path):
    df = pd.read_csv(path)

    for i in range(0, df.shape[0]):
        if df['Source'][i] not in outNodes.keys():
            outNodes[df['Source'][i]] = []
        if df['Target'][i] not in inNodes.keys():
            inNodes[df['Target'][i]] = []
        outNodes[df['Source'][i]].append(df['Target'][i])
        inNodes[df['Target'][i]].append(df['Source'][i])
        wightsEdges[(df['Source'][i], df['Target'][i])] = df['Weight'][i]


#calculates each nodes page rank
#page_rank_arr is an array which will hold all the page ranks
#node_name_to_number is a dictionary which sorts a node name to the right index of the page_rank_arr
#this algorithm uses a static matrix which gives us the page rank of the new iteration after we mulitply it
#by the vector (array) of the page rank of the previous iteration and use beta.
#its column i on the matrix shows how node i affects other nodes (weight to j / total weights out of i)
def calculate_page_rank(β=0.85, δ=0.001, maxIterations=20):
    global page_rank_arr
    index = 0
    for name in outNodes.keys():
        node_name_to_number[name] = index
        index = index+1
    for name in inNodes.keys():
        if name not in node_name_to_number:
            node_name_to_number[name] = index
            index = index + 1

    init_arr = []
    k = len(node_name_to_number.keys())
    for i in range(0, k):
        init_arr.append(1.0/k)
    r0 = np.array(init_arr)#first initial vector

    matrix = np.zeros((k, k),dtype= float) #initializes a 0 matrix
    for s in outNodes.keys():
        arr = np.zeros(k)
        sn = node_name_to_number[s]
        total_weight = 0
        target_nodes = outNodes[s]
        for t in target_nodes:
            tn = node_name_to_number[t]
            w = wightsEdges[(s,t)]
            total_weight = total_weight + w
            arr[tn] = w
        arr = arr / total_weight
        matrix[:,sn] = arr

    i = 0
    while i < maxIterations:
        prev = r0
        print(i)
        print(prev)
        r0 = β*np.matmul(matrix, r0)
        trash = (1 - np.sum(r0)) / k
        r0 = r0 + trash
        i = i + 1
        prev = np.absolute(prev - r0)
        is_less_than_epsilon = False
        for x in prev:
            if x < δ:
                is_less_than_epsilon = True
        if is_less_than_epsilon:
            break
    page_rank_arr = r0.tolist()



def get_PageRank(node_name):
    if node_name in node_name_to_number:
        key = node_name_to_number[node_name]
        return page_rank_arr[key]
    return -1

# take second element for sort
def takeSecond(elem):
    return elem[1]

def get_top_PageRank(n):
    lst=[]
    for name in node_name_to_number.keys():
        key = node_name_to_number[name]
        page_rank_arr[key]
        lst.append((name, page_rank_arr[key]))
    lst.sort(key=lambda a: a[1],reverse = True)
    return lst[:n]



def get_all_PageRank():
    list = []
    for name in node_name_to_number.keys():
        key = node_name_to_number[name]
        list.append((name, page_rank_arr[key]))
    return list



load_graph(r'C:\Users\Salman\Desktop\Folders\תואר\שנה ד\סמסטר א\ניתוח רשתות חברתיות\עבודות\soc-sign-bitcoinotc.csv')
calculate_page_rank()
<<<<<<< HEAD
print(get_all_PageRank())
print(get_top_PageRank(2))
=======
print(get_top_PageRank(10))
#print(get_all_PageRank())
>>>>>>> 3d91e494c7844ea8333d1b63f44a3924c39fe031
