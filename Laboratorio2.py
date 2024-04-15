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

# Button to display information
if st.button("Información sobre COVID-19 en Guatemala"):
    st.write(info_text)

# Button to show/hide code
if st.button("Ver código"):
    st.code("""
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
    
    # Display the plot
    st.plotly_chart(fig)
    """)
