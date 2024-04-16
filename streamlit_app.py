import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Función para ajustar una distribución gaussiana
def gaussian(x, A, u, r):
    return A * np.exp(-((x - u) / r) ** 2 / 2)

# Función para mostrar gráficos de datos COVID-19 con ajuste gaussiano
def plot_covid_data(data, A, u, r):
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

# Función para mostrar la imagen de carga
def show_loading_image():
    # Mostrar la imagen de carga con CSS y JavaScript
    st.markdown(
        """
        <style>
        /* Estilos para el div de la imagen de carga */
        #loading-image-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: white;
            z-index: 9999; /* Asegura que esté en la parte superior */
            display: flex;
            justify-content: center;
            align-items: center;
        }
        /* Estilos para la imagen de carga */
        #loading-image {
            width: 80%; /* Ajusta el tamaño de la imagen según sea necesario */
            height: auto;
            max-height: 80%; /* Limita la altura para asegurar que se vea bien */
        }
        </style>
        """
    )

    # Mostrar el div con la imagen de carga
    st.markdown(
        """
        <div id="loading-image-container">
            <img id="loading-image" src="https://example.com/your-image.jpg">
        </div>
        """,
        unsafe_allow_html=True
    )

    # Ejecutar código JavaScript para ocultar la imagen después de unos segundos
    st.markdown(
        """
        <script>
        setTimeout(function() {
            document.getElementById('loading-image-container').style.display = 'none';
        }, 3000);  // Oculta la imagen después de 3 segundos (3000 milisegundos)
        </script>
        """,
        unsafe_allow_html=True
    )

# Aplicación Streamlit
def main():
    # Llama a la función para mostrar la imagen de carga
    show_loading_image()

    # Encabezado y título de la aplicación
    st.title('Visualización Interactiva de Datos COVID-19')

    # Botones para mostrar información y código
    show_info_button = st.button('Mostrar Información sobre COVID-19')
    show_code_button = st.button('Ver Código')

    # Mostrar información sobre COVID-19 si se presiona el botón correspondiente
    if show_info_button:
        st.subheader('Resumen - Información sobre COVID-19')
        st.write("""
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
        """)

    # Mostrar código si se presiona el botón correspondiente
    if show_code_button:
        st.subheader('Código Fuente')
        st.code("""
        import pandas as pd
        import streamlit as st
        import plotly.graph_objects as go
        import numpy as np
        import matplotlib

        # Configura Matplotlib para un backend no interactivo
        matplotlib.use('agg')  # Utiliza el backend 'agg' (renderizado de imagen)
        import matplotlib.pyplot as plt

        # Funciones y código aquí
        """)

    # Mostrar gráficos fuera de los expanders
    st.subheader('Visualización de Datos')

    # Gráfico para datos1
    st.subheader('Primer conjunto de datos')
    fig1 = plot_covid_data(data1, A1, u1, r1)
    st.plotly_chart(fig1)

    # Gráfico para datos2
    st.subheader('Segundo conjunto de datos')
    fig2 = plot_covid_data(data2, A2, u2, r2)
    st.plotly_chart(fig2)

# Llama a la función principal
if __name__ == '__main__':
    main()

