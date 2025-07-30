import streamlit as st
import streamlit.components.v1 as htmlviewer

st.set_page_config(layout='wide', page_title='JJun2 Webapp')

# Title
st.title('This is JJun Webapp!!')

# Read HTML files
with open('./index.html', 'r', encoding='utf-8') as f:
    html1 = f.read()

with open('./index2.html', 'r', encoding='utf-8') as f:
    html2 = f.read()

with open('./index3.html', 'r', encoding='utf-8') as f:
    html3 = f.read()

# Layout
col1, col2 = st.columns((4, 1))

# Main Content Area
with col1:
    with st.expander('Content #1 ...'):
        url = 'https://www.youtube.com/watch?v=XyEOEBsa8I4'
        st.info('Content...')
        st.video(url)

    with st.expander('Content #2 ...'):
        htmlviewer.html(html1, height=1200)

    with st.expander('Content #3 ...'):
        htmlviewer.html(html2, height=1200)

    with st.expander('Content #4 ...'):
        htmlviewer.html(html3, height=1400)

# Side Column
with col2:
    with st.expander('Tips..'):
        st.info('Tips..')

# Footer
st.markdown('<hr>', unsafe_allow_html=True)
st.write('<font color="BLUE">(c)copyright. all rights reserved by jjun', unsafe_allow_html=True)
