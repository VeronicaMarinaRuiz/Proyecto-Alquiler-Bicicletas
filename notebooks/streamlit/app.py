import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import soporte as sp

# Función para nuestra animación
def load_lottieurl(url):
  r = requests.get(url)
  if r.status_code != 200:
    return None
  return r.json()

lottie_coding = load_lottieurl("https://lottie.host/3d70aeb0-1e6d-45ee-a406-10fd6b08d00b/akZviixXff.json")
imagen_video = Image.open("fotos/titulo_grupo.jpg")

with st.container():
  st.image(imagen_video)
  st.title("Bienvenido al estimador de bicicletas de Washington D. C.")
  st.subheader("Powered by SuperData 💻")
  st.write("Con este simulador podrás estimar cuantas bicicletas se van a alquilar en Washington D.C. dependiendo de las condiciones climática y el día de la semana.")

with st.container():
  st.write("---")
  left_column, right_column = st.columns(2)
  with left_column:
    st.header("¿Qué necesitamos?")
    st.write("Necesitamos que nos indiques en qué te quieres basar y posteriormente te pediremos unos datos para hacer la predicción.")
    st.write("[Tiempo en Whashinton D.C.](https://weather.com/weather/tenday/l/Washington+DC?canonicalCityId=4c0ca6d01716c299f53606df83d99d5eb96b2ee0efbe3cd15d35ddd29dee93b2)")
  with right_column:
    st_lottie(lottie_coding, height = 300, key = "coding")

with st.container():
  st.write("---")
  modelo = st.selectbox('¿Qué quieres predecir?',['Selecciona una opción','Clientes Casuales','Clientes Registrados', 'Clientes Totales'])
  if modelo == 'Clientes Casuales':
    estacion = st.selectbox('¿Qué estación quieres consultar?',['Selecciona una opción','invierno', 'primavera', 'verano', 'otoño'])
    año = st.text_input('¿Qué año quieres consultar?')
    mes = st.selectbox('¿Qué estación quieres consultar?',['Selecciona una opción','Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
       'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
    dia_semana = st.selectbox('¿Qué día de la semana quieres consultar?',['Selecciona una opción','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo'])
    dias_laborables = st.selectbox('¿Es laborable?',['Selecciona una opción','festivo', 'laborable', 'fin de semana'])
    tiempo = st.selectbox('¿Qué tiempo va a hacer?',['Selecciona una opción','nuboso', 'despejado', 'lluvioso'])
    temperatura = st.text_input('¿Qué temperatura hace (ºC)?')
    humedad = st.text_input('¿Qué humedad habrá (%)?')
    velocidad_viento = st.text_input('¿Qué velocidad tendrá el viento (km/h)?')
    if st.button('Predecir'):
      if estacion == 'Selecciona una opción' or año == '' or mes == 'Selecciona una opción' or dia_semana == 'Selecciona una opción' or dias_laborables == 'Selecciona una opción' or tiempo == 'Selecciona una opción' or temperatura == '' or humedad == '' or  velocidad_viento == '':
        pass
      else:
        prediccion = sp.prediccion_casuales(estacion,año,mes,dia_semana,dias_laborables,tiempo,temperatura,humedad,velocidad_viento)
        st.write(prediccion)

  elif modelo == 'Clientes Registrados':
    estacion = st.selectbox('¿Qué estación quieres consultar?',['Selecciona una opción','invierno', 'primavera', 'verano', 'otoño'])
    año = st.text_input('¿Qué año quieres consultar?')
    mes = st.selectbox('¿Qué estación quieres consultar?',['Selecciona una opción','Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
       'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
    dia_semana = st.selectbox('¿Qué día de la semana quieres consultar?',['Selecciona una opción','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo'])
    dias_laborables = st.selectbox('¿Es laborable?',['Selecciona una opción','festivo', 'laborable', 'fin de semana'])
    tiempo = st.selectbox('¿Qué tiempo va a hacer?',['Selecciona una opción','nuboso', 'despejado', 'lluvioso'])
    temperatura = st.text_input('¿Qué temperatura hace (ºC)?')
    humedad = st.text_input('¿Qué humedad habrá (%)?')
    velocidad_viento = st.text_input('¿Qué velocidad tendrá el viento (km/h)?')
    if st.button('Predecir'):
      if estacion == 'Selecciona una opción' or año == '' or mes == 'Selecciona una opción' or dia_semana == 'Selecciona una opción' or dias_laborables == 'Selecciona una opción' or tiempo == 'Selecciona una opción' or temperatura == '' or humedad == '' or  velocidad_viento == '':
        pass
      else:
        prediccion = sp.prediccion_registrados(estacion,año,mes,dia_semana,dias_laborables,tiempo,temperatura,humedad,velocidad_viento)
        st.write(prediccion)

  elif modelo == 'Clientes Totales':
    estacion = st.selectbox('¿Qué estación quieres consultar?',['Selecciona una opción','invierno', 'primavera', 'verano', 'otoño'])
    año = st.text_input('¿Qué año quieres consultar?')
    mes = st.selectbox('¿Qué estación quieres consultar?',['Selecciona una opción','Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio',
       'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'])
    dia_semana = st.selectbox('¿Qué día de la semana quieres consultar?',['Selecciona una opción','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo'])
    temperatura = st.text_input('¿Qué temperatura hace (ºC)?')
    humedad = st.text_input('¿Qué humedad habrá (%)?')
    velocidad_viento = st.text_input('¿Qué velocidad tendrá el viento (km/h)?')
    if st.button('Predecir'):
      if estacion == 'Selecciona una opción' or año == '' or mes == 'Selecciona una opción' or dia_semana == 'Selecciona una opción' or temperatura == '' or humedad == '' or  velocidad_viento == '':
        pass
      else:
        prediccion = sp.prediccion_total(estacion,año,mes,dia_semana,temperatura,humedad,velocidad_viento)
        st.write(prediccion)
