#!/usr/bin/python3

import os

with open('deck.md') as f:
    lines = f.readlines()

mydir = './_slides_test'
filelist = [ f for f in os.listdir(mydir) if f.endswith(".md") ]
for f in filelist:
    os.remove(os.path.join(mydir, f))

file_number = 0
slide_file = (f"./_slides_test/{file_number}-slide.md")
f = open(slide_file,"w+")
f.write('---\n')
f.write('layout: default\n')
f.write('---\n')

for l in lines:
    if (l.rstrip() == "---------------------------------------------------------------------------------------------------------------------------------"):
        f.close()
        file_number +=1
        slide_file = (f"./_slides_test/{file_number:02d}-slide.md")
        f = open(slide_file,"w+")
        f.write('---\n')
        f.write('layout: default\n')
        f.write('---\n')
    else:
        f.write(l)
