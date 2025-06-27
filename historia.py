import streamlit as st
import json
import analysis 
from analysis import sismos_mensualidad_2024, evolucion_mensual_por_zona_2024, evolucion_mensual_días_2024


with open("anuales.json","r",encoding='utf-8')as file:
    data=json.load(file)

#configura los detalles de la página
st.set_page_config(
    page_title="GeodataCuba",
    page_icon="🌋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Todo el CSS que hace bonita la página :D
st.markdown("""
<style>
    /* Fuentes bonitas para que se vea profesional */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700&family=Source+Sans+3:wght@300;400;600&display=swap');
    
    /* Los colores principales que elegimos */
    :root {
        --primary: #6B352C;
        --primary-dark: #5a2b24;
        --primary-light: #8B4513;
        --light-bg: #f8f5f2;
        --card-bg: #ffffff;
    }
    
    /* Estilo general de texto */
    * {
        font-family: 'Source Sans 3', sans-serif;
    }
    
    /* Títulos con otra fuente */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Montserrat', sans-serif;
        color: var(--primary);
    }
    
    body {
        background-color: var(--light-bg);
    }
    
    /* Barra lateral con color */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--primary) 0%, var(--primary-dark) 100%);
        color: white;
        padding: 1.5rem 1rem;
    }
    
    .sidebar-title {
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 2rem;
    }
    
    .sidebar-item {
        padding: 0.8rem 1rem;
        border-radius: 6px;
        margin-bottom: 0.5rem;
        cursor: pointer;
    }
    
    .sidebar-item:hover {
        background-color: rgba(255, 255, 255, 0.1);
    }
    
    .sidebar-item.active {
        background-color: rgba(255, 255, 255, 0.15);
        font-weight: 600;
    }
    
    /* Contenedor principal */
    .main-container {
        padding: 2rem 3rem;
    }
    
    /* Tarjetas que se ven modernas */
    .card-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 1.5rem;
        margin-bottom: 2.5rem;
    }
    
    .card {
        background-color: var(--card-bg);
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(107, 53, 44, 0.1);
        overflow: hidden;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(107, 53, 44, 0.15);
    }
    
    .card-header {
        background: linear-gradient(90deg, var(--primary) 0%, var(--primary-light) 100%);
        color: white;
        padding: 1.2rem;
    }
    
    .card-body {
        padding: 1.5rem;
    }
    
    /* Estadísticas grandes */
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1.5rem;
        margin-bottom: 2.5rem;
    }
    
    .stat-card {
        background-color: var(--card-bg);
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
    }
    
    .stat-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--primary);
    }
    
    /* Tabla con estilo */
    .data-table {
        width: 100%;
        border-collapse: collapse;
        background-color: var(--card-bg);
        border-radius: 10px;
        overflow: hidden;
    }
    
    .data-table th {
        background-color: var(--primary);
        color: white;
        padding: 1rem;
    }
    
    .data-table td {
        padding: 0.9rem 1rem;
        border-bottom: 1px solid #eeeeee;
    }
    
    .data-table tr:hover td {
        background-color: #f9f5f2;
    }
    
    /* Pie de página */
    .app-footer {
        text-align: center;
        padding: 2rem 0;
        margin-top: 3rem;
        color: #777777;
        border-top: 1px solid #e0e0e0;
    }
</style>
""", unsafe_allow_html=True)
c1,c2=st.columns([2,2])
st.title("¿Puede ocurrir un tsunami en Cuba? La historia que revelaron los datos del sismo de 2024")

st.title("Presentado por:")
st.image("Extra/GeoData.png")

with st.sidebar:
    st.image("Extra/GeoData.png", use_container_width=True)        
    st.sidebar.markdown("## 📖 Índice ")
    st.sidebar.markdown("- [Inicio](#Inicio)")
    st.sidebar.markdown("- [Contexto Geológico](#Contexto)")
    st.sidebar.markdown("- [La pregunta sobre tsunami](#tsunami)")
    st.sidebar.markdown("- [Actividad sísmica excepcional](#actividad)")
    st.sidebar.markdown("- [Visualizaciones: Patrones sísmicos](#visualizaciones)")
    st.sidebar.markdown("- [Días clave](#dias)")
    st.sidebar.markdown("- [Análisis: ¿Tsunami o no?](#analisis)")
    st.sidebar.markdown("- [Zonas vulnerables](#zonas)")
    st.sidebar.markdown("- [Antecedentes históricos](#historia_caribe)")
    st.sidebar.markdown("- [Testimonios](#testimonios)")
    st.sidebar.markdown("- [Respuesta institucional](#respuesta)")
    st.sidebar.markdown("- [Los números de 2024](#numeros)")
    st.sidebar.markdown("- [Respuesta científica](#respuesta_final)")
    st.sidebar.markdown("- [Epílogo](#epilogo)")

st.markdown("<a id='Inicio'></a>", unsafe_allow_html=True)
st.header("")
st.header("La mañana que cambió la perspectiva científica")

st.markdown("**10 de noviembre de 2024, 11:49 de la mañana...**")
st.markdown("""En Santiago de Cuba, los científicos del Centro Nacional de Investigaciones 
Sismológicas (CENAIS) observaban sus monitores con una mezcla de 
fascinación y preocupación. Las señales que llegaban desde la red de 
estaciones sísmicas no dejaban dudas: algo extraordinario estaba ocurriendo 
en las profundidades de la falla Septentrional-Oriente""") 
c1,c2,c3=st.columns([1,2,1])
with c2:
    st.image("Extra/Cientifico.png")  
st.markdown("""Mientras miles de cubanos almorzaban o trabajaban en sus rutinas 
dominicales, la tierra decidió recordarles que bajo sus pies se esconde una de 
las zonas tectónicamente más activas del Caribe. Un sismo de magnitud 6.7 
(el más fuerte registrado en Cuba en 2024)  sacudió la isla desde Bartolomé 
Masó, en la costa suroriental""")

st.image("Extra/Bartolome-Masó.png", use_container_width=True)

st.markdown("""Pero este evento tenía algo diferente. Una hora antes, a las 10:50 de la mañana, 
un precursor sísmico ya había hecho saltar las alarmas en el observatorio. Los 
científicos sabían que algo significativo se aproximaba, pero nadie imaginaba 
que estaban presenciando el inicio de la secuencia sísmica más intensa 
registrada en Cuba en décadas, pero para poder describir el fenómeno, debemos comprender primero el contexto geológico de Cuba""")

st.markdown("<a id='Contexto'></a>", unsafe_allow_html=True)
st.header("Contexto Geolólico")

st.markdown("""Desde el punto de vista geodinámico, el archipiélago cubano forma parte de la placa de Norteamérica, próximo al límite con la microplaca de Gonave. 
Este límite lo constituye la falla Oriente, situada al sur de la región oriental de Cuba, zona donde se registró la actividad anómala.
Aquí  se pone de manifiesto un proceso transpresivo tipo flower, manifestado por un predominio de fallas inversas. Este proceso transpresivo ha ocasionado el levantamiento del fondo marino, denominado Cinturón Deformado de Santiago de Cuba.""")

with st.expander("¿Quieres saber en que consiste este proceso?"):
    st.write("Se trata de un proceso tectónico donde una falla transpresiva (combinación de deslizamiento horizontal y compresión) genera una estructura en flor, caracterizada por múltiples fallas secundarias que se ramifican, similar a los pétalos de una flor.")
b1,b2=st.columns([2,2])
with b1:
    st.image("Extra/contexto.png")
with b2:
    st.markdown("""Esta estructura tectónica representa una de las zonas más activas del sistema 
de fallas cubano, donde la energía acumulada durante décadas se libera 
súbitamente en forma de terremotos. En las horas siguientes al sismo principal, 
los datos comenzaron a revelar una secuencia sísmica intensa que se 
extendería durante semanas
""")

st.markdown("")
st.markdown("""Cuando los números cuentan una historia

En los días siguientes, mientras los equipos de emergencia evaluaban los
daños materiales - más de 3,700 edificaciones afectadas, 156 viviendas con
colapsos parciales, 10 personas heridas levemente - los científicos del CENAIS
comenzaron a procesar una información que cambiaría para siempre la
perspectiva sobre el riesgo tsunamigénico en Cuba.
El primer dato que saltó a la vista fue la intensidad de las réplicas. Conforme
avanzaba noviembre, los números revelaron que 2024 registraría 10,795
terremotos en territorio cubano, con una concentración particular de eventos
durante este mes. No se trataba solo de un sismo fuerte: los datos mostraban
una secuencia sísmica de características excepcionales en la falla
Septentrional-Oriente.
""")
st.markdown("<a id='tsunami'></a>", unsafe_allow_html=True)
st.header("La pregunta que cambió de respuesta")
st.markdown("""
Durante años, cuando alguien preguntaba si podía ocurrir un tsunami en Cuba,
la respuesta científica era técnicamente correcta pero insatisfactoria: "Es muy
poco probable, pero no imposible". Una respuesta que dejaba más dudas que
certezas.

Los eventos de 2024 proporcionaron nuevos datos cruciales para el análisis del
riesgo tsunamigénico. Por primera vez, la secuencia sísmica ofreció
información detallada sobre el comportamiento de la falla Septentrional-Oriente
y sus implicaciones reales para la seguridad costera.
""")
st.markdown("<a id='actividad'></a>", unsafe_allow_html=True)
st.header("Un año de actividad sísmica excepcional")
st.markdown("""
Los datos consolidados del CENAIS mostraron una cifra que redefinió la
comprensión del fenómeno: 10,795 terremotos registrados en territorio
cubano durante 2024. Esta actividad sísmica intensa se concentró
principalmente en la región de Pilón-Chivirico y alcanzó su pico máximo
durante el mes de noviembre, cuando se registraron 7,337 sismos – más del
67% de toda la actividad anual.

La distribución temporal y espacial de estos sismos proporcionó información
invaluable sobre el comportamiento de las estructuras tectónicas activas en la
región suroriental de Cuba, revelando patrones que los científicos no habían
observado anteriormente con esta claridad.
""")
st.markdown("<a id='visualizaciones'></a>", unsafe_allow_html=True)
st.header("La historia que cuentan las visualizaciones: Patrones que revelan la realidad sísmica")

st.subheader("Noviembre 2024: Cuando la falla decidió hablar")
# Gráfico de barras mensual
fig_mensual = sismos_mensualidad_2024(data)
st.plotly_chart(fig_mensual, use_container_width=True)

st.markdown("""
Los números cuentan una historia extraordinaria. Noviembre de 2024 no fue un
mes cualquiera: concentró 7,337 sismos – más del 67% de toda la actividad
sísmica anual comprimida en apenas 30 días. Mientras septiembre, el segundo
mes más activo, registró 800 eventos, y el resto del año se mantuvo por debajo
de los 400 sismos mensuales, noviembre sobresale como una anomalía
estadística que cambió para siempre la comprensión científica del
comportamiento de la falla Septentrional-Oriente.

Esta concentración extrema revela algo fundamental: las fallas transformantes
no liberan su energía gradualmente, sino en pulsos intensos que pueden
prolongarse por semanas. Para los científicos que estudian el riesgo
tsunamigénico, este patrón temporal significa que cuando la falla "despierta",
puede mantenerse activa durante períodos extensos, incrementando las
probabilidades de que ocurra un evento con las características necesarias para
generar un tsunami.
""")

st.subheader("Pilón-Chivirico: El punto donde la tierra se quejó más fuerte")
# Gráfico de líneas por zonas
fig_zonas = evolucion_mensual_por_zona_2024(data)
st.plotly_chart(fig_zonas, use_container_width=True)

st.markdown("""
La geografía de los sismos cuenta su propia historia. De los 10,795 eventos de
2024, 7,408 ocurrieron en Pilón-Chivirico – el 68.6% de toda la actividad
nacional concentrada en una sola región. Mientras esta zona alcanzó su
explosión máxima en noviembre con 7,124 sismos, Santiago-Baconao registró
su pico en septiembre con 713 eventos, y las demás zonas sísmicas del país
(Cabo Cruz, Cauto-Guacanayabo, Imías, Moa Purial, Camagüey-Cubitas, Paso
de los Vientos-Gran Inagua, Caimán, Bahamas Norte, Centro, Bahamas Sur)
mantuvieron niveles mucho menores.
""")

st.markdown("""

Esta concentración geográfica extrema confirma que no se trató de una
activación general del sistema de fallas cubano, sino de un fenómeno muy
localizado. Para los expertos en tsunamis, esta especificidad resulta tanto
tranquilizadora como preocupante: tranquilizadora porque significa que no toda
la isla enfrenta el mismo nivel de riesgo, preocupante porque identifica
exactamente dónde podrían originarse los movimientos verticales del fondo
marino necesarios para generar un tsunami.
""")

st.markdown("<a id='dias'></a>", unsafe_allow_html=True)
st.header("Los días que marcaron la diferencia")
# Gráfico de días más activos
fig_dias = evolucion_mensual_días_2024(data)
st.plotly_chart(fig_dias, use_container_width=True)

st.markdown("""
Algunos días se vuelven legendarios en la historia científica. El 11 de noviembre
– apenas 24 horas después del sismo principal de magnitud 6.7 – se convirtió
en el día más sísmicamente activo del año. Le siguieron el 8 de septiembre y el
7 de abril, cada uno marcando episodios específicos donde la tierra decidió
liberar energía acumulada durante años.

Estos picos revelan que los sismos no siguen un patrón gradual, sino episódico.
Cada evento principal genera cascadas de réplicas que pueden extenderse por
días, un comportamiento que los científicos ahora comprenden es
característico de fallas complejas bajo alta tensión. Para evaluar el riesgo
tsunamigénico, estos patrones temporales son cruciales: demuestran que
después de un sismo mayor, las probabilidades de eventos adicionales se
mantienen elevadas durante períodos significativos.
""")
st.markdown("<a id='analisis'></a>", unsafe_allow_html=True)
st.header("¿Tsunami o no tsunami? El análisis científico")
st.markdown("""
El sismo de magnitud 6.7 del 10 de noviembre no generó tsunami debido a que
sus movimientos fueron predominantemente horizontales (strike-slip),
característica típica de las fallas transformantes. La generación de tsunamis
requiere desplazamientos verticales significativos del fondo marino,
mecanismo que no se produjo en el evento de noviembre de 2024.
Sin embargo, los modelos desarrollados por CENAIS y expertos internacionales
han identificado un escenario de riesgo real: un sismo de magnitud 7.5 o
superior en la misma zona, con componente de movimiento vertical
significativo, podría generar olas de hasta 4 metros en sectores de la costa
nororiental de Cuba.
""")

st.markdown("<a id='zonas'></a>", unsafe_allow_html=True)
st.subheader("Zonas de mayor vulnerabilidad")
st.markdown("""
- **Gibara**  
- **Baracoa**  
- **Holguín**

**Tiempo estimado de llegada:** Entre 10 y 20 minutos posteriores al evento sísmico.  
**Población potencialmente afectada:** Aproximadamente 2 millones de personas
residen en estas regiones costeras.
""")

st.markdown("<a id='historia_caribe'></a>", unsafe_allow_html=True)
st.header("🌊 Antecedentes históricos: La memoria sísmica del Caribe")

st.markdown("""
<div style='background-color:#f0f2f6; padding:20px; border-radius:10px; border-left: 5px solid #4e89ae'>
<h4 style='color:#1e3a8a'>📜 Cuba ha experimentado efectos tsunamigénicos históricos</h4>
<p>El más significativo registrado:</p>

<strong>🌍 El tsunami transatlántico de 1755</strong><br>
<div style='margin-left:20px;'>
• Originado por el <em>terremoto de Lisboa</em> (magnitud estimada ~8.5)<br>
• Cruzó todo el Océano Atlántico impactando el Caribe<br>
• Olas de <span style='background-color:#ffd700'>hasta 3 metros</span> en costas cubanas<br>
• Demostró que los tsunamis pueden propagarse <strong>miles de kilómetros</strong>
</div>
</div>
""", unsafe_allow_html=True)

st.subheader("🚨 Alertas recientes en el Caribe")

st.markdown("""
<div style='background-color:#fff8e1; padding:20px; border-radius:10px; margin-top:20px; border-left: 5px solid #ffc107'>
<strong>Últimas activaciones de protocolos:</strong>
<ul>
  <li><b>Enero 2020</b> │ Sismo 7.7 M<sub>w</sub> Jamaica-Cuba<br><span style='color:#d32f2f'>Activó alerta preventiva regional</span></li>
  <li><b>Febrero 2025</b> │ Sismo 7.6 M<sub>w</sub> Islas Caimán<br><span style='color:#d32f2f'>Reactivó sistemas de monitoreo</span></li>
</ul>

<div style='margin-top:15px; padding:10px; background-color:#e8f5e9; border-radius:5px'>
⚠️ Aunque no generaron tsunamis destructivos, estos eventos confirman que <strong>la amenaza permanece latente</strong> en la región caribeña.
</div>
</div>
""", unsafe_allow_html=True)
st.markdown("<a id='testimonios'></a>", unsafe_allow_html=True)
st.header("Testimonios desde el epicentro")
st.subheader("La experiencia humana detrás de los datos")
st.markdown("""
"Fue un estruendo enorme", relató Yaniseli Ramírez Tejeda, residente de 25
años de Pilón, al periódico *La Demajagua*. Se encontraba en el patio de su casa
con su hijo de dos años cuando comenzó el sismo del 10 de noviembre.

Su testimonio representa la experiencia de miles de familias que ese día
vivieron directamente los efectos de la actividad tectónica. En Pilón, la
infraestructura portuaria sufrió daños considerables y numerosas viviendas
desarrollaron fisuras estructurales, sin registrarse víctimas fatales.
""")

st.markdown("<a id='respuesta'></a>", unsafe_allow_html=True)
st.header("La respuesta institucional inmediata")
st.markdown("""
El presidente Miguel Díaz-Canel emitió instrucciones específicas a través de su
cuenta en X:  
> "Pedimos a nuestra población en esas zonas salir y mantenerse en lugares
abiertos. Comenzamos a evaluar daños para empezar la recuperación. Lo
primero, y esencial, salvar las vidas."

El 14 de noviembre, Díaz-Canel visitó el Observatorio Geodinámico del CENAIS
en Santiago de Cuba, donde exhortó a "aumentar la cultura sísmica en el país".
""")

st.markdown("<a id='numeros'></a>", unsafe_allow_html=True)
st.header("Los números que redefinieron la comprensión científica")
st.subheader("2024: Un año excepcional en términos sísmicos")
st.markdown("""
Los datos de 2024 obligaron a recalibrar los modelos de riesgo sísmico. Los
10,795 eventos registrados representan un incremento superior al 200%
respecto al promedio histórico de entre 2,000 y 4,000 sismos anuales
detectables instrumentalmente.
""")

st.markdown("**Los eventos principales del año:**")
st.markdown("""
1. **10 de noviembre:** Magnitud 6.7 en Bartolomé Masó (evento principal)  
2. **11 de noviembre:** Día de máxima actividad sísmica anual  
3. **8 de septiembre:** Segundo pico de actividad
""")

st.markdown("""
**Intensidad máxima registrada:** VIII grados en la escala EMS en localidades
como Pilón, Bartolomé Masó y Marea del Portillo.

**Interpretación técnica:** Una intensidad VIII indica que las
estructuras bien construidas experimentan daños leves,
mientras que las construcciones convencionales sufren
daños considerables y las estructuras vulnerables colapsan
parcialmente.
""")

st.markdown("""
Esta actividad elevada confirma que la falla Septentrional-Oriente atravesó un
período de alta actividad tectónica durante 2024, proporcionando a los
científicos datos sin precedentes para evaluar el comportamiento futuro del
sistema.
            
Los datos de 2024 han reescrito la comprensión científica sobre el riesgo
sísmico en Cuba. Lo que comenzó como un domingo cualquiera se convirtió en
una ventana extraordinaria hacia el comportamiento de nuestras fallas más
activas. La falla Septentrional-Oriente mostró la mayor actividad registrada en
décadas recientes, confirmando que el riesgo tsunamigénico, aunque
estadísticamente bajo, es científicamente verificable.

Estos hallazgos revelaron que los sistemas de preparación requieren desarrollo
continuo, no reactivo. La infraestructura de monitoreo necesita inversión
sostenida, y más importante aún, la educación pública sobre riesgos
geológicos se ha convertido en una prioridad nacional incuestionable.
""")

st.markdown("<a id='respuesta_final'></a>", unsafe_allow_html=True)
st.header("La respuesta científica a la pregunta fundamental")
st.markdown("""
**¿Puede ocurrir un tsunami en Cuba?**  
El análisis de los datos de 2024 proporciona la respuesta más sólida
científicamente hasta la fecha:

> **Sí, es geológicamente posible.**

Aunque la probabilidad no es inmediata, la evidencia confirma que las
condiciones tectónicas necesarias existen. La falla Septentrional-Oriente posee
el potencial para generar sismos de magnitud suficiente y con el mecanismo
focal adecuado para desplazar verticalmente el fondo marino.

> La cuestión fundamental ya no es "si puede ocurrir", sino "¿estaremos
preparados cuando ocurra?"
""")

st.markdown("<a id='epilogo'></a>", unsafe_allow_html=True)
st.header("Una advertencia y un regalo")

st.markdown("""
La tierra ha entregado tanto una advertencia como un regalo.  
Una **advertencia** sobre los riesgos reales que enfrentamos como nación insular en una zona tectónicamente activa.  
Y un **regalo invaluable**: el conocimiento científico necesario para prepararnos.

Cuando Yaniseli Ramírez corrió con su hijo hacia un lugar seguro esa mañana
de noviembre, no sabía que estaba viviendo un momento histórico para la
ciencia cubana. Tampoco sabía que su experiencia se convertiría en parte de la
evidencia que ayudaría a proteger a las próximas generaciones.

Porque al final, de eso se trata la ciencia:  
**De transformar la incertidumbre en conocimiento, el miedo en preparación,  
y los datos en herramientas para salvar vidas.**

La tierra siguió hablando durante semanas después del 10 de noviembre.  
Y por primera vez en décadas, entregó señales tan contundentes  
que dejaron una **huella irreversible en la ciencia cubana**.
""")


