from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

# Create your views here.

# サインアップページのビュー
class SignUpView(CreateView):

    # forms.pyで定義したフォームのクラス
    form_class = CustomUserCreationForm
    # レンダリングするテンプレート
    template_name = 'signup.html'
    # サインアップ完了後のリダイレクト先のURLパターン
    success_url = reverse_lazy('accounts:signup_success')

    # CreateViewクラスのform_valid()をオーバーライドする
    def form_valid(self, form):
        # formオブジェクトのフィールドの値をデータベースに保存
        user = form.save()
        self.object = user
        # 戻り値は基底クラスのform_valid()の戻り値
        return super().form_valid(form)


# サインアップ完了ページのビュー
class SignUpSuccessView(TemplateView):
    template_name = 'signup_success.html'