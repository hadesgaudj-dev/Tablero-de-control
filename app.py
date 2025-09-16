import pandas as pd
import streamlit as st
import plotly.express as px

url = 'https://github.com/juliandariogiraldoocampo/ia_taltech/raw/refs/heads/main/fiscalia/datos_generales_ficticios.csv'
df = pd.read_csv(url, sep=';', encoding='utf-8')

# Crear lista de las Columnas de Interés
seleccion_columnas = ['FECHA_HECHOS','DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
# Actualizo el dataframe -df- con las columnas de interés, ordenadas por fecha y reseteo el índice
df = df[seleccion_columnas].sort_values(by='FECHA_HECHOS', ascending=True).reset_index(drop=True)

# Convierto la columna FECHA_HECHOS a formato fecha
df['FECHA_HECHOS'] = pd.to_datetime(df['FECHA_HECHOS'], errors='coerce')
# Extraigo solo la fecha (sin hora)
df['FECHA_HECHOS'] = df['FECHA_HECHOS'].dt.date

conteo_municipios = df['MUNICIPIO_HECHOS'].value_counts()

# CÁLCULO DE MUNICIPIO CON MAS DELITOS
max_municipio = df['MUNICIPIO_HECHOS'].value_counts().index[0].upper()
max_cantidad_municipio = df['MUNICIPIO_HECHOS'].value_counts().iloc[0]

# CALCULO DE LA ETAPA QUE MAS VECES SE PRESENTA
# Ya que value_counts() genera un dataframe ORDENADO, traigo solo EL PRIMER INDICE .index[0]
etapa_mas_frecuente = df['ETAPA'].value_counts().index[0].upper()
# Ya que value_counts() genera un dataframe ORDENADO, traigo solo EL PRIMER VALOR .iloc[0]
cant_etapa_mas_frecuente = df['ETAPA'].value_counts().iloc[0]



# __________________________________________CONSTRUIR LA PÁGINA
st.set_page_config(page_title="Dashboard de Delitos - Fiscalía", layout="wide")
st.markdown(
    """
	<style>
		.block-container {
			padding: 1rem 2rem 2rem 2rem;
			max-width: 1600px;
		}
    </style>
	""",
    unsafe_allow_html=True
)

st.image('img\PORTADA.svg', use_container_width=True)
# st.markdown("# <font color = #3B668C> Dashboard de Delitos - Fiscalía | Bootcamp </font>", unsafe_allow_html=True)

# Gráfico de barras apiladas por departamento y tipo de delito
st.subheader("Delitos por Departamentos")
df_delitos = df.groupby(['DEPARTAMENTO', 'DELITO']).size().reset_index(name='conteo')
fig = px.bar(df_delitos, x='DEPARTAMENTO', y='conteo', color='DELITO', barmode='stack')
st.plotly_chart(fig, key="bar_departamentos")
fig.update_layout(showlegend=False, height=400)

# CREAR 4 COLUMNAS PARA LAS TARJETAS
col1, col2, col3, col4 = st.columns(4)

with col1:
	## Tarjeta 1 - Municipio con más delitos
	st.markdown(f"""<h3 style=
				'color:#F2A88D;
				background-color:#FFF6F5;
				border: 2px solid #F2A88D;
				border-radius: 10px; padding: 10px;
				text-align: center'>
				Municipio con más delitos: {max_municipio}</h3><br>""",
				unsafe_allow_html=True
	)

with col2:
	## Tarjeta 2 - Cantidad de delitos en el municipio con más delitos
	st.markdown(f"""<h3 style=
				'color:#F2A88D;
				background-color:#FFF6F5;
				border: 2px solid #F2A88D;
				border-radius: 10px; padding: 10px;
				text-align: center'>
				Delitos reportados<br>{max_cantidad_municipio} </h3><br>""",
				unsafe_allow_html=True
	)

with col3:
	## Tarjeta 3 - Etapa mas recurrente
	st.markdown(f"""<h3 style=
				'color:#F2A88D;
				background-color:#FFF6F5;
				border: 2px solid #F2A88D;
				border-radius: 10px; padding: 10px;
				text-align: center'>
				Etapa mas recurrente<br>{etapa_mas_frecuente} </h3><br>""",
				unsafe_allow_html=True
	)
with col4:
	## Tarjeta 3 - Etapa mas recurrente
	st.markdown(f"""<h3 style=
				'color:#F2A88D;
				background-color:#FFF6F5;
				border: 2px solid #F2A88D;
				border-radius: 10px; padding: 10px;
				text-align: center'>
				procesos en esta etapa<br>{cant_etapa_mas_frecuente} </h3><br>""",
				unsafe_allow_html=True
	)

#col5, col6 = st.columns(2)

#with col5:


st.subheader('Comportamiento Delitos')
delitos = df['DELITO'].value_counts()
st.bar_chart(delitos)

st.subheader('Departamentos con mas Casos')
departamento = df['DEPARTAMENTO'].value_counts()
st.bar_chart(departamento)

st.subheader("Distribución por Departamentos")
fig = px.pie(
	names=departamento.index,  # Para los nombres de la Torta
	values=departamento.values # Para los valores de la Torta
)
fig.update_traces(textposition='outside', textinfo='percent+label')
fig.update_layout(showlegend=False, height=450)
st.plotly_chart(fig, key="torta_departamentos")



st.dataframe(df)

#st.subheader('tipo delitos')
grafico = df_grafico[variable].value_counts()
st.bar_chart(grafico)

if st.checkbox('mostrar Matriz de Datos'):
	st.subheader('Matriz de Datos')
	st.dataframe(df_grafico)

# seleccion de dato para visualizar
#cols_grafico = ['FECHA_HECHOS','DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
#df_grafico = df[cols_grafico]

st.header("Consulta por Fiscal Asignado")
fiscal_consulta = st.selectbox(
	'Seleccione el Fiscal a consultar',
	options = df['FISCAL_ASIGNADO'].unique()
)

df_fiscal = df[df['FISCAL_ASIGNADO'] == fiscal_consulta]
st.dataframe(df_fiscal)




#leer datos


