import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Define Gaussian function
def gaussian(x, A, u, r):
    return A * np.exp(-((x - u) / r) ** 2 / 2)

# Define function to plot COVID-19 data with Gaussian fit
def plot_covid_data(data, A, u, r):
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

# Load data from datos1.csv
data1 = pd.read_csv('datos1.csv')
A1 = 465.464
u1 = 89.2538
r1 = 7.13597

# Load data from datos2.csv
data2 = pd.read_csv('datos2.csv')
A2 = 1062.39
u2 = 139.803
r2 = 35.1769

# Create Streamlit app
st.title('Visualización Interactiva de Datos COVID-19')

# Sidebar for Gaussian fit parameters
st.sidebar.title('Parámetros de Ajuste Gaussiano')

# Sidebar sliders for data1
st.sidebar.subheader('Primer conjunto de datos')
A_slider1 = st.sidebar.slider('Amplitud (A)', min_value=0.0, max_value=1000.0, value=A1, step=10.0)
u_slider1 = st.sidebar.slider('Media (u)', min_value=0.0, max_value=100.0, value=u1, step=1.0)
r_slider1 = st.sidebar.slider('Desviación estándar (r)', min_value=0.0, max_value=20.0, value=r1, step=0.1)

# Sidebar sliders for data2
st.sidebar.subheader('Segundo conjunto de datos')
A_slider2 = st.sidebar.slider('Amplitud (A)', min_value=0.0, max_value=2000.0, value=A2, step=10.0)
u_slider2 = st.sidebar.slider('Media (u)', min_value=0.0, max_value=200.0, value=u2, step=1.0)
r_slider2 = st.sidebar.slider('Desviación estándar (r)', min_value=0.0, max_value=40.0, value=r2, step=0.1)

# Display COVID-19 information toggle button
info_button_state = st.button('Mostrar Información sobre COVID-19')

if info_button_state:
    st.subheader('Resumen')

    # Create expandable sections for different parts of the summary
    with st.expander('Marco Teórico'):
        st.write("""
        El COVID-19, derivado de "Coronavirus Disease 2019", es una afección respiratoria provocada por el virus SARS-CoV-2, perteneciente a la familia de los coronavirus, que también incluye el SARS-CoV y el MERS-CoV. La principal vía de transmisión del SARS-CoV-2 es de persona a persona a través de gotas respiratorias expulsadas al toser, estornudar, hablar o respirar, aunque también puede propagarse por contacto con superficies u objetos contaminados con el virus y luego tocarse la boca, la nariz o los ojos.

En Guatemala, al igual que en muchos otros países, el COVID-19 ha tenido un impacto significativo en la salud pública y en la sociedad en general. Desde el inicio de la pandemia, el país ha experimentado un número considerable de casos confirmados de COVID-19, detectados mediante pruebas de laboratorio como PCR y pruebas rápidas de antígenos. La transmisión comunitaria del virus ha sido especialmente desafiante en áreas urbanas densamente pobladas de Guatemala, llevando a un aumento en la carga de casos en hospitales y centros de salud, poniendo a prueba la capacidad del sistema de salud guatemalteco.

El gobierno guatemalteco ha implementado diversas medidas para prevenir la propagación del virus, incluyendo cuarentenas, toques de queda y el uso obligatorio de mascarillas. Asimismo, se han llevado a cabo campañas de vacunación masiva como parte de las estrategias de control. La disponibilidad de camas de hospital, equipos médicos y personal sanitario ha sido un problema en algunos momentos de la pandemia, lo que ha puesto a prueba la capacidad del sistema de salud guatemalteco.

La pandemia ha exacerbado los desafíos socioeconómicos en Guatemala, con muchas personas perdiendo sus empleos o enfrentando dificultades económicas debido a las restricciones implementadas para contener el virus. Esto ha afectado especialmente a comunidades vulnerables y sectores informales de la economía. La vacunación contra el COVID-19 ha sido una prioridad en Guatemala, al igual que en todo el mundo, buscando proteger a la población contra la enfermedad y reducir la gravedad de los casos.

La respuesta a la pandemia en Guatemala ha sido multifacética, involucrando no solo medidas de salud pública, sino también esfuerzos para abordar los impactos socioeconómicos y garantizar el acceso equitativo a la atención médica y a las vacunas. La colaboración entre el gobierno, las organizaciones de salud y la sociedad civil ha sido fundamental para enfrentar los desafíos planteados por el COVID-19 y trabajar hacia la recuperación integral del país. La investigación científica ha sido clave para entender la enfermedad y desarrollar vacunas y tratamientos eficaces.

        """)

    with st.expander('Objetivos Generales'):
        st.write("""
        Aplicar técnicas estadísticas para modelar la evolución de casos de COVID-19 en Guatemala hasta una fecha en específico utilizando datos del Ministerio de Salud, mediante el ajuste de una distribución binomial y la realización de predicciones.
        """)

    with st.expander('Objetivos Específicos'):
        st.write("""
        - Recolectar datos históricos: Obtener datos precisos de casos de COVID-19 del Ministerio de Salud de Guatemala.
        - Modelar con distribución binomial: Representar el número de nuevos casos diarios como una distribución binomial.
        - Hacer predicciones futuras: Utilizar el modelo ajustado para prever la cantidad esperada de nuevos casos después del 15 de marzo de 2021.
        """)

    with st.expander('Conclusiones'):
        st.write("""
        - El ajuste de una distribución binomial permitió estimar la probabilidad diaria de nuevos casos y el número total de días en el modelo, brindando información valiosa para las predicciones.
        - Las predicciones ofrecen una visión proyectiva de la evolución esperada de la pandemia, facilitando la planificación de intervenciones futuras.
        - La vigilancia epidemiológica continua y la recopilación de datos precisos son esenciales para mejorar la precisión de los modelos y respaldar decisiones basadas en evidencia en la gestión de la pandemia.
        """)
    
# Run code button to display visualizations
run_button_state = st.button('Ejecutar Código')

if run_button_state:
    st.write('**Visualización de Datos**')

    # Plot data1
    st.subheader('Primer conjunto de datos')
    fig1 = plot_covid_data(data1, A_slider1, u_slider1, r_slider1)
    st.plotly_chart(fig1)

    # Plot data2
    st.subheader('Segundo conjunto de datos')
    fig2 = plot_covid_data(data2, A_slider2, u_slider2, r_slider2)
    st.plotly_chart(fig2)

