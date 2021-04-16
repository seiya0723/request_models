from django.db import models
from django.utils import timezone

# Create your models here.
class Topic(models.Model):

    #テーブル名
    class Meta:
        db_table    = "topic"

    #カラム名とルール
    dt      = models.DateTimeField(verbose_name="投稿日",default=timezone.now)
    comment = models.CharField(verbose_name="コメント",max_length=200)

    #管理画面を表示した時にコメントを表示させる
    def __str__(self):
        return self.comment
