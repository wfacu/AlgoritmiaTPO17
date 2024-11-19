<img src="https://i.ibb.co/LP2rwFw/oie-transparent.png" alt="Imagen centrada">
<h1>Introducción:</h1>
Las industrias farmacéuticas en las que este proyecto se enfoca se tratan de empresas dedicadas a la producción de medicamentos y/o tratamientos por medio de procesos biotecnológicos. 
Estas empresas utilizan organismos vivos o sus derivados, como células, proteínas, o genes, para llevar a cabo su producción.
En el presente proyecto, se desarrolla un código de software diseñado para ser utilizado por empresas biotecnológicas en la gestión de procesos productivos. 
El objetivo principal del código es permitir a estas empresas generar y almacenar perfiles de procesos productivos personalizados para sus clientes, recabando información imprescindible mediante consultas efectuadas a estos.
<h1>Conceptos básicos:</h1>
<ul>
<li><b>VCD (Viable Cell Density (Densidad de Células Viables)):</b> Representa la cantidad de células vivas o viables presentes en un volumen determinado de medio de cultivo, excluyendo las células muertas.</li>
<li><b>VCDi:</b> VCD inicial, es la VCD con la que se inicia una etapa, por lo general los rangos van desde 0.3 a 1 x10⁶ células/mL.</li>
<li><b>VCDtarget:</b> es la VCD objetivo a la que se desea llegar en cada pasaje.</li>
<li><b>Pasaje:</b> subetapa de la etapa de expansión.</li>
<li><b>Medio de expansión:</b> Es una solución nutritiva utilizada para alimentar y promover el crecimiento de células durante la etapa de expansión celular. Este medio contiene una composición específica de nutrientes, metabolitos, vitaminas, sales y factores de crecimiento necesarios para optimizar la proliferación y la viabilidad celular. Su objetivo principal es aumentar la densidad celular y preparar a las células para la siguiente etapa del proceso biotecnológico.</li>
<li><b>Medio productivo:</b> Es la solución nutritiva empleada durante la etapa de producción en el cultivo celular. A diferencia del medio de expansión, el medio productivo está formulado para limitar el crecimiento celular y dirigir los recursos metabólicos de las células hacia la producción del producto de interés (como proteínas, anticuerpos, etc.) en lugar de hacia la proliferación celular. Esto se logra ajustando la concentración de ciertos nutrientes y metabolitos para maximizar la eficiencia del proceso de producción.</li>
<li><b>Biorreactor:</b> Es un equipo o sistema diseñado para proporcionar un entorno controlado en el que se llevan a cabo procesos biológicos. El biorreactor optimiza las condiciones para el crecimiento celular y la producción del producto biotecnológico deseado, asegurando una mezcla homogénea, un adecuado suministro de nutrientes y oxígeno, y un control preciso de parámetros críticos como el pH y la temperatura. 
Los biorreactores están diseñados con un volumen mínimo y un volumen máximo de operación, que definen el rango en el que pueden funcionar de manera efectiva y segura. Estos límites de volumen son cruciales para garantizar la eficiencia del proceso biotecnológico, evitar problemas operativos y mantener condiciones óptimas para el crecimiento celular y la producción del producto.</li>
</ul>
<h1>Proceso de producción:</h1>
Un proceso de producción consta de una serie de etapas y condiciones controladas diseñadas para fabricar un producto biológico, como proteínas, anticuerpos, o vacunas. Este proceso implica varios pasos desde el cultivo celular hasta la cosecha y purificación del producto final.
En este trabajo nos enfocamos únicamente en la fase de cultivo celular, la cual se divide a su vez en dos etapas, la etapa de expansión y la de producción.
<ol>
<li>Etapa expansiva:</li>
El objetivo de esta etapa es multiplicar un número de células vivas y viables desde una pequeña cantidad inicial hasta una biomasa suficientemente grande para soportar la producción industrial del producto deseado. 
Para llevar a cabo este crecimiento es necesario disponer de medio de expansión el cual será el alimento de estas células. 
Esta etapa se divide en subetapas a las que comúnmente se les llama pasajes. En cada uno de estos pasajes se añade una cantidad de medio de expansión fresco y se tiene como objetivo alcanzar una VCD target, la que depende de cada proceso. 
En base a la VCD que se desea alcanzar se calcula el medio de expansión que se necesita para cada pasaje.
<br>
<b>Volumen del pasaje</b> = <i>(VCD inicial el pasaje x Volumen inicial del pasaje) /VCD target</i>
<br>
<li>Etapa productiva:</li>
La etapa productiva es la fase del proceso biotecnológico en la que se cultivan células en un biorreactor con el propósito de producir un producto biotecnológico específico como proteínas recombinantes, anticuerpos monoclonales, vacunas, o metabolitos específicos. 
En esta etapa, se emplea un medio de cultivo denominado medio productivo o feed, el cual difiere del medio utilizado en la etapa anterior en las concentraciones de metabolitos esenciales. El objetivo es ralentizar el crecimiento celular, lo que induce a las células a dedicar su maquinaria interna principalmente a la producción del producto deseado, en lugar de al crecimiento celular. 
La duración de la etapa productiva varía dependiendo del tipo de células y del producto a producir, y puede durar desde unos pocos días hasta varias semanas.
A su vez, dependiendo del tipo celular, del producto y del medio productivo a utilizar, se puede requerir el agregado de una solución adicional que contenga algún metabolito necesario ausente en el medio productivo.
</ol>
<h1>Rango de valores permitidos a ingresar por el usuario:</h1>
<ul>
<li>VCD inicial de cada pasaje: Los rangos permitidos van desde 0.3 a 1 x10⁶ células/mL. El usuario debe ingresar solo el valor sin “x10⁶ células/mL”.</li>
<li>Cantidad de pasajes: Los rangos permitidos son de 3 a 6. Números enteros.</li>
<li>Volúmenes iniciales de los pasajes: la idea de estas variables es que aumenten progresivamente por cada pasaje ya que esta etapa (etapa de expansión) tiene como objetivo aumentar la cantidad de células. Los rangos permitidos van desde 10 mL a 1000 mL.</li>
<li>Días por pasaje: Los rangos permitidos pueden ser 3 o 4. Números enteros.</li>
<li>VCD target para cada pasaje: la idea de estas variables es que aumenten progresivamente por cada pasaje ya que esta etapa (etapa de expansión) tiene como objetivo aumentar la cantidad de células. Los rangos permitidos van desde 1 a 8 x10⁶ células/mL. El usuario debe ingresar solo el valor sin “x10⁶ células/mL”.</li>
<li>Días de la etapa productiva: Los rangos permitidos para esta variable van desde 9 a 16 días.</li>
<li>Cada cuántos días se agregará el Feed: rangos permitidos desde 2 a cada 3 días.</li>
<li>Volumen de la solución adicional en ml: rangos permitidos desde 50 a 500 mL.</li>
<li>Por cuántos días agregará: Va desde 1 a 9.</li>
</ul>

<small>
  <img src="https://facundo-seib.github.io/quad/images/LogoUADE.png" alt="Logo UADE" width="50">
  Proyecto presentado con fines educativos. Los integrantes son los siguientes:
  <ul>
    <li>Erika Tosto</li>
    <li>Facundo Pall</li>
    <li>Valentín Romero</li>
  </ul>
</small>

