O seguinte repositório representa o workspace onde está alocado o pacote "ponderada_turtlesim". Esse pacote conta com um código capaz de fazer com que a tartaruga do turtlesim realize um movimento segundo os critérios estipulados no enunciado da atividade.

Para tanto, foram utilizadas as configurações necessárias de um pacote em ROS.

Para executar é necessário que haja dois terminais:
Um deles rodará o gráfico do turtlesim, com o comando "ros2 run turtlesim turtlesim_node"
O outro irá rodar o código executado pela tartaruga, com o seguinte comando "ros2 run ponderada_turtlesim ponderada_drawing_node"

O código contém as principais funções:

spawn_turtle: inicia a tartaruga

set_pen: configura o traço do desenho

move_circle: faz a tartaruga se movimentar em círculo

kill_turtle: faz a tartaruga desaparecer depois de formar o círculo.

O funcionamento é possível ver no seuinte vídeo do drive: [funcionamento da ponderada](https://drive.google.com/file/d/128Edn9zmxFie-lYL2HkOw4102uFYeibP/view?usp=sharing)
