from django.db import models

# Create your models here.
from accounts.models import CustomUser

# 映画のカテゴリを管理するモデル
class Category(models.Model):
    # カテゴリ名のフィールド
    title = models.CharField(verbose_name = 'カテゴリ', max_length = 20)

    def __str__(self):
        # オブジェクトを文字列に変換して返す
        return self.title


# 投稿されたデータを管理するモデル
class MoviePost(models.Model):
    # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
    user = models.ForeignKey(CustomUser, verbose_name = 'ユーザー', on_delete = models.CASCADE)
    # カテゴリに関連付けられた投稿データが存在する場合は、そのカテゴリを削除できないようにする
    category = models.ForeignKey(Category, verbose_name = 'カテゴリ', on_delete = models.PROTECT)

    # タイトル用のフィールド
    title = models.CharField(verbose_name = 'タイトル', max_length = 200)
    # 本文テキスト用のフィールド
    comment = models.TextField(verbose_name = 'コメント',)
    # イメージのフィールド
    image = models.ImageField(verbose_name = 'イメージ', upload_to = 'movie')
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(verbose_name = '投稿日時', auto_now_add = True)

    def __str__(self):
        # オブジェクトを文字列にして返す
        return self.title


# 観たい映画として登録されたデータを管理するモデル
class MovieToWatch(models.Model):
    # ユーザーを削除する場合はそのユーザーの投稿データもすべて削除する
    user = models.ForeignKey(CustomUser, verbose_name = 'ユーザー', on_delete = models.CASCADE)
    # カテゴリに関連付けられた投稿データが存在する場合は、そのカテゴリを削除できないようにする
    category = models.ForeignKey(Category, verbose_name = 'カテゴリ', on_delete = models.PROTECT)

    # タイトル用のフィールド
    title = models.CharField(verbose_name = 'タイトル', max_length = 200)
    # 本文テキスト用のフィールド
    comment = models.TextField(verbose_name = 'コメント',)
    # イメージのフィールド
    image = models.ImageField(verbose_name = 'イメージ', upload_to = 'movie')
    # 投稿日時のフィールド
    posted_at = models.DateTimeField(verbose_name = '投稿日時', auto_now_add = True)

    def __str__(self):
        # オブジェクトを文字列にして返す
        return self.title