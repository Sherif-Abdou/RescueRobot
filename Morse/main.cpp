#include <iostream>
#include "MorseParser.h"
int main() {
    auto parser = MorseParser();
    auto result = parser.parseMorse({1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0});
    std::cout << result << std::endl;
    return 0;
}