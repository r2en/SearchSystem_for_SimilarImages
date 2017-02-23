#coding:utf-8
import codecs
import cv2
import os
import sys
import math
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

IMAGE_DIR = "caltech101"
HIST_DIR = "hist"

def load_hist():
    hist = {}
    for file in os.listdir(HIST_DIR):
        h = []
        print "load %s ... " % file,
        fp = open("%s/%s" % (HIST_DIR, file), "r")
        for line in fp:
            line = line.rstrip()
            h.append(int(line))
        fp.close()
        hist[file] = h
        print "OK"
    return hist

def calc_hist_intersection(hist1, hist2):
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE,tree = 5)
    search_params = dict(check=50)
    flann = cv2.FlannBasedMatcher(index_params,search_params)
    matches = flann.knnMatch(hist1,hist2,k=2)
    return matches

def main():
    hist = load_hist()
    while True:
        query_file = raw_input("query? > ")
        
        if query_file == "quit":
            break
        
        if not hist.has_key(query_file):
            print "no histogram"
            continue
        
        result = []
        e1 = cv2.getTickCount()
        query_hist = hist[query_file]
        for target_file in hist.keys():
            target_hist = hist[target_file]
            d = calc_hist_intersection(query_hist, target_hist)
            result.append((d, target_file))
        e2 = cv2.getTickCount()
        t = (e2 - e1)/cv2.getTickFrequency()
        print "second : " + str(t)

        result.sort()#reverse=True)

        p = 0
        canvas = Image.new("RGB", (6000, 600), (255,255,255))  # 白いキャンバス
        for score, filename in result[0:40]:
            print "%f\t%s" % (score, filename)
            img = Image.open("caltech101/" + filename[:-4] + ".jpg")
            pos = (300*(p%20), 300*(p/20))
            canvas.paste(img, pos)
            p += 1
        canvas.resize((6000/2, 600/2))
        canvas.show()
        canvas.save(query_file + ".jpg", "JPEG")

if __name__ == "__main__":
    e1 = cv2.getTickCount()
    main()
    e2 = cv2.getTickCount()
    t = (e2 - e1)/cv2.getTickFrequency()
    print "second : " + str(t)
