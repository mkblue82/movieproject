from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import MoviePostForm, MovieToWatchForm, ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import MoviePost, MovieToWatch
from django.views.generic import DetailView
from django.views.generic import DeleteView


class IndexView(ListView):
    template_name = 'index.html'
    # 投稿日時の降順で並び替える
    queryset = MoviePost.objects.order_by('-posted_at')
    # 1ページに表示するレコードの数
    paginate_by = 6



# 映画レビュー投稿ページのビュー
# ビューに対してログイン必須を設定
@method_decorator(login_required, name='dispatch')
class CreateMovieView(CreateView):
    # forms.pyのMoviePostFormをフォームクラスとして登録
    form_class = MoviePostForm
    # レンダリングするテンプレート
    template_name = 'post_movie.html'
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('movie:post_done')

    # CreateViewクラスのform_valid()をオーバーライド
    def form_valid(self, form):
        # Commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)


# 観たい映画登録ページのビュー
@method_decorator(login_required, name='dispatch')
class CreateMovieToWatchView(CreateView):
    # forms.pyのMovieToWatchFormをフォームクラスとして登録
    form_class = MovieToWatchForm
    # レンダリングするテンプレート
    template_name = 'post_movie_to_watch.html'
    # フォームデータ登録完了後のリダイレクト先
    success_url = reverse_lazy('movie:post_movie_to_watch_done')

    # CreateViewクラスのform_valid()をオーバーライド
    def form_valid(self, form):
        # Commit=FalseにしてPOSTされたデータを取得
        postdata = form.save(commit=False)
        # 映画登録ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 映画登録データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)


# 投稿完了ページのビュー
class PostSuccessView(TemplateView):
    # post_success.htmlをレンダリングする
    template_name = 'post_success.html'


# 観たい映画登録完了ページのビュー
class MovieToWatchSuccessView(TemplateView):
    # post_movie_to_watch_success.htmlをレンダリングする
    template_name = 'post_movie_to_watch_success.html'


# カテゴリページのビュー
class CategoryView(ListView):
    # index.htmlをレンダリングする
    template_name = 'index.html'
    # 1ページに表示するレコードの件数
    paginate_by = 6

    # クエリを実行する
    def get_queryset(self):
        category_id = self.kwargs['category']
        print(f'Category ID:{category_id}')
        categories = MoviePost.objects.filter(category=category_id).order_by('-posted_at')
        print(f'Filtered categories:{categories}')
        return categories


# ユーザーの投稿一覧ページのビュー
class UserView(ListView):
    # index.htmlをレンダリングする
    template_name = 'index.html'
    # 1ページに表示するレコードの件数
    paginate_by = 6

    # クエリを実行する
    def get_queryset(self):
        user_id = self.kwargs['user']
        user_list = MoviePost.objects.filter(user=user_id).order_by('-posted_at')
        return user_list


# 詳細ページのビュー
class DetailView(DetailView):
    # detail.htmlをレンダリングする
    template_name = 'detail.html'
    # クラス変数modelにモデルMoviePostを設定
    model = MoviePost


# ウォッチリストの詳細ページのビュー
class WatchListDetailView(DetailView):
    # watch_list_detail.htmlをレンダリングする
    template_name = 'watch_list_detail.html'
    # クラス変数modelにMovieToWatchを設定
    model = MovieToWatch


# マイページのビュー
class MypageView(TemplateView):
    # mypage.htmlをレンダリングする
    template_name = 'mypage.html'


# ログイン中ユーザーのレビュー投稿一覧のビュー
class ReviewListView(ListView):
    # review_list.htmlをレンダリングする
    template_name = 'review_list.html'
    # 1ページに表示するレコードの件数
    paginate_by = 10

    # クエリを実行する
    def get_queryset(self):
        queryset = MoviePost.objects.filter(user=self.request.user).order_by('-posted_at')
        return queryset


# ログイン中ユーザーのウォッチリスト一覧のビュー
class WatchListView(ListView):
    # watch_list.htmlをレンダリングする
    template_name = 'watch_list.html'
    # 1ページに表示するレコードの件数
    paginate_by = 10

    # クエリを実行する
    def get_queryset(self):
        queryset = MovieToWatch.objects.filter(user=self.request.user).order_by('-posted_at')
        return queryset



# レコードの削除を行うビュー
class MovieDeleteView(DeleteView):
    model = MoviePost
    template_name = 'movie_delete.html'
    success_url = reverse_lazy('movie:movie_delete_done')

    # レコードの削除を行う
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# ウォッチリストのレコードの削除を行うビュー
class WatchListDeleteView(DeleteView):
    model = MovieToWatch
    template_name = 'watchlist_delete.html'
    success_url = reverse_lazy('movie:movie_delete_done')

    # レコードの削除を行う
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# 投稿削除完了ページのビュー
class MovieDeleteSuccessView(TemplateView):
    # delete_success.htmlをレンダリングする
    template_name = 'delete_success.html'


# お問い合わせのビュー
class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('movie:contact')
    
    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']

        subject = 'お問い合わせ：{}'.format(title)
        message = \
            '送信者名：{0}\nメールアドレス：{1}\n タイトル：{2}\n メッセージ：\n{3}' \
            .format(name, email, title, message)
        from_email = 'mmr2482lk@gmail.com'
        to_list = ['mmr2482lk@gmail.com']

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list)
        message.send()

        messages.success(self.request, 'お問い合わせは正常に送信されました。')

        return super().form_valid(form)