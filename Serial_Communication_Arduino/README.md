# Comunicação Serial do ESP com o Python

## As seguintes funções devem ser adicionadas:
	void rec_param(float* param)
	void start_transmition()
	void end_transmition()
## As seguintes configurações devem ser adicionadas:
	baud_rate == 115200
	Serial.setTimeout == 2000 

###Primeiro passo é a chamada da função rec_param

A função rec_param recebe como argumento um vetor de float cujo tamanho é o tamanho de parâmetros a serem recebidos,
e onde os parâmetros ficarão salvos após a chamada da função.
Os parâmetros a serem recebidos são os seguintes: (Exatamente na mesma ordem):
	1) Range de Corrente
	2) V_inicio
	3) V_fim
	4) V_pulso
	5) V_passo
	6) T_pulso

O próximo passo é chamar a função void start_transmition() para começar o envio dos valores lidos 

Os valores a ser enviados devem seguir a seguinte ordem:
	1) Float, com 4 casas decimais, representando a coordenada X (Serial.println(X,4))
	2) Inteiro (Y) representando a corrente faradaica (Serial.println(Y,DEC))
	3) Inteiro (Y1) representando a corrente capacitiva (Serial.println(Y1,DEC))

Após enviar todos os valores, chamar a função end_transmition()