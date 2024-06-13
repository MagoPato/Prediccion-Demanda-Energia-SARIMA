<h1>Predicción de la Demanda de Energía Eléctrica con SARIMA</h1>

<p>Este proyecto utiliza un modelo SARIMA para predecir la demanda de energía eléctrica. Los datos se procesan utilizando <code>pandas</code> y el modelo se ajusta con <code>statsmodels</code>.</p>

<h2>Requisitos</h2>
<ul>
    <li>Python 3.x</li>
    <li>numpy</li>
    <li>pandas</li>
    <li>statsmodels</li>
    <li>matplotlib</li>
</ul>

<p>Puedes instalar las dependencias necesarias usando el siguiente comando:</p>

<pre><code>pip install numpy pandas statsmodels matplotlib</code></pre>

<h2>Uso</h2>
<ol>
    <li>Clona el repositorio:
        <pre><code>git clone https://github.com/tu-usuario/Prediccion-Demanda-Energia-SARIMA.git
cd Prediccion-Demanda-Energia-SARIMA</code></pre>
    </li>
    <li>Ejecuta el script:
        <pre><code>python prediccion_demanda_energia.py</code></pre>
    </li>
</ol>

<h2>Descripción del Proyecto</h2>
<p>El script realiza los siguientes pasos:</p>
<ol>
    <li><strong>Carga y procesamiento de datos:</strong> Se cargan los datos históricos de demanda de energía y se procesan para adecuarlos al modelo.</li>
    <li><strong>Ajuste del modelo SARIMA:</strong> Se ajusta un modelo SARIMA a los datos históricos.</li>
    <li><strong>Generación de predicciones:</strong> Se generan predicciones para futuros periodos usando el modelo ajustado.</li>
    <li><strong>Visualización de resultados:</strong> Se grafican los datos observados y las predicciones.</li>
</ol>

<h2>Datos</h2>
<p>Los datos utilizados en este proyecto están contenidos dentro del script y representan la demanda de energía eléctrica en kW para diferentes periodos. A continuación, se muestra una tabla con algunos ejemplos de los datos:</p>

<table align="center" border="1">
    <tr>
        <th>Periodo</th>
        <th>DemandakW</th>
        <th>CTkWh</th>
        <th>FP%</th>
        <th>FC%</th>
        <th>PM(MXN)</th>
    </tr>
    <tr>
        <td>2022-02</td>
        <td>140</td>
        <td>22.317</td>
        <td>99.98</td>
        <td>24</td>
        <td>2.662</td>
    </tr>
    <tr>
        <td>2022-03</td>
        <td>147.6</td>
        <td>28.59</td>
        <td>99.93</td>
        <td>30.17</td>
        <td>2.606</td>
    </tr>
    <tr>
        <td>2022-04</td>
        <td>37.6</td>
        <td>485.5</td>
        <td>100</td>
        <td>57.17</td>
        <td>2.1152</td>
    </tr>
    <tr>
        <td>2022-04</td>
        <td>143.9</td>
        <td>20.45</td>
        <td>99.72</td>
        <td>24.17</td>
        <td>2.6301</td>
    </tr>
    <tr>
        <td>2022-05</td>
        <td>156.1</td>
        <td>39.01</td>
        <td>99.45</td>
        <td>37.17</td>
        <td>2.6745</td>
    </tr>
</table>

<h2>Ejemplo de Visualización</h2>
<p>A continuación, se muestran ejemplos de las visualizaciones generadas por el script:</p>
<div align="center">
<h3 align="center" >Datos Reales</h3>
<img src="https://github.com/MagoPato/Prediccion-Demanda-Energia-SARIMA/blob/main/datos_real.png?raw=true" alt="Datos Observados" width="650">
<h3 align="center" >Predicciones SARIMA</h3>
<img src="https://github.com/MagoPato/Prediccion-Demanda-Energia-SARIMA/blob/main/datos_predecidos.png?raw=true" alt="Predicciones SARIMA" width="650">
</div>
<h2>Conclusión</h2>
<p>La predicción de la demanda de energía eléctrica es crucial para gestionar de manera eficiente los recursos energéticos. En este proyecto, utilizando un modelo SARIMA, se logró predecir la demanda futura con base en datos históricos. Un hallazgo interesante fue que el consumo de energía ha aumentado con el tiempo, lo que inicialmente parecía estar correlacionado con el aumento en el número de alumnos en la institución. Sin embargo, considerando que el número de salones no ha cambiado, se concluyó que este incremento en la demanda se debe probablemente a una falla en algún lugar del sistema, falta de mantenimiento en las subestaciones eléctricas, uso incrementado de dispositivos eléctricos como climas o minisplits, o a otros factores similares. Identificar y resolver estos problemas es esencial para evitar aumentos innecesarios en el consumo de energía.</p>
