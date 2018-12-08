#include <iostream>
#include "MorseParser.h"
int main() {
    auto parser = MorseParser();
    auto result = parser.parseMorse({1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0});
    auto f = vector<int>({1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0});
    std::cout << result << std::endl;
    auto morse = parser.toMorse("ae e");
    for (auto& f: morse) {
        std::cout << f << std::endl;
    }
    std::cout << std::endl;
    std::cout << (morse == f) << std::endl;
    return 0;
}