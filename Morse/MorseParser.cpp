//
// Created by Sherif Abdou on 12/8/18.
//

#include "MorseParser.h"

MorseParser::MorseParser() = default;

string MorseParser::parseMorse(vector<int> morse) {
    string result;
    vector<vector<int>> letters;
    int marker = 0;
    for (int i1 = 0; i1 < morse.size()-3; ++i1) {
        if (morse[i1+1] == 0 && morse[i1+2] == 0 && morse[i1+3] == 0) {
            letters.emplace_back(morse.begin()+marker, morse.begin()+i1+1);
            marker = i1+4;
        }
    }
    return result;
}