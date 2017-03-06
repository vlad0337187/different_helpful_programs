#! /bin/bash

cd '/home/vlad/Programs/my_projects/different_helpful_programs'
hg status
hg commit
hg bookmark -r default master
hg push git+ssh://git@github.com/vlad1777d/different_helpful_programs.git
