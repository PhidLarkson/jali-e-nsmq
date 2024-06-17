#include <WiFi.h>
#include <WiFiClient.h>

const char* ssid = "ESP"; // Replace with your WiFi network name
const char* password = "smart123"; // Replace with your WiFi password

const int port = 10000; // Adjust port if needed

// Pin definitions
const int bell1Pin = 4;
const int bell2Pin = 14;
const int led1Pin = 2;
const int led2Pin = 15;
const int buzzerPin = 5;

WiFiServer server(port);
WiFiClient client;

char bellSequence[2] = "";
int sequence_index = 0;

unsigned long debounceTime = 50; // debounce time in milliseconds
unsigned long lastBell1PressTime = 0;
unsigned long lastBell2PressTime = 0;

void setup() {
  Serial.begin(115200);
  delay(1000);

  Serial.print("Connecting to WiFi: ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.print("Connected to WiFi with IP: ");
  Serial.println(WiFi.localIP());

  // Set button pins as input
  pinMode(bell1Pin, INPUT);
  pinMode(bell2Pin, INPUT);
  // Set LED pins as output
  pinMode(led1Pin, OUTPUT);
  pinMode(led2Pin, OUTPUT);
  // Set buzzer pin as output
  pinMode(buzzerPin, OUTPUT);
  // Turn off LEDs and buzzer initially
  digitalWrite(led1Pin, LOW);
  digitalWrite(led2Pin, LOW);
  digitalWrite(buzzerPin, LOW);

  server.begin();
}

void loop() {
  if (client.connected()) {
    if (client.available()) {
      char c = client.read();
      if (c == '#') {
        sequence_index = 0;
        bellSequence[0] = '\0'; // Clear the sequence
        Serial.println("Sequence reset.");
        // Turn off LEDs and buzzer on reset
        digitalWrite(led1Pin, LOW);
        digitalWrite(led2Pin, LOW);
        digitalWrite(buzzerPin, LOW);
      }
    }

    // Read button states and update sequence
    int bell1State = digitalRead(bell1Pin);
    int bell2State = digitalRead(bell2Pin);
    unsigned long currentTime = millis();

    if (bell1State == HIGH && (currentTime - lastBell1PressTime > debounceTime)) {
      lastBell1PressTime = currentTime;
      bellSequence[sequence_index] = 'A';
      sequence_index = (sequence_index + 1) % 2;
      // Flash LED 1 and sound buzzer for bell 1 press
      digitalWrite(led1Pin, !digitalRead(led1Pin)); // Toggle LED 1
      tone(buzzerPin, 1000, 200); // Play sound at 1kHz for 200ms
      delay(200); // Delay to avoid rapid flashing
      digitalWrite(led1Pin, LOW); // Turn off LED 1
      noTone(buzzerPin); // Stop buzzer
      Serial.println("Bell A pressed first");
      client.println("A");
    } else if (bell2State == HIGH && (currentTime - lastBell2PressTime > debounceTime)) {
      lastBell2PressTime = currentTime;
      bellSequence[sequence_index] = 'B';
      sequence_index = (sequence_index + 1) % 2;
      // Flash LED 2 and sound buzzer for bell 2 press
      digitalWrite(led2Pin, !digitalRead(led2Pin)); // Toggle LED 2
      tone(buzzerPin, 1500, 200); // Play sound at 1.5kHz for 200ms
      delay(200);
      digitalWrite(led2Pin, LOW); // Turn off LED 2
      noTone(buzzerPin); // Stop buzzer
      Serial.println("Bell B pressed first");
      client.println("B");
    }
  } else {
    client = server.available();
    if (client) {
      client.println("Hey Python client!");
      client.flush();
      Serial.println("New client connected.");
    }
  }
}

