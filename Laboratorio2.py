import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Load data
data1 = pd.read_csv('datos1.csv')
data2 = pd.read_csv('datos2.csv')

# Gaussian function
def gaussian(x, A, u, r):
    return A * np.exp(-((x - u) / r) ** 2 / 2)

# Create Streamlit app
st.title('Interactive COVID-19 Data Visualization')

# Initialize figure and parameters
fig = go.Figure()
x_fit = np.linspace(0, 100, 100)

# Plot the first data set with a Gaussian fit
fig.add_trace(go.Bar(
    x=data1['N'],
    y=data1['Casos por fecha de emisión de resultados'],
    name='Días VS total de contagios',
    marker=dict(color=data1['Casos por fecha de emisión de resultados'], colorscale='Reds')
))

A = 465.464
u = 89.2538
r = 7.13597
fit_y = gaussian(x_fit, A, u, r)
fig.add_trace(go.Scatter(
    x=x_fit,
    y=fit_y,
    name='Fit',
    mode='lines'
))

# Plot layout for the first chart
fig.update_layout(
    title='Gráfico combinado - Primer conjunto de datos',
    xaxis_title='Número de día',
    yaxis_title='Casos por fecha de emisión de resultados',
    barmode='group'
)

# Second data set
fig2 = go.Figure()
x_fit2 = np.linspace(0, 190, 100)

fig2.add_trace(go.Bar(
    x=data2['N'],
    y=data2['Casos por fecha de emisión de resultados'],
    name='Días VS total de contagios',
    marker=dict(color=data2['Casos por fecha de emisión de resultados'], colorscale='inferno')
))

A2 = 1062.39
u2 = 139.803
r2 = 35.1769
fit2_y = gaussian(x_fit2, A2, u2, r2)
fig2.add_trace(go.Scatter(
    x=x_fit2,
    y=fit2_y,
    name='Fit',
    mode='lines'
))

# Plot layout for the second chart
fig2.update_layout(
    title='Gráfico combinado - Segundo conjunto de datos',
    xaxis_title='Número de día',
    yaxis_title='Casos por fecha de emisión de resultados',
    barmode='group'
)

# Interactive buttons
chart_selection = st.radio("Seleccionar Gráfico:", ('Primer conjunto de datos', 'Segundo conjunto de datos'))

if chart_selection == 'Primer conjunto de datos':
    st.plotly_chart(fig)
elif chart_selection == 'Segundo conjunto de datos':
    st.plotly_chart(fig2)
