from rest_framework import mixins, viewsets


class CreateListDestroyMixin(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
):
    pass
