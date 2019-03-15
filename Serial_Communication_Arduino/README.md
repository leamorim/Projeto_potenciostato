# Comunicação Serial do ESP com o Python

## As seguintes funções devem ser adicionadas:
	void rec_param(float* param){//Função que recebe os parâmetros do DPV
	  while(!Serial.available()){}
	  while(true){
	    String start = Serial.readStringUntil('\n');
	    if(start == "start"){
	        break;
	      }
	  }
	  Serial.println("start");
	  
	  String aux;
	  while(!Serial.available()){}
	  unsigned int i = 0;
	  while(Serial.available()){
	    char a = Serial.read();
	    //A mensagem recebida é da forma range_current/V_inicio/V_fim/V_pulso/V_passo/T_pulso/s_rate/e onde 'e' indica o fim da tranmissão dos dados
	    if(a == '/'){
	      param[i] = aux.toFloat();
	      aux = ""; 
	      i++;
	    }
	    else if(a == 'e'){
	      Serial.println("end");
	      break;
	    }
	    else{
	      aux = aux + a;
	    }
	  }  
	}

	void start_transmition(){
	  Serial.println("start");
	  while(!Serial.available()){}
	  while(true){
	    String start = Serial.readStringUntil('\n');
	    if(start == "start"){
	      break;
	    }
	  }
	}


	void end_transmition(){
	  Serial.println("end");
	  while(!Serial.available()){}
	  while(true){
	    String end = Serial.readStringUntil('\n');
	    if(end == "end"){
	        break;
	      }
	    }
	}

## As seguintes configurações devem ser adicionadas:
	baud_rate == 115200
	Serial.setTimeout == 2000 

## Fluxo:

Primeiro passo é a chamada da função rec_param.

A função rec_param recebe como argumento um vetor de float cujo tamanho é o tamanho de parâmetros a serem recebidos,
e onde os parâmetros ficarão salvos após a chamada da função.

Passe como argumento algo do tipo: *float buffer [7]*, uma vez que os valores recebidos serão do tipo float.

Os parâmetros a serem recebidos são os seguintes: (Exatamente na mesma ordem):

1. Current Range	**(índice referente ao range escolhido)**
2. Pot. Inicial 	**(em Volts)**
3. Pot. Final		**(em Volts)**
4. Pot. Passo		**(em Volts)**
5. Pot. Pulso		**(em Volts)**
6. Tem. Pulso		**(em Volts)**
7. SRate			**(em Volts/Segundo)**

O próximo passo é chamar a função void **start_transmition()** para começar o envio dos valores lidos 

Os valores devem ser enviados ponto a ponto na seguintes ordem:

1. Float, com 4 casas decimais, representando a coordenada X 	**(Serial.println(X,4))** [Printa 4 casas decimais]
2. Inteiro (Y) representando a corrente faradaica 				**(Serial.println(Y,DEC))**
3. Inteiro (Y1) representando a corrente capacitiva 			**(Serial.println(Y1,DEC))**

Após enviar todos os valores, chamar a função end_transmition() para sinalizar o fim da transmissão de dados