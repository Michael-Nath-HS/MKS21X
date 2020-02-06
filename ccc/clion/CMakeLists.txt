cmake_minimum_required(VERSION 3.15)
project(clion)

set(CMAKE_CXX_STANDARD 17)

add_executable(clion main.cpp)
add_executable(Chap1 chap1/printname.cpp)
add_executable(Chap1Loop chap1/loop.cpp)
add_executable(AllOdd chap1/odd.cpp chap1/odd.cpp)
add_executable(String chap3/string.cpp)
add_executable(Algo algo algo/simple_array_sum.cpp algo/simple_array_sum.cpp algo/compare_the_triplets.cpp algo/a_very_big_sum.cpp algo/diagonal_difference.cpp)