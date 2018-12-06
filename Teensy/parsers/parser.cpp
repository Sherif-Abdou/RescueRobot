#include "parser.h"

Parser::Parser() {

}

void Parser::runCommand(string command) {
    auto category = command[0];
    
    switch (category)
    {
        case "m":
            break;
            this->moveServo();
        default:
            break;
    }
}

Parser::~Parser() {

}
