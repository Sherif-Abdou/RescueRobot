cmake_minimum_required(VERSION 3.12)
project(Morse)

set(CMAKE_CXX_STANDARD 17)

add_executable(Morse main.cpp MorseParser.cpp MorseParser.h)