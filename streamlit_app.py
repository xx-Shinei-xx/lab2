import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def gaussian(x, A, u, r):
    return A * np.exp(-((x - u) / r) ** 2 / 2)

def plot_covid_data(data, A, u, r, num_bins=10):
    fig = go.Figure()
    x_fit = np.linspace(0, len(data) - 1, 100)

    # Gráfico de barras de datos COVID-19
    fig.add_trace(go.Bar(
        x=data.index,
        y=data['Casos por fecha de emisión de resultados'],
        name='Días VS total de contagios',
        marker=dict(color=data['Casos por fecha de emisión de resultados'], colorscale='Reds')
    ))

    # Ajuste gaussiano y trazado
    fit_y = gaussian(x_fit, A, u, r)
    fig.add_trace(go.Scatter(
        x=x_fit,
        y=fit_y,
        name='Fit',
        mode='lines'
    ))

    # Histograma con bins personalizados
    data_values = data['Casos por fecha de emisión de resultados'].values
    hist, bins = np.histogram(data_values, bins=num_bins)
    fig.add_trace(go.Bar(
        x=bins,
        y=hist,
        name='Histograma',
        opacity=0.5,
        marker=dict(color='blue')
    ))

    # Diseño del gráfico
    fig.update_layout(
        title='Gráfico combinado - Datos COVID-19',
        xaxis_title='Número de día',
        yaxis_title='Casos por fecha de emisión de resultados',
        barmode='group'
    )

    return fig

# Carga de datos
data1 = pd.read_csv('datos1.csv')
data2 = pd.read_csv('datos2.csv')

# Parámetros iniciales para ajuste gaussiano
A1 = 465.464
u1 = 89.2538
r1 = 7.13597
A2 = 1062.39
u2 = 139.803
r2 = 35.1769

# Aplicación Streamlit
st.title('Visualización Interactiva de Datos COVID-19')

# Mostrar gráficos fuera de los expanders
st.subheader('Visualización de Datos')

# Gráfico para datos1
st.subheader('Primer conjunto de datos')
num_bins1 = st.slider('Número de bins para histograma de datos1', min_value=5, max_value=20, value=10)
fig1 = plot_covid_data(data1, A1, u1, r1, num_bins1)
st.plotly_chart(fig1)

# Gráfico para datos2
st.subheader('Segundo conjunto de datos')
num_bins2 = st.slider('Número de bins para histograma de datos2', min_value=5, max_value=20, value=10)
fig2 = plot_covid_data(data2, A2, u2, r2, num_bins2)
st.plotly_chart(fig2)
