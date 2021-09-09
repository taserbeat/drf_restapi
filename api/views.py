from .models import Task, Tag
from rest_framework import viewsets
from .serializers import TaskSerializer, TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    """
    タグモデルのビューセット

    viewsets.ModelViewSetを継承されているので、タグモデルに対するCRUD操作を提供する。
    """

    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    """
    タスクモデルのビューセット

    タスクモデルに対するCRUD操作を提供する。
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
