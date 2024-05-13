#!/usr/bin/python3

import rospy                                    #Importamos a librería de rospy , que é a que vai permitirnos crear Nodos ca linguaxe ros                             

from std_msgs.msg import Int32                  #Desde a librería standar messages importamos o tipo de dato Int32


def callback(msg):                              #Definimos a función (callback), o seu parámetro é a mensaxe que lle chega do contador
    print (msg.data)                            #Imprimimos a mensaxe.....   o atributo ".data" do tipo de mensaje Int32 de standar message, ten so ese atributo.

rospy.init_node("topic_subscriber")             #Inicializamos o noso Nodo con "rospy.init_node" e o nome do Nodo "(topic_subscriber)"

sub = rospy.Subscriber("counter",Int32,callback)  #Agora facemos o Obxeto de subscriber, indicando que Tópico está subscrito(contador),tipo de dato(Int32),e a función (callback)






rospy.spin()                                    #  Esta función vai ciclar o nodo, para que sempre esté activo escoitando ao contador
