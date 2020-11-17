#!/usr/bin/python3

import os

with open('deck.md') as f:
    lines = f.readlines()

mydir = './_slides_test'
filelist = [ f for f in os.listdir(mydir) if f.endswith(".md") ]
for f in filelist:
    os.remove(os.path.join(mydir, f))

notesdir = './_notes'
filelist = [ f for f in os.listdir(notesdir) if f.endswith(".md") ]
for f in filelist:
    os.remove(os.path.join(notesdir, f))



commentFlag = False

file_number = 0
slide_file = (f"./_slides_test/{file_number:02d}-slide.md")
f = open(slide_file,"w+")
f.write('---\n')
f.write('layout: default\n')
f.write('---\n')

slide_file = (f"./_notes/{file_number:02d}-notes.md")
fn = open(slide_file,"w+")
fn.write('---\n')
fn.write('layout: default\n')
fn.write('---\n')

topFlag = True


for l in lines:

    if (l.rstrip() == "{% endcomment %}"):
        commentFlag = False



    if (l.rstrip() == "---------------------------------------------------------------------------------------------------------------------------------"):
        f.close()
        file_number +=1

        slide_file = (f"./_slides_test/{file_number:02d}-slide.md")
        f = open(slide_file,"w+")
        f.write('---\n')
        f.write('layout: default\n')
        f.write('---\n')

        fn.close()
        slide_file = (f"./_notes/{file_number:02d}-notes.md")
        fn = open(slide_file,"w+")
        fn.write('---\n')
        fn.write('layout: default\n')
        fn.write('---\n')

        topFlag = True


    else:
        f.write(l)
        if commentFlag or (l[0] == "#" and topFlag):
            fn.write(l)
            topFlag = False

    if (l.rstrip() == "{% comment %}"):
        commentFlag = True
