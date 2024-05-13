# Inicio_ROS

#!/usr/bin/python3                                                    #Indicamos que tipo de archivo é e como o vai executar


import rospy                                                      #Importamos a librería de rospy, que é a que vai permitirnos crear Nodos ca linguaxe ros                             

from std_msgs.msg import Int32                                    #Desde a librería standar messages importamos o mensaje que vamos publicar (valor dun contador, int32)


rospy.init_node("publisher_node")                               #Inicializamos o noso Nodo con "rospy.init_node" e o nome do Nodo "(publisher_node)"


pub = rospy.Publisher("counter", Int32, queue_size = 1)         #Creamos o obxeto de Publisher, dentro vai ter 3 parámetros.. 1º nome do topico= counter, 2º tipo mnsaje Int 32,  
                                                                # 3º queue_size=1, número de mensaxes que poden estar en cola antes de ser entregados
rate= rospy.Rate(8)                                             #Frecuencia coa que queremos que se execut o contador en Hz

count=0                                                         #Inicializamos a variable de Count

while not rospy.is_shutdown():                                  #Creamos 1 while, e que esté dentro de while vaise executar mentras o Nodo esté correndo
    pub.publish(count)                                          #Queremos que publique o valor do contador, para elo utilizamos a variable pub.publisher e q publique o contador
    count+=1                                                    #Queremos que aumente unha unidade o valor do contador cada vez que fai o ciclo de scan
    rate.sleep()                                                #Este comando é coma un delay especial que garantiza que o Nodo se esté correndo á frecuencia que queremos.
