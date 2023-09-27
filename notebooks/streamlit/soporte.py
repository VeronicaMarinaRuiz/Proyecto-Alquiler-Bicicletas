# Tratamiento de datos
# -----------------------------------------------------------------------
import numpy as np
import pandas as pd

# Guardar transformers
import pickle


# Preprocesado
from sklearn.preprocessing import RobustScaler


#  Modelado y evaluación
# -----------------------------------------------------------------------------
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

metricas_cas = pd.read_pickle("../../datos_finales/predicciones/metricas_casuales.pkl")

df_casual_limpio = pd.read_pickle('../../datos_finales/predicciones/archivo_casual_est.pkl')

with open("../../datos_finales/predicciones/estandarizacion.pkl", "rb") as est:
    estandarizacion = pickle.load(est)

with open("../../datos_finales/predicciones/mejor_modelo_causal.pkl", "rb") as modelo:
    mejor_modelo_cas = pickle.load(modelo)

def prediccion_casuales(estacion,año,mes,dia_semana,dias_laborables,tiempo,temperatura,humedad,velocidad_viento):
    """Esta función hace la predicción de bicicletas registradas por los usuarios casuales

    Args:
        estacion (str): estación del año
        año (str): año
        mes (str): mes del año
        dia_semana (str): día de la semana
        dias_laborables (str): si el día ess laborable, fin de semana o festivo
        tiempo (str): si el tiempo es nuboso, lluvioso o despejado
        temperatura (str): temperatura en ºC
        humedad (str): humedad relativa en %
        velocidad_viento (_type_): velocidad del viento en km/h

    Returns: devuelve un string con la predicción
    """
    año = int(año)
    temperatura = int(temperatura)
    humedad = int(humedad)
    velocidad_viento = int(velocidad_viento)

    diccionario_aut = {'estacion':estacion,'año':año,'mes':mes,'dia_semana':dia_semana,
                       'dias_laborables':dias_laborables,'tiempo':tiempo,'temperatura':temperatura,
                       'humedad':humedad,'velocidad_viento':velocidad_viento}
    usuario = pd.DataFrame(diccionario_aut,index=[0])

    numericas = usuario.select_dtypes(include=np.number).drop('año',axis=1)
    numericas_robust = pd.DataFrame(estandarizacion.transform(numericas), columns = numericas.columns)
    usuario[numericas_robust.columns] = numericas_robust
    
    usuario.loc[0,'año'] = 1.47
    categoricas = df_casual_limpio.select_dtypes(include='O')

    for col in categoricas.columns:
        diccionario = {}
        df_mediana = df_casual_limpio.groupby(col)['usuarios_casuales'].median().reset_index().sort_values(by='usuarios_casuales')
        df_mediana['encoding'] = round(df_mediana['usuarios_casuales']/df_mediana.iloc[0,1], 2)
        for indice in range(df_mediana.shape[0]):
            diccionario[df_mediana.iloc[indice,0]] = df_mediana.iloc[indice,2]
        usuario[col] = usuario[col].map(diccionario)

    return f'La predicción de bicicletas alquiladas para ese día por los clientes casuales es entre {round(mejor_modelo_cas.predict(usuario)[0] + metricas_cas.loc[0,"RMSE"],0)} y {round(mejor_modelo_cas.predict(usuario)[0] - metricas_cas.loc[0,"RMSE"],0)}'


df_registrados_limpio = pd.read_pickle('../../datos_finales/predicciones/archivo_registrados_est.pkl')
with open("../../datos_finales/predicciones/mejor_modelo_registrados.pkl", "rb") as modelo:
    mejor_modelo_reg = pickle.load(modelo)
metricas_reg = pd.read_pickle("../../datos_finales/predicciones/metricas_registrados.pkl")


def prediccion_registrados(estacion,año,mes,dia_semana,dias_laborables,tiempo,temperatura,humedad,velocidad_viento):
    """Esta función hace la predicción de bicicletas registradas por los usuarios registrados

    Args:
        estacion (str): estación del año
        año (str): año
        mes (str): mes del año
        dia_semana (str): día de la semana
        dias_laborables (str): si el día ess laborable, fin de semana o festivo
        tiempo (str): si el tiempo es nuboso, lluvioso o despejado
        temperatura (str): temperatura en ºC
        humedad (str): humedad relativa en %
        velocidad_viento (_type_): velocidad del viento en km/h

    Returns: devuelve un string con la predicción
    """
    año = int(año)
    temperatura = int(temperatura)
    humedad = int(humedad)
    velocidad_viento = int(velocidad_viento)

    diccionario_aut = {'estacion':estacion,'año':año,'mes':mes,'dia_semana':dia_semana,
                       'dias_laborables':dias_laborables,'tiempo':tiempo,'temperatura':temperatura,
                       'humedad':humedad,'velocidad_viento':velocidad_viento}
    usuario = pd.DataFrame(diccionario_aut,index=[0])

    numericas = usuario.select_dtypes(include=np.number).drop('año',axis=1)
    numericas_robust = pd.DataFrame(estandarizacion.transform(numericas), columns = numericas.columns)
    usuario[numericas_robust.columns] = numericas_robust
    
    usuario.loc[0,'año'] = 1.47
    categoricas = df_registrados_limpio.select_dtypes(include='O')

    for col in categoricas.columns:
        diccionario = {}
        df_mediana = df_registrados_limpio.groupby(col)['usuarios_registrados'].median().reset_index().sort_values(by='usuarios_registrados')
        df_mediana['encoding'] = round(df_mediana['usuarios_registrados']/df_mediana.iloc[0,1], 2)
        for indice in range(df_mediana.shape[0]):
            diccionario[df_mediana.iloc[indice,0]] = df_mediana.iloc[indice,2]
        usuario[col] = usuario[col].map(diccionario)

    return f'La predicción de bicicletas alquiladas para ese día por los clientes registrados es entre {round(mejor_modelo_reg.predict(usuario)[0] + metricas_reg.loc[0,"RMSE"],0)} y {round(mejor_modelo_reg.predict(usuario)[0] - metricas_reg.loc[0,"RMSE"],0)}'

df_total_limpio = pd.read_pickle('../../datos_finales/predicciones/archivo_total_est.pkl')
with open("../../datos_finales/predicciones/mejor_modelo_total.pkl", "rb") as modelo:
    mejor_modelo_total = pickle.load(modelo)
metricas_total = pd.read_pickle("../../datos_finales/predicciones/metricas_totales.pkl")

def prediccion_total(estacion,año,mes,dia_semana,temperatura,humedad,velocidad_viento):
    """Esta función hace la predicción de bicicletas registradas por los usuarios totales

    Args:
        estacion (str): estación del año
        año (str): año
        mes (str): mes del año
        dia_semana (str): día de la semana
        temperatura (str): temperatura en ºC
        humedad (str): humedad relativa en %
        velocidad_viento (_type_): velocidad del viento en km/h

    Returns: devuelve un string con la predicción
    """
    año = int(año)
    temperatura = int(temperatura)
    humedad = int(humedad)
    velocidad_viento = int(velocidad_viento)

    diccionario_aut = {'estacion':estacion,'año':año,'mes':mes,'dia_semana':dia_semana,'temperatura':temperatura,
                       'humedad':humedad,'velocidad_viento':velocidad_viento}
    usuario = pd.DataFrame(diccionario_aut,index=[0])

    numericas = usuario.select_dtypes(include=np.number).drop('año',axis=1)
    numericas_robust = pd.DataFrame(estandarizacion.transform(numericas), columns = numericas.columns)
    usuario[numericas_robust.columns] = numericas_robust
    
    usuario.loc[0,'año'] = 1.47
    categoricas = df_total_limpio.select_dtypes(include='O').drop(['dias_laborables', 'tiempo'], axis = 1)

    for col in categoricas.columns:
        diccionario = {}
        df_mediana = df_total_limpio.groupby(col)['total_usuarios'].median().reset_index().sort_values(by='total_usuarios')
        df_mediana['encoding'] = round(df_mediana['total_usuarios']/df_mediana.iloc[0,1], 2)
        for indice in range(df_mediana.shape[0]):
            diccionario[df_mediana.iloc[indice,0]] = df_mediana.iloc[indice,2]
        usuario[col] = usuario[col].map(diccionario)
    
    return f'La predicción de bicicletas alquiladas para ese día por los clientes totales es entre {round(mejor_modelo_total.predict(usuario)[0] + metricas_total.loc[0,"RMSE"],0)} y {round(mejor_modelo_total.predict(usuario)[0] - metricas_total.loc[0,"RMSE"],0)}'