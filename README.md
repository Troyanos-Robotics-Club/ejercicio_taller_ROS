# Ejercicio práctico del taller de ROS2
Descripcion del resultado final del ejercicio que se realizara en el taller de ROS.
Se tendrá la siguiente estructura: un caso de domótica simple: una casita con luces LED, una puerta automática, un sensor de presencia (ultrasónico) y un botón (timbre).

Se tendrá un sistema de Nodos comunicándose entre la RPi y ROS2 en las VMs de los participantes.

La estructura es la siguiente:
![ejemplo_taller](https://github.com/Troyanos-Robotics-Club/ejercicio_taller_ROS/assets/139887285/79f608ce-da92-4459-b4b0-bf3cbc313ab1)

### Arquitectura
#### Raspberry Pi
Se tendrá corriendo en la RPi un nodo que leerá la distancia del sensor ultrasónico y el estado del botón. Activará los actuadores de las luces LED y el servomotor con una señal de PWM. 
Mandará las lecturas como publishers, y realizará acciones en los actuadores dependiendo de la info que reciba como subscriber. 

#### Nodo 1
Recibirá la información del sensor de distancia y, con base en eso, enciende las luces LED. Se manejará como un salón de clases: encenderá la luz si la lectura es variable (simulando la presncia de una persona) y las apagará si es constante (simulando que la habitación está vacía). Otra alternativa es encederla cuando el valor leído es chico (un threshold).
publisher_LED: manda el estado del LED. Tipo Bool de std_msgs en topic /estado_LED
subscriber_proximidad: recibe la distancia del sensor recibido. Tipo Int32 de std_msgs en topuc /distancia_sensor

#### Nodo 2
Recibirá la info del botón, mandará la señal en un On-Set (de 0 a 1 lógico). Esto hará que se abra y cierre la puerta
subscriber_boton: recibe el estado del botón, tipo Bool de std_msgs en el topic /estado_boton
publisher_servo: manda el DC del PWM al servo, de tipo Int32 de std_msgs en topuc /pwm_servo

# Pasos para instalar el repositorio
