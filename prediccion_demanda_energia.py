
import numpy as np
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

data_modificada = [
    "Periodo,DemandakW,CTkWh,FP%,FC%,PM(MXN)",
    "2023-02,140,22.317,99.98,24,2.662",
    "2023-03,157,30.138,99.91,26,2.606",
    "2023-04,40,512,99.98,53,2.1152",
    "2023-04,153,21.578,99.7,20,2.6301",
    "2023-05,166,41.115,99.43,33,2.6745",
    "2023-06,166,44.724,99,37,2.7586",
    "2023-07,105,2.754,99,35,2.7209",
    "2023-08,236,532,99.26,30,2.7365",
    "2023-09,239,65.878,99.43,38,2.7464",
    "2023-10,203,36.498,99.62,27,2.7071",
    "2023-10,55,2.062,99.99,52,2.6259",
    "2023-11,123,23.209,99.98,26,2.6754",
    "2023-12,51,17.491,100,46,2.5765",
    "2024-01,81,19.423,99.99,32,2.6126",
    "2024-02,149,23.505,99.96,23,2.7489"
]

# Datos
data = [
    "Periodo,DemandakW,CTkWh,FP%,FC%,PM(MXN)",
    "2022-02,140,22.317,99.98,24,2.662",
    "2022-03,147.6,28.59,99.93,30.17,2.606",
    "2022-04,37.6,485.5,100,57.17,2.1152",
    "2022-04,143.9,20.45,99.72,24.17,2.6301",
    "2022-05,156.1,39.01,99.45,37.17,2.6745",
    "2022-06,166,44.724,99,37,2.7586",
    "2022-07,105,2.754,99,35,2.7209",
    "2022-08,236,532,99.26,30,2.7365",
    "2022-09,224.9,62.53,99.45,42.17,2.7464",
    "2022-10,191.1,34.62,99.64,31.17,2.7071",
    "2022-10,51.8,1.96,100.01,56.17,2.6259",
    "2022-11,115.8,22.01,100,30.17,2.6754",
    "2022-12,48.0,16.59,100.02,50.17,2.5765",
    "2023-01,76.3,18.42,100.01,36.17,2.6126",
    "2023-02,140,22.317,99.98,24,2.662",
    "2023-03,157,30.138,99.91,26,2.606",
    "2023-04,40,512,99.98,53,2.1152",
    "2023-04,153,21.578,99.7,20,2.6301",
    "2023-05,166,41.115,99.43,33,2.6745",
    "2023-06,166,44.724,99,37,2.7586",
    "2023-07,105,2.754,99,35,2.7209",
    "2023-08,236,532,99.26,30,2.7365",
    "2023-09,239,65.878,99.43,38,2.7464",
    "2023-10,203,36.498,99.62,27,2.7071",
    "2023-10,55,2.062,99.99,52,2.6259",
    "2023-11,123,23.209,99.98,26,2.6754",
    "2023-12,51,17.491,100,46,2.5765",
    "2024-01,81,19.423,99.99,32,2.6126",
    "2024-02,149,23.505,99.96,23,2.7489"
]

# Convertir a DataFrame y ajustar tipos de datos
data_list = [line.split(",") for line in data[1:]]
df = pd.DataFrame(data_list, columns=data[0].split(","))
df["DemandakW"] = pd.to_numeric(df["DemandakW"])

# Convertir la columna "Periodo" a formato de fecha y hora
df["Periodo"] = pd.to_datetime(df["Periodo"], errors='coerce', format='%Y-%m')

# Eliminar filas con valores de fecha y hora no válidos
df = df.dropna(subset=['Periodo'])

# Establecer la columna "Periodo" como índice
df.set_index("Periodo", inplace=True)

# Ajustar un modelo SARIMA
modelo_sarima = ARIMA(df["DemandakW"], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
modelo_sarima_ajustado = modelo_sarima.fit()

# Generar predicciones para los próximos 150 periodos
predicciones_sarima = modelo_sarima_ajustado.predict(start=len(df), end=len(df)+35, dynamic=False)

# Generar rangos de fechas para los períodos futuros
fechas_futuras = pd.date_range(start=df.index[-1], periods=len(predicciones_sarima)+1, freq='M')[1:]

# Crear DataFrame con las fechas y las predicciones
predicciones_df = pd.DataFrame(predicciones_sarima.values, index=fechas_futuras, columns=["Predicciones"])

# Mostrar las predicciones
print(predicciones_df)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(df.index, df["DemandakW"], label="Observado")
plt.xlabel("Periodo")
plt.ylabel("Consumo Total kWh")
plt.title("Predicción de la demanda de energía eléctrica con SARIMA")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()


# Graficar
plt.figure(figsize=(10, 6))
plt.plot(df.index, df["DemandakW"], label="Observado")
plt.plot(predicciones_df.index, predicciones_df["Predicciones"], label="Predicciones SARIMA", color='red')
plt.xlabel("Periodo")
plt.ylabel("Consumo Total kWh")
plt.title("Predicción de la demanda de energía eléctrica con SARIMA")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

