cmake_minimum_required(VERSION 3.23)
project(toonpp)

set(CMAKE_CXX_STANDARD 20)

include_directories("C:\\Program Files\\Python39\\include")

add_library(toonpp SHARED toonpp.cpp ida.h)
target_link_directories(toonpp PRIVATE libs "C:\\Program Files\\Python39\\libs")