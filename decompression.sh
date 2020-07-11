#!/usr/bin/bash

data_path=${1}

for file in $(ls ${data_path}/)
do
    echo ${file}
    name=${file%%.*}
    if [ ! -d ${data_path}/${name} ]; then
        echo "${data_path}/${name} is not existed, so we create it."
        mkdir ${data_path}/${name}
    fi
    gunzip -nv ${data_path}/${file}
    if [ -f ${data_path}/${file%.*} ]; then
        mv ${data_path}/${file%.*} ${data_path}/${name}
    else
        echo "no such file"
        exit
    fi
done

