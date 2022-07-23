from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from reviews.models import Review
from reviews.permissions import OwnResourcePermission
from titles.models import Title
from .serializers import ReviewSerializer, CommentSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """Вывод отзывов."""
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    """Вывод коментов на отзыв."""
    serializer_class = CommentSerializer
    permission_classes = (OwnResourcePermission,)

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(
            review=review, author=self.request.user)
