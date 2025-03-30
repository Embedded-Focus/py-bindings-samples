cmake_minimum_required(VERSION 3.14)
project(geometry VERSION 0.1.0 LANGUAGES C CXX)

add_library(geometry SHARED
  geometry.cpp
  geometry_wrap.cpp)
target_include_directories(geometry PUBLIC ${CMAKE_CURRENT_LIST_DIR})
