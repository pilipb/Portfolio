
/*
        Arduino Brushless Motor Control
     by Dejan, https://howtomechatronics.com
*/
#include <Servo.h>
Servo ESC;     // create servo object to control the ESC
int potValue;  // value from the analog pin or simply a speed

#include <Filters.h>

//SETTING UP AVERAGING AND PLOTTING HERE
float testFrequency = 60;                     // test signal frequency (Hz)
float windowLength = 20.0/testFrequency;     // how long to average the signal, for statistist
int sensorValue = 0;
float intercept = -0.1129; // to be adjusted based on calibration testing
float slope = 0.0405; // to be adjusted based on calibration testing
float current_amps; // estimated actual current in amps

int LP = 0;
int HP = 0;
int one ;
int two ;
int three ;

unsigned long printPeriod = 1000; // in milliseconds
// Track time in milliseconds since last reading 
unsigned long previousMillis = 0;



//INCREASING THE RATE BY CHANGING THE PRESCALER TO 16
// Arrays to save our results in unsigned long start_times[100];
unsigned long stop_times[100]; unsigned long values[100];
// Define various ADC prescaler 
const unsigned char PS_16 = (1 << ADPS2); const unsigned char PS_32 = (1 << ADPS2) | (1 << ADPS0); const unsigned char PS_64 = (1 << ADPS2) | (1 << ADPS1); const unsigned char PS_128 = (1 << ADPS2) | (1 << ADPS1) | (1 << ADPS0);
// Setup the serial port and pin 2 
#define FASTADC 1
// defines for setting and clearing register bits
#ifndef cbi
#define cbi(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif
#ifndef sbi
#define sbi(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif

int value[100];   // variable to store the value coming from the sensor

void setup() 
{
  //initialise serial communication at 115200 bits a second
 Serial.begin(115200) ;
 int i ;
 
 { ESC.attach(9,1000,3000); // (pin, min pulse width, max pulse width in microseconds) 

#if FASTADC
  // set prescale to 16
  sbi(ADCSRA,ADPS2) ;
  cbi(ADCSRA,ADPS1) ;
  cbi(ADCSRA,ADPS0) ;
#endif
}

void loop() 

//potValue = 500 //analogRead(A0);   // reads the value of the potentiometer if using(value between 0 and 1023)
;  potValue = 90;   // map(potValue, 0, 1023, 0, 180) scale it to use it with the servo library (value between 0 and 180)
  ESC.write(potValue);    // Send the signal to the ESC


    
  RunningStatistics inputStats;     // create statistics to look at the raw test signal
 //RUNNING AVERAGE
  inputStats.setWindowSecs( windowLength );

  

 //LOW PASS FILTER
 FilterOnePole lowpassFilter( LOWPASS, 1000000 );   


 //HIGH PASS FILTER
 FilterTwoPole highpassFilter( HIGHPASS, 1 );   

 
 

  
  while( true ) {   
    sensorValue = analogRead(A0);  // read the analog in value:
    inputStats.input(sensorValue); // log to Stats function
    LP = intercept-21 + slope*(lowpassFilter.input( sensorValue ));
    HP = intercept + slope*(highpassFilter.input( sensorValue ));
    
    if((unsigned long)(millis() - previousMillis) >= printPeriod) {
      previousMillis = millis();   // update time


   

    
      // display current values to the screen
      Serial.print( "\n" );
      // output sigma or variation values associated with the inputValue itsel
      //Serial.print( "\tsigma: " ); Serial.print( inputStats.sigma() );
      // convert signal sigma value to current in amps
      current_amps = intercept + slope * inputStats.sigma();
      Serial.print( "\tamps_averaging: " ); Serial.print( current_amps );
      // output lowpass
      Serial.print( "\tHP_filter: "); Serial.print(LP);
      //output highpass
      Serial.print( "\tLP_filter: "); Serial.print(HP);
     
        



//AVERAGING 
  // calculate the average:
//  average = total / numReadings;
  // send it to the computer as ASCII digits
  //Serial.println(average);
//  delay(1);        // delay in between reads for stability

//UN AVERAGED UN FLITERED
//  read the input on analog pin 0:
//  int sensorValue = analogRead(A0);
//  // print out the value you read:
//  float current = (sensorValue - 2.5)/0.17;
//  // print out the value you read:
//  Serial.println(current);
//  //Serial.println(sensorValue);
//  delay(0.01);        // delay in between reads for stability




;    }    }}
