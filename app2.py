# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 13:43:28 2022

@author: tom97
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 11:19:44 2022

@author: tom97
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st



pickle_in = open('model.pkl','rb')
model = pickle.load(pickle_in)



def welcome():
    return "Welcome All"
    
def recommendmovies(title):
    
    matrix = pd.read_csv('matrix',index_col = 'Book-Title')
    
    X = pd.DataFrame(matrix.index)
    X.reset_index(inplace = True)
    X.rename(columns = {'index':'Serial_No'},inplace = True)
    
    df = X.set_index('Book-Title').to_dict()['Serial_No']
    
    q = df[title]
    
    distances,indices = model.kneighbors(matrix.iloc[q,:].values.reshape(1,-1),n_neighbors = 6)
    
    str = ""
    
    for i in range(0, len(distances.flatten())):
        if i == 0:
            print('Recommendations for {0}:\n'.format(matrix.index[q]))

            str = str + 'Recommendations for {0}:\n'.format(matrix.index[q])
            str =  str + '\n'
        else:
            print('{0}: {1}, with distance of {2}:'.format(i, matrix.index[indices.flatten()[i]], distances.flatten()[i]))
            str= str + '{0}: {1}\n'.format(i, matrix.index[indices.flatten()[i]])
            str =  str + '\n'

    return str


def main():
    st.title("Recommended Books")
    

        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://i0.wp.com/ebookfriendly.com/wp-content/uploads/2013/11/The-World-in-a-Book.jpg?resize=540%2C304&ssl=1");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    

    
    title = st.text_input("Title")

    result =""
    
    
    
    if st.button("Recommendation for similar books"):
        
        result = recommendmovies(title)
        st.success(result)
    
    
    
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    main()