cmake_minimum_required(VERSION 3.10)
project(bt_task)

find_package(behaviortree_cpp REQUIRED)

add_executable(bt main.cpp)

target_link_libraries(bt behaviortree_cpp)