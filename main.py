import pandas as pd

inNodes = {}
outNodes = {}
wightsEdges = {}

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



def calculate_page_rank(β, δ, maxIterations):
    pass


def get_PageRank(node_name):
    pass


def get_top_PageRank(n):
    pass


def get_all_PageRank():
    pass


load_graph(r'C:\Users\Salman\Desktop\Folders\תואר\שנה ד\סמסטר א\ניתוח רשתות חברתיות\עבודות\soc-sign-bitcoinotc.csv')
