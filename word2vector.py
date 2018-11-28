# coding=utf-8

import sys
from random import shuffle
import multiprocessing
import gensim


if __name__ == "__main__":
    with open("./course_recommend_data.csv") as f:
        user_list = []
        course_list = []
        for line in f.readlines():
            try:
                course_list.append(line.strip().split("\t"))
            except Exception as e:
                print e

    model = gensim.model.Word2Vec(sentences=)