#include <iostream>
#include "MorseParser.h"
int main() {
    auto parser = MorseParser();
    parser.parseMorse({1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0});
    std::cout << "Hello, World!" << std::endl;
    return 0;
}