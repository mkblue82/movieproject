from django.contrib import admin
# CustomUserをインポート
from .models import Category, MoviePost, MovieToWatch

# 管理ページのレコード一覧に表示するカラムを設定するクラス
class CategoryAdmin(admin.ModelAdmin):
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')


# 管理ページのレコード一覧に表示するカラムを設定するクラス
class MoviePostAdmin(admin.ModelAdmin):
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')


# 管理ページのレコード一覧に表示するカラムを設定するクラス
class MovieToWatchAdmin(admin.ModelAdmin):
    # レコード一覧にidとtitleを表示
    list_display = ('id', 'title')
    # 表示するカラムにリンクを設定
    list_display_links = ('id', 'title')


# Django管理サイトにCategory、CategoryAdminを登録する
admin.site.register(Category, CategoryAdmin)

# Django管理サイトにMoviePost、MoviePostAdminを登録する
admin.site.register(MoviePost, MoviePostAdmin)

# Django管理サイトにMovieToWatch、MovieToWatchAdminを登録する
admin.site.register(MovieToWatch, MovieToWatchAdmin)