//
// Created by Sherif Abdou on 12/8/18.
//

#ifndef MORSE_MORSEPARSER_H
#define MORSE_MORSEPARSER_H

#include <vector>
#include <string>
using namespace std;
class MorseParser {
public:
    MorseParser();

    string parseMorse(vector<int> morse);
    vector<int> toMorse(string message);
private:
    vector<int> a = {1, 0, 1, 1, 1};
    vector<int> b = {1, 1, 1, 0, 1, 0, 1, 0, 1};
    vector<int> c = {1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1};
    vector<int> d = {1, 1, 1, 0, 1, 0, 1};
    vector<int> e = {1};
    vector<int> f = {1, 0, 1, 0, 1, 1, 1, 0, 1};
    vector<int> g = {1, 1, 1, 0, 1, 1, 1, 0, 1};
    vector<int> h = {1, 0, 1, 0, 1, 0, 1};
    vector<int> i = {1, 0, 1};
    vector<int> j = {1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1};
    vector<int> k = {1, 1, 1, 0, 1, 0, 1, 1, 1};
    vector<int> l = {1, 0, 1, 1, 1, 0, 1, 0, 1};
    vector<int> m = {1, 1, 1, 0, 1, 1, 1};
    vector<int> n = {1, 1, 1, 0, 1};
    vector<int> o = {1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1};
    vector<int> p = {1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1};
    vector<int> q = {1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1};
    vector<int> r = {1, 0, 1, 1, 1, 0, 1};
    vector<int> s = {1, 0, 1, 0, 1, 0};
    vector<int> t = {1, 1, 1};
    vector<int> u = {1, 0, 1, 0, 1, 1, 1};
    vector<int> v = {1, 0, 1, 0, 1, 0, 1, 1, 1};
    vector<int> w = {1, 0, 1, 1, 1, 0, 1, 1, 1};
    vector<int> x = {1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1};
    vector<int> y = {1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1};
    vector<int> z = {1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1};
};


#endif //MORSE_MORSEPARSER_H
