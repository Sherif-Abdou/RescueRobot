//
// Created by Sherif Abdou on 12/8/18.
//

#include "MorseParser.h"

MorseParser::MorseParser() = default;

string MorseParser::parseMorse(vector<int> morse) {
    string result;
    vector<vector<int>> letters;
    int marker = 0;
    for (int i1 = 0; i1 < morse.size()-5; ++i1) {
        if ((morse[i1+1] == 0 && morse[i1+2] == 0 && morse[i1+3] == 0 && morse[i1+4] == 1)) {
            letters.emplace_back(morse.begin()+marker, morse.begin()+i1+1);
            marker = i1+4;
        }
        if ((morse[i1+1] == 0 && morse[i1+2] == 0 && morse[i1+3] == 0 && morse[i1+4] == 0 && morse[i1+5] == 0)) {
            letters.emplace_back(morse.begin()+marker, morse.begin()+i1+1);
            letters.push_back({0, 0});
            marker = i1+6;
            i1+=4;
        }
    }
    for (auto& letter: letters) {
        if (letter == vector{0, 0}) {
            result+=' ';
        } else if (letter == this->a) {
            result+='a';
        } else if (letter == this->b) {
            result+='b';
        } else if (letter == this->c) {
            result+='c';
        } else if (letter == this->d) {
            result+='d';
        } else if (letter == this->e) {
            result+='e';
        } else if (letter == this->f) {
            result+='f';
        } else if (letter == this->g) {
            result+='g';
        } else if(letter == this->h) {
            result+='h';
        } else if(letter == this->i) {
            result+='i';
        } else if(letter == this->j) {
            result+='j';
        } else if(letter == this->k) {
            result+='k';
        } else if(letter == this->l) {
            result+='l';
        } else if(letter == this->m) {
            result+='m';
        } else if(letter == this->n) {
            result+='n';
        } else if(letter == this->o) {
            result+='o';
        } else if(letter == this->p) {
            result+='p';
        } else if(letter == this->q) {
            result+='q';
        } else if(letter == this->r) {
            result+='r';
        } else if(letter == this->s) {
            result+='s';
        } else if(letter == this->t) {
            result+='t';
        } else if(letter == this->u) {
            result+='u';
        } else if(letter == this->v) {
            result+='v';
        } else if(letter == this->w) {
            result+='w';
        } else if(letter == this->x) {
            result+='x';
        } else if(letter == this->y) {
            result+='y';
        } else if(letter == this->z) {
            result+='z';
        }
    }
    return result;
}