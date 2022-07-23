from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (TitlesViewSet, CategoryViewSet,
                    GenreViewSet, ReviewViewSet,
                    CommentViewSet, signup_post,
                    token_post, UserViewSet)

app_name = 'api'

router_ver1 = DefaultRouter()
router_ver1.register(r'users', UserViewSet, basename='user')
router_ver1.register(r'titles', TitlesViewSet, basename='title')
router_ver1.register(r'categories', CategoryViewSet, basename='category')
router_ver1.register(r'genres', GenreViewSet, basename='genre')
router_ver1.register(
    r'titles/(?P<title_id>[\d]+)/reviews',
    ReviewViewSet,
    basename='review'
)
router_ver1.register(
    r'titles/(?P<title_id>[\d]+)/reviews/(?P<review_id>[\d]+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('v1/', include(router_ver1.urls)),
    path('v1/auth/token/', token_post, name='get_token'),
    path('v1/auth/signup/', signup_post, name='register'),
]
