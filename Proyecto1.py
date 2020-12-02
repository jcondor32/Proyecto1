import streamlit as st
import pandas as pd
import altair as alt
import math
from PIL import Image
from pandas import read_excel
import plotly.express as px
# Lectura del archivo Excel
# data=pd.read_excel('Proyecto1.xlsx',sheet_name='Sheet1')
image1=Image.open("040_Guarumos.jpg")
st.image(image1)
html_temp = """
	<div style="background-color:teal ;padding:10px">
	<h2 style="color.white;text-align:center;">Proyecto 1</h2>
	</div>
	"""
st.markdown(html_temp,unsafe_allow_html=True)
st.title("Proyecto 1")
st.write(""" Primera Aplicacion - Proyecto 1
	### ** Inicia proyetco sobre Phyton **

	|Kro|Krw|Sw|
	|---|---|--|
	|0.2|0.3|0.4|
""")
st.sidebar.title("Parametros")

checkbox1=st.checkbox('DataFrame',value=False)
if checkbox1==True:

	def ingreso_parametros():
		permeabilidad=st.sidebar.slider('Permeabilidad',0.0,1.0,0.2,step=0.1)
		saturacion=st.sidebar.slider('Saturacion',0.0,1.0,0.2,step=0.1)
		porosidad=st.sidebar.slider('Porosidad',0.0,1.0,0.2,step=0.1)
		parametros={'Permeabilidad':permeabilidad,
					'Saturacion':saturacion,
					'Porosidad':porosidad}
		parametros_iniciales=pd.DataFrame(parametros, index=['adimensional'])
		return parametros_iniciales
	df_parametros=ingreso_parametros()
	st.write(df_parametros)
	st.write('Resultados')
	selectbox1=st.selectbox('Elja una opcion',('Permeabilidad','Porosidad', 'Saturacion'),index=2)
	grafico=alt.Chart(df_parametros).mark_point().encode(
		alt.X('Permeabilidad'),
		alt.Y('Saturacion')
		).interactive().properties(title='Primer Grafico',width=700,height=400)
	st.altair_chart(grafico)
lista1={1,2,3,4,5,6,7,8,9,10}
st.write(lista1)
lista2=[1,2,3,4,5,6,7,8,9,10]
st.write(lista2)
lista3=list(range(1,200,2))
st.write(lista3)
lista4=[i*3 for i in lista3]
st.write(lista4)
lista5=[math.cos(n) for n in lista4]
st.write(lista5)
data2={'Lista 3':lista3, 
		'Lista 4':lista4,
		'Lista 5':lista5}
df_data2=pd.DataFrame(data2)
st.write(df_data2)
fig=px.line_3d(df_data2, x="Lista 3",y="Lista 4", z="Lista 5")
st.write(fig)