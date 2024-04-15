import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Define functions
def gaussian(x, A, u, r):
    """ Gaussian function """
    return A * np.exp(-((x - u) / r) ** 2 / 2)

def plot_covid_data(data, A, u, r):
    """ Plot COVID-19 data and Gaussian fit """
    fig = go.Figure()
    x_fit = np.linspace(0, len(data) - 1, 100)
    
    # Plot bar chart of COVID-19 data
    fig.add_trace(go.Bar(
        x=data.index,
        y=data['Casos por fecha de emisión de resultados'],
        name='Días VS total de contagios',
        marker=dict(color=data['Casos por fecha de emisión de resultados'], colorscale='Reds')
    ))
    
    # Calculate and plot Gaussian fit
    fit_y = gaussian(x_fit, A, u, r)
    fig.add_trace(go.Scatter(
        x=x_fit,
        y=fit_y,
        name='Fit',
        mode='lines'
    ))
    
    # Customize plot layout
    fig.update_layout(
        title='Gráfico combinado - Conjunto de datos COVID-19',
        xaxis_title='Número de día',
        yaxis_title='Casos por fecha de emisión de resultados',
        barmode='group'
    )
    
    return fig

# Load data
data = pd.read_csv('datos1.csv')

# Create Streamlit app
st.title('Datos COVID-19')

# Display parameters for Gaussian fit
st.sidebar.title('Parámetros de Ajuste Gaussiano')
A = st.sidebar.slider('Amplitud (A)', min_value=0.0, max_value=1000.0, value=465.464, step=10.0)
u = st.sidebar.slider('Media (u)', min_value=0.0, max_value=100.0, value=89.2538, step=1.0)
r = st.sidebar.slider('Desviación estándar (r)', min_value=0.0, max_value=20.0, value=7.13597, step=0.1)

# Display the data
st.write('**Datos COVID-19**')
st.write(data)

# Information about COVID-19 in Guatemala
info_text = """
El COVID-19, derivado de "Coronavirus Disease 2019", es una afección respiratoria provocada por el virus SARS-CoV-2, 
perteneciente a la familia de los coronavirus, que también incluye el SARS-CoV y el MERS-CoV. La principal vía de 
transmisión del SARS-CoV-2 es de persona a persona a través de gotas respiratorias expulsadas al toser, estornudar, 
hablar o respirar, aunque también puede propagarse por contacto con superficies u objetos contaminados con el virus 
y luego tocarse la boca, la nariz o los ojos.

En Guatemala, al igual que en muchos otros países, el COVID-19 ha tenido un impacto significativo en la salud pública y 
en la sociedad en general. Desde el inicio de la pandemia, el país ha experimentado un número considerable de casos 
confirmados de COVID-19, detectados mediante pruebas de laboratorio como PCR y pruebas rápidas de antígenos. La 
transmisión comunitaria del virus ha sido especialmente desafiante en áreas urbanas densamente pobladas de Guatemala, 
llevando a un aumento en la carga de casos en hospitales y centros de salud, poniendo a prueba la capacidad del sistema 
de salud guatemalteco.

El gobierno guatemalteco ha implementado diversas medidas para prevenir la propagación del virus, incluyendo cuarentenas, 
toques de queda y el uso obligatorio de mascarillas. Asimismo, se han llevado a cabo campañas de vacunación masiva como 
parte de las estrategias de control. La disponibilidad de camas de hospital, equipos médicos y personal sanitario ha sido 
un problema en algunos momentos de la pandemia, lo que ha puesto a prueba la capacidad del sistema de salud guatemalteco.

La pandemia ha exacerbado los desafíos socioeconómicos en Guatemala, con muchas personas perdiendo sus empleos o enfrentando 
dificultades económicas debido a las restricciones implementadas para contener el virus. Esto ha afectado especialmente a 
comunidades vulnerables y sectores informales de la economía. La vacunación contra el COVID-19 ha sido una prioridad en 
Guatemala, al igual que en todo el mundo, buscando proteger a la población contra la enfermedad y reducir la gravedad de 
los casos.

La respuesta a la pandemia en Guatemala ha sido multifacética, involucrando no solo medidas de salud pública, sino también 
esfuerzos para abordar los impactos socioeconómicos y garantizar el acceso equitativo a la atención médica y a las vacunas. 
La colaboración entre el gobierno, las organizaciones de salud y la sociedad civil ha sido fundamental para enfrentar los 
desafíos planteados por el COVID-19 y trabajar hacia la recuperación integral del país. La investigación científica ha sido 
clave para entender la enfermedad y desarrollar vacunas y tratamientos eficaces.
"""

# Button to display additional information
if st.button('Información sobre COVID-19 en Guatemala'):
    st.write(info_text)

# Run code button
if st.button('Ejecutar Código'):
    st.write('**Visualización de Datos**')
    fig = plot_covid_data(data, A, u, r)
    st.plotly_chart(fig)


