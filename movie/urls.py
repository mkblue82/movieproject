from django.urls import path
from . import views

# URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name = 'movie'

# URLパターンを登録するためのリスト
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('movie_to_watch_list/', views.WatchListView.as_view(), name='watchlist'),
    path('review_list/', views.ReviewListView.as_view(), name='reviewlist'),
    path('post/', views.CreateMovieView.as_view(), name='post'),
    path('post_done/', views.PostSuccessView.as_view(), name='post_done'),
    path('post_movietowatch/', views.CreateMovieToWatchView.as_view(), name='post_movie_to_watch'),
    path('post_movietowatch_done/', views.MovieToWatchSuccessView.as_view(), name='post_movie_to_watch_done'),
    path('movie/<int:category>', views.CategoryView.as_view(), name='movies_cat'),
    path('user-list/<int:user>', views.UserView.as_view(), name='user_list'),
    path('movie-detail/<int:pk>', views.DetailView.as_view(), name='movie_detail'),
    path('watch_list-detail/<int:pk>', views.WatchListDetailView.as_view(), name='watchlist_detail'),
    path('mypage/', views.MypageView.as_view(), name='mypage'),
    path('movie/<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie_delete'),
    path('movie_delete_done/', views.MovieDeleteSuccessView.as_view(), name='movie_delete_done'),
    path('watch_list/<int:pk>/delete/', views.WatchListDeleteView.as_view(), name='watchlist_delete'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]