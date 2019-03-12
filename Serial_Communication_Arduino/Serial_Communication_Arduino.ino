void setup() {
  Serial.begin(115200);
  Serial.setTimeout(2000);
}

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
    char a = Serial.read();//A mensagem recebida é da forma PARAM_01/PARAM_02/PARAM_03/PARAM_04/PARAM_05/PARAM_06/PARAM_07/e onde 'e' indica o fim da tranmissão dos dados
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


void loop() {
  float param [5];//[0]Current_Range,[1]V_inicio,[2]V_fim,[3]V_pulso,[4]V_passo,[5]T_pulso,[6]SRate;
  rec_param(param);

  ///Envio dos valores lidos no DPV
  start_transmition();
  
  // Simulando a leitura dos 120 pontos com 25ms entre cada leitura:
  unsigned int y = 1;
  unsigned int y1 = 3;
  float x = -0.6;
  for (unsigned int i = 0; i < 120; i++){
    x += 0.005;
    if(i < 20){
      y = 1;
      y1 = 3;
    }
    else if(i > 20 and i < 60){
      y++;
      y1++;
    }
    else if( i ==60){
      y = 41;
      y1 = 43;
    }
    else if(i > 60 and i < 100){
      y = y-1;
      y1 = y1 - 1;
    }
    else {
      y = 1;
      y1 = 3;
    }
    Serial.println(x,3);
    Serial.println(y,DEC);
    Serial.println(y1,DEC);
    delay(25);
  }
  
  end_transmition();
  ///Enviando os valores do fundo de escala:
  unsigned int zero,f_positivo,f_negativo;
  start_transmition();
  zero = 600;
  f_positivo = 300;
  f_negativo = 350;
  Serial.println(zero,DEC);
  Serial.println(f_positivo,DEC);
  Serial.println(f_negativo,DEC); 
  end_transmition();
}
