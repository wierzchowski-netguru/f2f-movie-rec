from django.views.generic import TemplateView

from app.models import Movie, User, Rating
from app.services import RecommendationService


class MovieTemplateView(TemplateView):
    template_name = "movies.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ratings'] = self.get_ratings_matrix(
            movies=Movie.objects.all(),
            users=User.objects.all()
        )
        # for the sake of simplicity just show all records for movies and users,
        # this could be problematic with larger sets of data if not optimized
        return context

    def get_ratings_matrix(self, movies, users):
        ratings = Rating.objects.filter(movie__in=movies, user__in=users).select_related('movie', 'user')
        matrix = [[('', '')]]  # first empty cell in table, intersection of column and row names

        [matrix[0].append((movie.name, '')) for movie in movies]

        ratings_dict = {
            'movie_id': [],
            'user_id': [],
            'rating': []
        }

        # create dict, to be used as feed for recommendation algorithm
        for rating in ratings:
            ratings_dict['movie_id'].append(rating.movie.id)
            ratings_dict['user_id'].append(rating.user.id)
            ratings_dict['rating'].append(rating.rating)

        # train once, use multiple times
        trained_algorithm = RecommendationService.train(ratings_dict)

        for user in users:
            matrix.append([(user.username, '')])
            for movie in movies:
                item = ratings.filter(user=user, movie=movie).first()
                if item:
                    matrix[-1].append((item.rating, 'rated'))
                else:
                    matrix[-1].append((RecommendationService.rate(trained_algorithm, movie.id, user.id), 'calculated'))
        return matrix
