# Copyright (C) 2020-2023 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
#

file(GLOB MAIN_SRC ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp)
file(GLOB MAIN_HEADERS ${CMAKE_CURRENT_SOURCE_DIR}/*.h*)

add_demo(NAME interactive_face_detection_demo_gapi
    SOURCES ${MAIN_SRC}
    HEADERS ${MAIN_HEADERS}
    DEPENDENCIES monitors utils_gapi
    OPENCV_VERSION_REQUIRED 4.5.3)
