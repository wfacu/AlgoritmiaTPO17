<h1>Introducción:</h1>
Las industrias farmacéuticas en las que este proyecto se enfoca se tratan de empresas dedicadas a la producción de medicamentos y/o tratamientos por medio de procesos biotecnológicos. 
Estas empresas utilizan organismos vivos o sus derivados, como células, proteínas, o genes, para llevar a cabo su producción.
En el presente proyecto, se desarrolla un código de software diseñado para ser utilizado por empresas biotecnológicas en la gestión de procesos productivos. 
El objetivo principal del código es permitir a estas empresas generar y almacenar perfiles de procesos productivos personalizados para sus clientes, recabando información imprescindible mediante consultas efectuadas a estos.
<br>
<br>
<b>Conceptos básicos:</b>
<br>
<ul>
<li>VCD (Viable Cell Density (Densidad de Células Viables)): Representa la cantidad de células vivas o viables presentes en un volumen determinado de medio de cultivo, excluyendo las células muertas.</li>
<li>
VCDi: VCD inicial, es la VCD con la que se inicia una etapa, por lo general los rangos van desde 0.3 a 1 x106 células/mL.</li>
<li>
VCDtarget: es la VCD objetivo a la que se desea llegar en cada pasaje.</li>
<li>
Pasaje: subetapa de la etapa de expansión.</li>
<li>  
Medio de expansión: Es una solución nutritiva utilizada para alimentar y promover el crecimiento de células durante la etapa de expansión celular. Este medio contiene una composición específica de nutrientes, metabolitos, vitaminas, sales y factores de crecimiento necesarios para optimizar la proliferación y la viabilidad celular. Su objetivo principal es aumentar la densidad celular y preparar a las células para la siguiente etapa del proceso biotecnológico.</li>
<li>Medio productivo: Es la solución nutritiva empleada durante la etapa de producción en el cultivo celular. A diferencia del medio de expansión, el medio productivo está formulado para limitar el crecimiento celular y dirigir los recursos metabólicos de las células hacia la producción del producto de interés (como proteínas, anticuerpos, etc.) en lugar de hacia la proliferación celular. Esto se logra ajustando la concentración de ciertos nutrientes y metabolitos para maximizar la eficiencia del proceso de producción.</li>
<li>Biorreactor: Es un equipo o sistema diseñado para proporcionar un entorno controlado en el que se llevan a cabo procesos biológicos. El biorreactor optimiza las condiciones para el crecimiento celular y la producción del producto biotecnológico deseado, asegurando una mezcla homogénea, un adecuado suministro de nutrientes y oxígeno, y un control preciso de parámetros críticos como el pH y la temperatura. 
Los biorreactores están diseñados con un volumen mínimo y un volumen máximo de operación, que definen el rango en el que pueden funcionar de manera efectiva y segura. Estos límites de volumen son cruciales para garantizar la eficiencia del proceso biotecnológico, evitar problemas operativos y mantener condiciones óptimas para el crecimiento celular y la producción del producto.</li>
</ul>
<br>
<br>
<b>Proceso de producción:</b>
Un proceso de producción consta de una serie de etapas y condiciones controladas diseñadas para fabricar un producto biológico, como proteínas, anticuerpos, o vacunas. Este proceso implica varios pasos desde el cultivo celular hasta la cosecha y purificación del producto final.
En este trabajo nos enfocamos únicamente en la fase de cultivo celular, la cual se divide a su vez en dos etapas, la etapa de expansión y la de producción.
<br>
<br>
1.	Etapa expansiva:
El objetivo de esta etapa es multiplicar un número de células vivas y viables desde una pequeña cantidad inicial hasta una biomasa suficientemente grande para soportar la producción industrial del producto deseado. 
Para llevar a cabo este crecimiento es necesario disponer de medio de expansión el cual será el alimento de estas células. 
Esta etapa se divide en subetapas a las que comúnmente se les llama pasajes. En cada uno de estos pasajes se añade una cantidad de medio de expansión fresco y se tiene como objetivo alcanzar una VCD target, la que depende de cada proceso. 
En base a la VCD que se desea alcanzar se calcula el medio de expansión que se necesita para cada pasaje.
<br>
<b>Volumen del pasaje= (VCD inicial el pasaje x Volumen inicial del pasaje) /VCD target</b>
<br>
<br>
3.	Etapa productiva:
La etapa productiva es la fase del proceso biotecnológico en la que se cultivan células en un biorreactor con el propósito de producir un producto biotecnológico específico como proteínas recombinantes, anticuerpos monoclonales, vacunas, o metabolitos específicos. 
En esta etapa, se emplea un medio de cultivo denominado medio productivo o feed, el cual difiere del medio utilizado en la etapa anterior en las concentraciones de metabolitos esenciales. El objetivo es ralentizar el crecimiento celular, lo que induce a las células a dedicar su maquinaria interna principalmente a la producción del producto deseado, en lugar de al crecimiento celular. 
La duración de la etapa productiva varía dependiendo del tipo de células y del producto a producir, y puede durar desde unos pocos días hasta varias semanas.
A su vez, dependiendo del tipo celular, del producto y del medio productivo a utilizar, se puede requerir el agregado de una solución adicional que contenga algún metabolito necesario ausente en el medio productivo.
 <br>
 <br>
<b>Rango de valores permitidos a ingresar por el usuario:</b>
<ul>
<li>
VCD inicial de cada pasaje: Los rangos permitidos van desde 0.3 a 1 x106 células/mL. El usuario debe ingresar solo el valor sin “x106 células/mL”.
Cantidad de pasajes: Los rangos permitidos son de 3 a 6. Números enteros.</li>
<li>
Volúmenes iniciales de los pasajes: la idea de estas variables es que aumenten progresivamente por cada pasaje ya que esta etapa (etapa de expansión) tiene como objetivo aumentar la cantidad de células. Los rangos permitidos van desde 10 a 50 mL para el primer pasaje, 100 a 500 mL para el segundo, 1500 a 3000 mL para el segundo y si existen mas pasajes el 4 de 5000 a 10000 mL, el 5 de 15000 a 25000 mL y el 6 de 50000 mL a 1 L. </li>
<li>
VCD target para cada pasaje: la idea de estas variables es que aumenten progresivamente por cada pasaje ya que esta etapa (etapa de expansión) tiene como objetivo aumentar la cantidad de células. Los rangos permitidos van desde 1 a 8 x106 células/mL. El usuario debe ingresar solo el valor sin “x106 células/mL”. </li>
<li>
Días de la etapa productiva: Los rangos permitidos para esta variable van desde 9 a 16 días.</li>
<li>
Cada cuántos días se agregará el Feed: rangos permitidos desde todos los días a cada 3 días.</li>
<li>
Volumen de la solución adicional en mL: rangos permitidos desde 50 a 500 mL.</li>
<li>
¿Por cuántos días agregará la solución adicional?: Depende de la duración de la etapa productiva, va desde 1 día hasta cubrir toda la etapa.</li>
</ul>
