# Relatório do projeto de sockets
<p> Projeto de sockets na disciplina de Redes </p>
<p> Professor: Kelvin Lopes Dias </p>
<p> Dupla: Ana Júlia de Oliveira Fernandes e  Bruno Miguel Moreira Albuquerque </p>
<h2>Contexto</h2>

	Nesse projeto, criamos um socket, o qual realiza o cálculo de operações matemáticas por meio do envio de dados pelo UDP ou TCP. A linguagem de programação utilizada foi o “Python” e usamos, também, a biblioteca “sockets” e “time” do python. O projeto foi desenvolvido utilizando a arquitetura SOLID, onde cada componente exerce uma função única na funcionalidade. Assim, há um arquivo e função separado para cada “agente”(client udp, client tcp, server tcp, server udp e dns). Foi criada também a funcionalidade do client encerrar a conexão por meio do envio do comando “fim”.
	O Projeto foi organizado seguindo o seguinte fluxo: Servidor DNS é ligado e após isso liga-se os servidores TCP e/ou UDP, os quais se conectam com o DNS. Após ligá-los se pode ligar os clientes TCP e/ou UDP. Quando o cliente faz uma requisição, ele faz uma solicitação ao DNS para obter informações do servidor. Posteriormente, por meio dos clientes se pode enviar operações matemáticas para serem calculadas no servidor, e após isso o cliente recebe a resposta da operação e o tempo em que ela ocorreu.
	O repositório do projeto se encontra nesse link: https://github.com/AnaJulia22/sockets-projeto
      	Assim, ele pode ser baixado por zip ou pelo git clone, instalado suas dependências e sua execução é feita pela ordem previamente estabelecida( primeiro dns, depois servidores e depois clientes), sendo cada um feito em terminais diferentes. 
	Com base nas cinco capturas realizadas abaixo, pode-se observar que o tempo médio de requisição no protocolo UDP foi ligeiramente maior, com uma média de 0,0842 segundos, em comparação com o TCP, onde o tempo médio foi de 0,07161 segundos para as mesmas requisições de cálculos matemáticos. O que ocorreu é extremamente incomum com  o tempo médio do TCP sendo menor, pois, geralmente, o UDP é mais rápido, mas não oferece as mesmas garantias de confiabilidade que o TCP oferece. De todo modo, a escolha entre esses protocolos depende das necessidades específicas de uma aplicação ou sistema.

Capturas dos terminais
Servidor DNS
<img src="">


Server UDP

<img src="">

Client UDP

<img src="">

Server TCP

<img src="">

Client TCP

<img src="">


Capturas wireshark

<img src="">










Nas primeiras linhas, os servidores fazem conexão com o dns, registrando seus nomes no dns. A partir da linha 11, a conexão cliente-servidor tcp se inicia e isso pode ser visto por causa do 3-way-handshake [syn], [syn,ack] e [ack]



Finalizando a conexão tcp com [fin,ack], a conexão cliente-servidor udp se inicia


