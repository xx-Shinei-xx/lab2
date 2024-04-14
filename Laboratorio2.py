import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

data = pd.read_csv('datos1.csv')
A = 465.464
u = 89.2538
r = 7.13597
x_fit = np.linspace(0, 100, 100)
x = data['N']

def funcion_gaussiana(x, A, u, r):
    return A * np.exp(-((x - u) / r) ** 2 / 2)

fit_y = funcion_gaussiana(x, A, u, r)

fig = go.Figure()

fig.add_trace(go.Bar(x=x, y=data['Casos por fecha de emisión de resultados'],name='Días VS total de contagios',marker=dict(
        colorscale='redor',  # Aquí puedes cambiar el esquema de colores según tu preferencia
        color=data['Casos por fecha de emisión de resultados']
    )))

fig.add_trace(go.Scatter(x=x_fit, y=fit_y, name='Fit', mode='lines'))

fig.update_layout(
    title='Gráfico combinado',
    xaxis_title='Numero de día',
    yaxis_title='Casos por fecha de emisión de resultados',
    barmode='group'
)

st.plotly_chart(fig)


#Grafica del inicio al 1 de junio de 2020
data2 = pd.read_csv('datos2.csv')
A2= 1062.39
u2=  139.803 
r2=  35.1769 
x_fit2= np.linspace(0,190,100)
x2= data2['N']
def funcion2_gaussiana(x2, A2, u2, r2):
    return A2 * np.exp(-((x2 - u2) / r2) ** 2 / 2)  
fit2_y = funcion2_gaussiana(x2, A2, u2, r2)
fig2= go.Figure()

fig2.add_trace(go.Bar(x=x2, y=data2['Casos por fecha de emisión de resultados'],name='Días VS total de contagios',marker=dict(
        colorscale='inferno',  # Aquí puedes cambiar el esquema de colores según tu preferencia
        color=data2['Casos por fecha de emisión de resultados']
    )))

fig2.add_trace(go.Trace(x=x_fit2, y=fit2_y, name='Fit'))
fig2.update_layout(
    title='Gráfico combinado',
     xaxis_title='Numero de día',
    yaxis_title='Casos por fecha de emisión de resultados',
    barmode='group'
)

st.plotly_chart(fig2)
