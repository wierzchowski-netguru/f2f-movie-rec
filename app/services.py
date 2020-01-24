from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from surprise import KNNWithMeans
import pandas as pd

from surprise import Dataset
from surprise import Reader


class RecommendationService:
    @classmethod
    def train(cls, ratings_dict):
        # Load dataset movie_id:user_id_rating
        df = pd.DataFrame(ratings_dict)

        # A reader is still needed but only the rating_scale param is requiered.
        reader = Reader(rating_scale=(1, 5))

        # The columns must correspond to user id, item id and ratings (in that order).
        data = Dataset.load_from_df(df[['user_id', 'movie_id', 'rating']], reader)

        trainset = data.build_full_trainset()

        # Use user_based true/false to switch between user-based or item-based collaborative filtering
        # https://surprise.readthedocs.io/en/stable/knn_inspired.html#surprise.prediction_algorithms.knns.KNNWithMeans
        algo = KNNWithMeans(k=5, sim_options={'name': 'pearson_baseline', 'user_based': False})
        print(f">>> trained algorithm")
        return algo.fit(trainset)

    @classmethod
    def rate(cls, trained_algorithm, movie_id, user_id):
        # get a prediction for specific users and items.
        pred = trained_algorithm.predict(user_id, movie_id, verbose=True)
        if not pred.details['was_impossible']:
            return round(pred.est, 2)
        return 'n/a'
