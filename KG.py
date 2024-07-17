import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import pandas as pd 
st.set_page_config(layout="wide")
from streamlit_agraph.config import Config, ConfigBuilder

final_vd = pd.read_csv(r'./final_top51.csv')

with st.sidebar:
  option = st.selectbox(
    'Please select Disease or CoMordities:',
    ('Disease', 'CoMorbidities'))

if option == 'Disease':
     option1 = st.selectbox(
    'Choose disease type:',
    ('ARR', 'CHD', 'CM', 'CVA', 'IHD', 'VD'))
else:
    option2 = st.selectbox(
        'Choose CoMorbidity type:',
        ('Heart failure', 'Liver dysfunction', 'Lung dysfunction', 'Cancer', 'Liver fibrosis', 'Kidney dysfunction'))


final_arr_short = final_vd[final_vd.Condition == option] 

st.title('Knowledge Graph')
df_genes=dict(enumerate(final_arr_short.Protein.unique()))
for i in df_genes:
  nodes.append(Node(id=df_genes[i],
                    label=df_genes[i],
                    size=25,
                    shape="diamond",
                    color='#00008B'
                   )
              )

df_comorbidities = pd.DataFrame(final_arr_short.neighbour_name.value_counts().reset_index().values, columns=["name", "count"])
df_comorbidities = df_comorbidities.sort_index(axis = 0, ascending=True)
df_comorbidities = df_comorbidities[df_comorbidities.name != 'na']
for index, row in df_comorbidities.iterrows():
            nodes.append( Node(id=row['name'],
                        label=row['name'],
                        size=10 * row['count'],
                        shape="square",
                        color='#56a0b3'
                        )
                    ) # includes **kwargs
df_condition = dict()
df_disease = pd.DataFrame(final_arr_short.neighbour_name.value_counts().reset_index().values, columns=["name", "count"])
df_disease = df_disease.sort_index(axis = 0, ascending=True)
df_disease = df_disease[df_disease.name != 'na']
for index, row in df_disease.iterrows():
            nodes.append( Node(id=row['name'],
                        label=row['name'],
                        size=10 * row['count'],
                        shape="square",
                        color='#bf9b30'
                        )
                    ) # includes **kwargs
df_condition=dict(enumerate(final_arr_short.Condition.unique()))
for k in df_condition:
            nodes.append( Node(id=df_condition[k],
                        label=f"          {option}          ",
                        size=200,
                        shape="circle",
                        color='#00FFFF'
                        )
                    ) # includes **kwargs

df_connections = final_arr_short.filter(items=['Protein','neighbour_name']).drop_duplicates()
df_connections = df_connections[df_connections.neighbour_name != 'na']
for index, row in df_connections.iterrows(): 
      edges.append(Edge(source=row['Protein'],
                      label="--",
                      target=row['neighbour_name'],
                      #**kwargs
                      )
                  )
df_mconnections = final_arr_short.filter(items=['Protein','Condition']).drop_duplicates()
for index, row in df_mconnections.iterrows():
      edges.append(Edge(source=row['Condition'],
                      label="--",
                      target=row['Protein'],
                      #**kwargs
                      )
                  )

# initializing buckets
nodes = []
edges = []

df_genes = dict()

config_builder = ConfigBuilder(nodes)
config = config_builder.build()

config.save("config.json")

config = Config(from_json="config.json")

return_value = agraph(nodes=nodes,
                       edges=edges,
                       config=config)


          
        
            
            
