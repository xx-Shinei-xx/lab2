import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go

# Load data
data1 = pd.read_csv('datos1.csv')
data2 = pd.read_csv('datos2.csv')

# Parameters for Gaussian functions
A1, u1, r1 = 465.464, 89.2538, 7.13597
A2, u2, r2 = 1062.39, 139.803, 35.1769

# Generate x values for fitting curve
x_fit1 = np.linspace(0, 100, 100)
x_fit2 = np.linspace(0, 190, 100)

# Define Gaussian function
def gaussian(x, A, u, r):
    return A * np.exp(-((x - u) / r) ** 2 / 2)

# Calculate fitted values
fit_y1 = gaussian(data1['N'], A1, u1, r1)
fit_y2 = gaussian(data2['N'], A2, u2, r2)

# Create first figure
fig1 = go.Figure()
fig1.add_trace(go.Bar(
    x=data1['N'],
    y=data1['Casos por fecha de emisión de resultados'],
    name='Días VS total de contagios',
    marker=dict(color=data1['Casos por fecha de emisión de resultados'], colorscale='redor')
))
fig1.add_trace(go.Scatter(
    x=x_fit1,
    y=fit_y1,
    name='Fit',
    mode='lines'
))
fig1.update_layout(
    title='Gráfico combinado - Primer conjunto de datos',
    xaxis_title='Número de día',
    yaxis_title='Casos por fecha de emisión de resultados',
    barmode='group'
)

# Create second figure
fig2 = go.Figure()
fig2.add_trace(go.Bar(
    x=data2['N'],
    y=data2['Casos por fecha de emisión de resultados'],
    name='Días VS total de contagios',
    marker=dict(color=data2['Casos por fecha de emisión de resultados'], colorscale='inferno')
))
fig2.add_trace(go.Scatter(
    x=x_fit2,
    y=fit_y2,
    name='Fit',
    mode='lines'
))
fig2.update_layout(
    title='Gráfico combinado - Segundo conjunto de datos',
    xaxis_title='Número de día',
    yaxis_title='Casos por fecha de emisión de resultados',
    barmode='group'
)

# Display figures in Streamlit
st.plotly_chart(fig1)
st.plotly_chart(fig2)

