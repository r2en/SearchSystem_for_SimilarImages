#coding:utf-8
import codecs
import os

TARGET = "caltech101"
OUTDIR = "hist"

for file in os.listdir(TARGET):
    image_file = "%s/%s" % (TARGET, file)          # caltech101/xxx.jpg
    hist_file = "%s/%s.hst" % (OUTDIR, file[:-4])  # hist/xxx.hst
    os.system("python sample.py %s %s" % (image_file, hist_file))