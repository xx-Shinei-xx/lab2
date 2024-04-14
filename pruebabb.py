import streamlit as st
import pandas as pd
from urllib.request import urlopen
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import json

from streamlit_lottie import st_lottie


<<<<<<< HEAD






=======
>>>>>>> 7a2fd2812fde7f7e292aac3b47df17c037cc6d4e
#Layout
st.set_page_config(
    page_title=Practica 1,
    layout=wide,
    initial_sidebar_state=expanded)



#Data Pull and Functions
st.markdown(
<style>
.big-font {
    font-size:80px !important;
}
</style>
, unsafe_allow_html=True)

@st.cache_data
def load_lottiefile(filepath: str):
    with open(filepath,r) as f:
        return json.load(f)

@st.cache_data
def pull_clean():
    master_zip=pd.read_csv('ConteoDeCarasPorParejas.csv',dtype={'ZCTA5': str})
    return master_zip



#Options Menu
with st.sidebar:
<<<<<<< HEAD
    selected = option_menu('Menu', [Intro, 'Graficas'], 
        icons=['comment-alt','stats'],menu_icon='intersect', default_index=0)
=======
    selected = option_menu('Menu', [Intro, 'Graficas', 'Distribucion binomial', 'Info'], 
        icons=['comment-alt','stats','info-circle'],menu_icon='intersect', default_index=0)
>>>>>>> 7a2fd2812fde7f7e292aac3b47df17c037cc6d4e
    lottie = load_lottiefile(digglet.json)
    st_lottie(lottie,key='loc')


#Intro Page
if selected==Intro:
<<<<<<< HEAD
    #Titulo Distribución binomial centrado con html
 st.markdown(
<style>
.big-title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    margin-top: 50px;
}
</style>
<div class=big-title>Laboratorio 1 Distribución Binomial</div>
, unsafe_allow_html=True)
 st.markdown(
<style>
.centered-italic {
    text-align: center;
    font-style: italic;
    font-size: 20px;
    margin-top: 5px;
}
</style>
<div class=centered-italic>This is some centered and italicized content.</div>
, unsafe_allow_html=True)
=======
    #Header
    st.title('Distribución Binomial')
   # ecuacion de la distribucion binomial https://es.wikipedia.org/wiki/Distribuci%C3%B3n_binomial
    st.latex(r'''
    P(X = k) = \binom{n}{k} \cdot p^k \cdot (1 - p)^{n - k}
    ''')
>>>>>>> 7a2fd2812fde7f7e292aac3b47df17c037cc6d4e

<<<<<<< HEAD
 st.divider()
=======

    st.divider()
>>>>>>> 6b45c4fc394bddcdf3df55cc0c87ae797e571483


  

    #Use Cases
 with st.container():
        col1,col2=st.columns(2)
#Columna 1 de introducción        
        with col1:
            st.markdown(
<style>
.big-title {
    text-align: center;
    font-size: 36px;
    margin-top: 5px;
}
</style>
<div class=big-title>Resumen</div>
, unsafe_allow_html=True)
            st.markdown(
<<<<<<< HEAD
<<<<<<< HEAD
                
                La distribución binomial es una función que describe la probabilidad de obtener un número específico de éxitos
                  en un número fijo de casos independientes. La distribuión binomial es ideal en casos en donde se analice el resultado de un número pequeño de posibles estados finales
                )
            st.markdown(
<style>
.big-title {
    text-align: center;
    font-size: 36px;
    margin-top: 5px;
}
</style>
<div class=big-title>Objetivos</div>
, unsafe_allow_html=True)
            st.subheader('Generales')
            st.markdown(
                
                - Comprobar experimental y teóricamente el conoimiento de probabilidades 
                
                
                )
            st.subheader('Específicos')
            st.markdown(
                
                - Verificar le toeria de la distribución binomial
                - Verificar que los datos obtenidos experimentalmente sigan un comportamiento ¿binomial? xd
                
                )
#Columna dos de introducción       
=======
                 
=======
                
>>>>>>> 6b45c4fc394bddcdf3df55cc0c87ae797e571483
                Una distribución binomial es un modelo matemático que representa la probabilidad de obtener cierta cantidad de
                éxitos en un número fijo de intentos independientes, donde cada intento solo puede tener dos resultados posibles: éxito o fracaso.
                Cada intento se considera independiente entre sí y la probabilidad de éxito en cada uno permanece constante.
                
                )
            st.header('Objetivos')
<<<<<<< HEAD
        # Lista de objetivos generales
objetivos_generales = [
    Determinar probabilidades particulares relacionadas con el número de éxitos.,
    Aplicar la distribución binomial en la toma de decisiones.
]

# Convertir los objetivos en una lista HTML
objetivos_html = <ul> + .join([f<li>{objetivo}</li> for objetivo in objetivos_generales]) + </ul>

# Mostrar los objetivos generales
st.markdown(f### Objetivos generales:\n{objetivos_html}, unsafe_allow_html=True) 

        
#Evaluar la precisión de modelos y experimentos mediante la distribución binomial.,
            #-----------------------------------------------
>>>>>>> 7a2fd2812fde7f7e292aac3b47df17c037cc6d4e
=======
            st.markdown(
                
                asdddddddddddddddddddd
                
                )
            
>>>>>>> 6b45c4fc394bddcdf3df55cc0c87ae797e571483
        with col2:
             st.markdown(
              <style>
             .big-title {
             text-align: center;
              font-size: 36px;
               margin-top: 5px;
               }
              </style>
             <div class=big-title>Marco teorico</div>
            , unsafe_allow_html=True)
             st.subheader('Coeficiente Binomial')
             st.markdown(
                
                El coeficiente binomial indica el numero de subconjuntos 
                de k elementos escogidos de un conjunto de n elementos totales. Puede ser calculado de la siguiene manera
                
                )
             st.latex(r'''\binom{n}{k}= \frac{n!}{k!(n-k)!}''')
             st.subheader('Distribución Binomial')
             st.markdown(La distribución Binomial, llamada así por el coeficiente binomial, permite describir la probabilidad de observar una cantidad de éxitos en una cantidad de intentos, considerando la probabilidad individual de éxito de cada intento. Específicamente, estas características se dividen en las siguientes variables: )
             st.markdown( 
                        - Número de ensayos (n): Representa el número total de ensayos o experimentos. 
                        - Probabilidad de éxito (p): Es la probabilidad de que ocurra un éxito en un solo ensayo. 
                        - Número de éxitos (x): Es la variable discreta que representa el número de éxitos que se observan en los n ensayos.
)
             st.latex(r'''P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}''')

             st.markdown(
              <style>
             .big-title {
              text-align: center;
             font-size: 36px;
             margin-top: 5px;
               }
             </style>
             <div class=big-title>Conclusiones</div>
            , unsafe_allow_html=True)
             st.markdown(
                
                asdddddddddddddddddddd
                )

    

    




    
#Search Page
if selected=='Graficas':
    # Set up the Streamlit ap

 # Add a title to the app
 st.title(CSV File Viewer)

# Add a file uploader to the app
 

 df = pd.read_csv(ConteosDeCarasPorPareja.csv)
  # Display the DataFrame in Streamlit
 st.dataframe(df)

   # Display some statistics about the DataFrame
 st.write(fThe DataFrame has {len(df)} rows and {len(df.columns)} columns.)
<<<<<<< HEAD
=======



#---------------------------------------------------------------
# Grafica
#if selected=='Distribucion binomial':

#def leer_archivo_py():
#    try:
 #       with open(Practica1.py, r) as archivo:
 #           contenido = archivo.read()
#            st.text_area(Contenido del archivo, contenido)
#    except FileNotFoundError:
#        st.error(El archivo no fue encontrado.)

#def main():
 #   st.title(aaaaa)
#    st.write(sdasdasdasd.)

 #   leer_archivo_py()
#if __name__ == __main__:
 #   main()

#-----------------------------------------------------------------
    
  

 
#About Page
if selected=='Info': 
    st.title('Datos')
    st.markdown(
                
                asdasdasdsaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
                )

>>>>>>> 7a2fd2812fde7f7e292aac3b47df17c037cc6d4e
