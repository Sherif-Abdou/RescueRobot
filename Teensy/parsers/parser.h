#include <arduino.h>

class Parser {
public:
    Parser();
    ~Parser();
    void runCommand(string);
private:
    void moveServo(int, char);
};