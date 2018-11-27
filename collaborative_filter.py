# -*- coding=utf-8 -*-

from surprise import KNNBaseline, Reader
from surprise import SVD,evaluate,NMF,NormalPredictor, BaselineOnly, KNNBasic, KNNWithMeans,KNNBaseline,SVDpp
from surprise import Dataset

file_path = './course_recommend_data.csv'
reader = Reader(line_format='user item rating timestamp', sep='\t')
recommend_data = Dataset.load_from_file(file_path, reader=reader)

#trainset = recommend_data.build_full_trainset()
#
#algo = KNNBaseline()
#algo.train(trainset)
#
#inner_iid = algo.trainset.to_inner_iid("54480")
#
#inner_course_id_list = algo.get_neighbors(inner_iid, k=20)
#
#for inner_iid in inner_course_id_list:
#    try:
#        print algo.trainset.to_raw_iid(inner_iid)
#    except Exception as e:
#        continue
algo = SVDpp()
all_trainset = recommend_data.build_full_trainset()

algo.fit(all_trainset)
course_id = '55446'
course_iid = algo.trainset.to_inner_iid(course_id)
course_neighbors = algo.get_neighbors(course_iid, k=20)
course_ids = (algo.trainset.to_raw_iid(inner_id) for inner_id in course_neighbors)
print list(course_ids)


#evaluate(algo, recommend_data, measures=['RMSE', 'MAE'])
