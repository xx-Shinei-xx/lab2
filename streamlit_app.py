import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Define Gaussian distribution
def gaussian(x, A, u, r):
    return A * np.exp(-((x - u) / r) ** 2 / 2)

# Define plot function with Gaussian fit
def plot_covid_data(data, A, u, r):
    fig = go.Figure()
    x_fit = np.linspace(0, len(data) - 1, 100)

    # Plot COVID-19 data as histogram
    fig.add_trace(go.Histogram(
        x=data.index,
        y=data['Casos por fecha de emisión de resultados'],
        name='Días VS total de contagios',
        marker=dict(color=data['Casos por fecha de emisión de resultados'], coloraxis='coloraxis'),
        nbinsx=len(data)  # Set the number of bins to match the number of data points
    ))

    # Fit Gaussian distribution
    fit_y = gaussian(x_fit, A, u, r)
    fig.add_trace(go.Scatter(
        x=x_fit,
        y=fit_y,
        name='Fit',
        mode='lines'
    ))

    # Update layout
    fig.update_layout(
        title='Gráfico combinado - Conjunto de datos COVID-19',
        xaxis_title='Número de día',
        yaxis_title='Casos por fecha de emisión de resultados',
        coloraxis=dict(colorscale='Reds'),
        barmode='overlay'  # Overlay histograms and Gaussian fit
    )

    return fig

# Load data 1
data1 = pd.read_csv('datos1.csv')
A1 = 465.464
u1 = 89.2538
r1 = 7.13597

# Load data 2
data2 = pd.read_csv('datos2.csv')
A2 = 1062.39
u2 = 139.803
r2 = 35.1769

# Streamlit setup
st.title('Visualización Interactiva de Datos COVID-19')

# Sidebar parameters for first dataset
st.sidebar.title('Parámetros de Ajuste Gaussiano')
st.sidebar.subheader('Primer conjunto de datos')
A_slider1 = st.sidebar.slider('Amplitud (A)', min_value=0.0, max_value=1000.0, value=A1, step=10.0)
u_slider1 = st.sidebar.slider('Media (u)', min_value=0.0, max_value=100.0, value=u1, step=1.0)
r_slider1 = st.sidebar.slider('Desviación estándar (r)', min_value=0.0, max_value=20.0, value=r1, step=0.1)

# Sidebar parameters for second dataset
st.sidebar.subheader('Segundo conjunto de datos')
A_slider2 = st.sidebar.slider('Amplitud (A)', min_value=0.0, max_value=2000.0, value=A2, step=10.0)
u_slider2 = st.sidebar.slider('Media (u)', min_value=0.0, max_value=200.0, value=u2, step=1.0)
r_slider2 = st.sidebar.slider('Desviación estándar (r)', min_value=0.0, max_value=40.0, value=r2, step=0.1)

# Show information about COVID-19
info_button_state = st.button('Mostrar Información sobre COVID-19')
if info_button_state:
    st.subheader('Laboratorio 2: Predicción de COVID19')
    # Display COVID-19 information using expander elements

# Run button to execute the code
run_button_state = st.button('Ejecutar Código')
if run_button_state:
    st.write('**Visualización de Datos**')

    # Plot first dataset
    st.subheader('Primer conjunto de datos')
    fig1 = plot_covid_data(data1, A_slider1, u_slider1, r_slider1)
    st.plotly_chart(fig1)

    # Plot second dataset
    st.subheader('Segundo conjunto de datos')
    fig2 = plot_covid_data(data2, A_slider2, u_slider2, r_slider2)
    st.plotly_chart(fig2)
