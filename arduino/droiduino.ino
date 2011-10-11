#define SPEED_1 4
#define SPEED_2 2
#define SPEED_3 8
#define DELAY_RELAY 250


void turnOffAll() {
    digitalWrite(SPEED_1, LOW);
    digitalWrite(SPEED_2, LOW);
    digitalWrite(SPEED_3, LOW);
}

void setup() {
    pinMode(SPEED_1, OUTPUT);
    pinMode(SPEED_2, OUTPUT);
    pinMode(SPEED_3, OUTPUT);

    digitalWrite(SPEED_1, LOW);
    digitalWrite(SPEED_2, LOW);
    digitalWrite(SPEED_3, LOW);

    Serial.begin(9600);
}

void loop() {
    if (Serial.available()) {
        char data = Serial.read();
        if (data == '0') {
            turnOffAll();
            delay(DELAY_RELAY);
        }
        else if (data == '1') {
            turnOffAll();
            delay(DELAY_RELAY);
            digitalWrite(SPEED_1, HIGH);
            digitalWrite(SPEED_2, LOW);
            digitalWrite(SPEED_3, LOW);
            delay(DELAY_RELAY);
        }
        else if (data == '2') {
            turnOffAll();
            delay(DELAY_RELAY);
            digitalWrite(SPEED_1, LOW);
            digitalWrite(SPEED_2, HIGH);
            digitalWrite(SPEED_3, LOW);
            delay(DELAY_RELAY);
        }
        else if (data == '3') {
            turnOffAll();
            delay(DELAY_RELAY);
            digitalWrite(SPEED_1, LOW);
            digitalWrite(SPEED_2, LOW);
            digitalWrite(SPEED_3, HIGH);
            delay(DELAY_RELAY);
        }
    }
}
