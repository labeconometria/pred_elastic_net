import streamlit as st
import pickle
import sklearn
import numpy as np

st.title('Aplicación para predicción')

model = pickle.load(open('model.pickle', 'rb'))
educ = st.slider('Educación', 0, 30)
exper = st.slider('Experiencia', 0, 45)
pred = model.predict(np.array([[educ, exper]]))

st.text(f'El salario por hora es de {pred[0]}.')
