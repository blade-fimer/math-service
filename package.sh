#!/bin/bash

APP=$0
APP=${APP##*/}

BUILD_DIR='math_service'

usage()
{
    echo "usage: ${APP}"
    echo "###### Build the package"
    echo
}

build()
{
    echo "###### Packaging ######"
    cd `dirname $0`
    mkdir -p $BUILD_DIR
    rm -rf $BUILD_DIR/*
    cp -r install math_service.py v1/ $BUILD_DIR
    tar -czvf math_service.tar.gz $BUILD_DIR
    rm -rf $BUILD_DIR
}

if [ $# -gt 0 ]; then
    usage
    exit 0
fi

build
exit 0
