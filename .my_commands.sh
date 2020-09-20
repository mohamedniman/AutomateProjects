#!/bin/bash

function create() {
    cd ~
    locatedir='~/Documents/Projects/MyProjects/$1'
    if [ ! -d $locatedir ]; then
        python3 create.py $1
        cd Documents/Projects/MyProjects
        mkdir $1
        cd $1
        git init
        git remote add origin git@github.com:mohamedniman/$1.git
        touch README.md
        git add .
        git commit -m "Initial commit"
        git push -u origin master
        code .
    else echo " FolderName Already Exist :( "
    fi
    
    #mkdir $1
}