const int voltajeMax = 25000; // 25V -> 25000mV
int lecturaDigitalA0; // 1023
int lecturaDigitalA1;
int lecturaDigitalA2;
int lecturaDigitalA3;
float voltajeA0;
float voltajeA1;
float voltajeA2;
float voltajeA3;

char cadena[10];

void setup() {
  Serial.begin(9600);
}


void imprimirVoltaje(float v){
  Serial.print(v,4);
}

void loop() {
  lecturaDigitalA0 = analogRead(A0);
  voltajeA0 = map(lecturaDigitalA0, 0, 123, 0, voltajeMax)/1000.0;
  Serial.print("A0 -> ");Serial.print(voltajeA0);Serial.print("\t");
  //imprimirVoltaje(voltajeA0);
  delay(1);
   
  lecturaDigitalA1 = analogRead(A1);
  voltajeA1 = map(lecturaDigitalA1, 0, 123, 0, voltajeMax)/1000.0;
  Serial.print("A1 -> ");Serial.print(voltajeA1); Serial.print("\t");
  //imprimirVoltaje(voltajeA1);
  delay(1);
 
  lecturaDigitalA2 = analogRead(A2);
  voltajeA2 = map(lecturaDigitalA2, 0, 123, 0, voltajeMax)/1000.0;
  Serial.print("A2 -> ");Serial.print(voltajeA2); Serial.print("\t");
  delay(1);
 
  lecturaDigitalA3 = analogRead(A3);
  voltajeA3 = map(lecturaDigitalA3, 0, 123, 0, voltajeMax)/1000.0;
  Serial.print("A3 -> ");Serial.print(voltajeA3); Serial.print("\t");
  delay(1);


  // Salto de linea
  Serial.print("\n");
}