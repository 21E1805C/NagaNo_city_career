# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 17:41:22 2022

@author: alber
"""

import streamlit as st

st.title('あなたの未来のキャリア')
st.write('長野県の職のプラットフォーム')

text = st.text_input('あなたの名前を教えてください')
'あなたは',text,'さんですね'

condition = st.slider('就職についての気持ちを数字で表してください',0, 100, 50)
'コンディション:',condition



