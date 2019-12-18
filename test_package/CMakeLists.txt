project(PackageTest CXX)
cmake_minimum_required(VERSION 2.8.12)


find_package(meteoio REQUIRED)

add_executable(test test.cpp)
target_link_libraries(test meteoio::meteoio)
set_target_properties(test
    PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin"
    )
