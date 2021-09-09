from django.db import models


class Tag(models.Model):
    """
    タグモデル
    """

    name = models.CharField(max_length=100)
    """
    名前
    """

    def __str__(self):
        """
        インスタンス名
        """

        return self.name


class Task(models.Model):
    """
    タスクモデル
    """

    title = models.CharField(max_length=100)
    """
    タイトル
    """

    created_at = models.DateTimeField(auto_now_add=True)
    """
    作成日時
    """

    updated_at = models.DateTimeField(auto_now=True)
    """
    更新日時
    """

    tag = models.ForeignKey(Tag, null=True, on_delete=models.CASCADE)
    """
    タグ
    """

    def __str__(self):
        """
        インスタンス名
        """
        return self.title
