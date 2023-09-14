import pickle
import streamlit as st
import numpy as np
import requests
import webbrowser



st.header('Mouse Recommender System Using Machine Learning')
model = pickle.load(open('artifacts/mrmodel.pkl','rb'))
mouse_names = pickle.load(open('artifacts/mouse_names.pkl','rb'))
final_rating = pickle.load(open('artifacts/m_final_rating.pkl','rb'))
mouse_pivot = pickle.load(open('artifacts/mouse_pivot.pkl','rb'))

def fetch_poster(suggestion):
    mouse_name = []
    ids_index = []
    poster_url = []

    for mouse_id in suggestion:
        mouse_name.append(mouse_pivot.index[mouse_id])

    for name in mouse_name[0]: 
        ids = np.where(final_rating['title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['image_url']
        poster_url.append(url)

    return poster_url

def recommend_mouse(mouse_name):
    mouse_list = []
    mouse_id = np.where(mouse_pivot.index == mouse_name)[0][0]
    distance, suggestion = model.kneighbors(mouse_pivot.iloc[mouse_id,:].values.reshape(1,-1), n_neighbors=6 )

    poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
            mouse = mouse_pivot.index[suggestion[i]]
            for j in mouse:
                mouse_list.append(j)
    return mouse_list , poster_url       

selected_mouse = st.selectbox(
    "Type or select a mouse from the dropdown",
    mouse_names
)

laz_url = "https://www.lazada.com.my/catalog/?q="
shp_url = "https://shopee.com.my/search?keyword="

laz1 = "laz l1"
laz2 = "laz l2"
laz3 = "laz l3"
laz4 = "laz l4"
laz5 = "laz l5"
shp1 = "shp l1"
shp2 = "shp l2"
shp3 = "shp l3"
shp4 = "shp l4"
shp5 = "shp l5"


if st.button('Show Recommendation'):
    recommended_mouse,poster_url = recommend_mouse(selected_mouse)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_mouse[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommended_mouse[2])
        st.image(poster_url[2])
    with col3:
        st.text(recommended_mouse[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommended_mouse[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommended_mouse[5])
        st.image(poster_url[5])

if st.button("Buy on Lazada"):
    laz_query = selected_mouse
    query_laz = laz_url + laz_query 
    webbrowser.open_new_tab(query_laz)
##    st.markdown(f'<a href="{query_laz}" target="_blank" id="link2" style="display: none;"></a>', unsafe_allow_html=True)
##    st.markdown('<script>document.getElementById("link2").click();</script>', unsafe_allow_html=True)

if st.button("Buy on Shopee"):
    shp_query = selected_mouse
    query_shp = shp_url + shp_query 
    webbrowser.open_new_tab(query_shp)
##    st.markdown(f'<a href="{query_shp}" target="_blank" id="link2" style="display: none;"></a>', unsafe_allow_html=True)
##    st.markdown('<script>document.getElementById("link2").click();</script>', unsafe_allow_html=True)