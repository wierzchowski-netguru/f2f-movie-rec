## Movie recommendation ##

Movie recommendation sample project utilizing [Surprise](https://surprise.readthedocs.io/en/) library. 

### Installation & run: ### 
* install dependencies with provided requirements.txt file, user prvided sqlite db
* create users / movies / ratings in Django admin [http://localhost:8000/admin/](http://localhost:8000/admin/)
* view table with ratings and predictions [http://localhost:8000/](http://localhost:8000/)

### Remarks: ###
* algorithm used for recommendation is [KNNWithMeans](https://surprise.readthedocs.io/en/stable/knn_inspired.html#surprise.prediction_algorithms.knns.KNNWithMeans)
* app uses sqlite, it is enough for the sake of configuration simplicity
* sample data provided as fixtures (3 users / 4 movies)
* no login in Django admin is required: custom middleware automatically logs in as `.first()` user
* in table with results, red value is calculated, black are provided in db

