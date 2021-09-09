from rest_framework import serializers
from .models import Task, Tag


class TagSerializer(serializers.ModelSerializer):
    """
    タグモデルのシリアライザー
    """

    class Meta:
        """
        シリアライズ対象のモデルとフィールド名
        """
        model = Tag
        fields = ('id', 'name')


class TaskSerializer(serializers.ModelSerializer):
    """
    タスクモデルのシリアライザー
    """

    # 日時の文字列フォーマット
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S.%f', read_only=True)
    updated_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S.%f', read_only=True)

    # Tagオブジェクトを参照したときにidだけではなくnameも取得できるようにする
    tag_name = serializers.ReadOnlyField(source='tag.name', read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'created_at', 'updated_at', 'tag', 'tag_name')
