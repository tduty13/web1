import streamlit as st
import pickle
import sklearn 
from sklearn.linear_model import LinearRegression
import numpy as np

model=pickle.load(open('lr_model.pkl','rb'))

st.title('Прогнозирование Tensile Elastic Modulus')

st.write('Это приложение позволяет предсказать <Модуль упругости композита при растяжении>')
st.write("Введите значения характеристики")
         
mat_F_rat=st.number_input('Matrix-Filler Ratio',format="%0.10f", step=0.0000000001)
dens=st.number_input('Density',format="%0.10f", step=0.0000000001)  
elast_mod=st.number_input('Elastic Modulus',format="%0.10f", step=0.0000000001)
cur_ag_quan=st.number_input('Curing Agent Quantity',format="%0.10f", step=0.0000000001)
ep_gr_con=st.number_input('Epoxy Groups Content',format="%0.10f", step=0.0000000001)       
fl_po_temp=st.number_input('Flash Point Temperature',format="%0.10f", step=0.0000000001)
res_cons=st.number_input('Resin Consumption',format="%0.10f", step=0.0000000001)
l_step=st.number_input('Layup Step',format="%0.10f", step=0.0000000001)
sur_dens=st.number_input('Surface Density',format="%0.10f", step=0.0000000001) 
l_dens=st.number_input('Layup Density',format="%0.10f", step=0.0000000001) 
layup_0=st.number_input('Layup_0',format="%0.10f", step=0.0000000001) 
layup_90=st.number_input('Layup_90',format="%0.10f", step=0.0000000001)

if st.button('Рассчитать модуль упругости при растяжении'):
    input_data=np.array([mat_F_rat, dens,elast_mod,cur_ag_quan,ep_gr_con,fl_po_temp,res_cons,l_step,sur_dens,l_dens,layup_0,layup_90]).reshape(1, -1)

    prediction=model.predict(input_data)[0]
    st.success(f'Прогнозируемый модуль упругости при растяжении: {prediction: .10f}')
    