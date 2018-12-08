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

vector<int> MorseParser::toMorse(string message) {
    auto morse = vector<int>();
    vector<int> letterspace = {0, 0, 0};
    vector<int> ending = {0, 0};
    for (auto& character: message) {
        if (character == ' ') {
            morse.insert(morse.end(), ending.begin(), ending.end());
            continue;
        }
        switch (character) {
            case 'a':
                morse.insert(morse.end(), this->a.begin(), this->a.end());
                break;
            case 'b':
                morse.insert(morse.end(), this->b.begin(), this->b.end());
                break;
            case 'c':
                morse.insert(morse.end(), this->c.begin(), this->c.end());
                break;
            case 'd':
                morse.insert(morse.end(), this->d.begin(), this->d.end());
                break;
            case 'e':
                morse.insert(morse.end(), this->e.begin(), this->e.end());
                break;
            case 'f':
                morse.insert(morse.end(), this->f.begin(), this->f.end());
                break;
            case 'h':
                morse.insert(morse.end(), this->h.begin(), this->h.end());
                break;
            case 'i':
                morse.insert(morse.end(), this->i.begin(), this->i.end());
                break;
            case 'j':
                morse.insert(morse.end(), this->j.begin(), this->j.end());
                break;
            case 'k':
                morse.insert(morse.end(), this->k.begin(), this->k.end());
                break;
            case 'l':
                morse.insert(morse.end(), this->l.begin(), this->l.end());
                break;
            case 'm':
                morse.insert(morse.end(), this->m.begin(), this->m.end());
                break;
            case 'n':
                morse.insert(morse.end(), this->n.begin(), this->n.end());
                break;
            case 'o':
                morse.insert(morse.end(), this->o.begin(), this->o.end());
                break;
            case 'p':
                morse.insert(morse.end(), this->p.begin(), this->p.end());
                break;
            case 'q':
                morse.insert(morse.end(), this->q.begin(), this->q.end());
                break;
            case 'r':
                morse.insert(morse.end(), this->r.begin(), this->r.end());
                break;
            case 's':
                morse.insert(morse.end(), this->s.begin(), this->s.end());
                break;
            case 't':
                morse.insert(morse.end(), this->t.begin(), this->t.end());
                break;
            case 'u':
                morse.insert(morse.end(), this->u.begin(), this->u.end());
                break;
            case 'v':
                morse.insert(morse.end(), this->v.begin(), this->v.end());
                break;
            case 'w':
                morse.insert(morse.end(), this->w.begin(), this->w.end());
                break;
            case 'x':
                morse.insert(morse.end(), this->x.begin(), this->x.end());
                break;
            case 'y':
                morse.insert(morse.end(), this->y.begin(), this->y.end());
                break;
            case 'z':
                morse.insert(morse.end(), this->z.begin(), this->z.end());
                break;
        }
        morse.insert(morse.end(), letterspace.begin(), letterspace.end());
    }
    morse.insert(morse.end(), ending.begin(), ending.end());
    return morse;
}
