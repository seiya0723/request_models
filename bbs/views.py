from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render
from django.views import View

class BbsView(View):

    def get(self, request, *args, **kwargs):

        #予めifでname属性の値が存在するかチェックする。
        if "search" in request.GET:

            #TODO:実際にはここでDBに検索処理を実行する。
            print(request.GET["search"])




        topics = [
            {"id": "1", "comment": "Hello!!","prime": True},
            {"id": "2", "comment": "こんにちは","prime": True},
            {"id": "3", "comment": "やあ","prime": False},
            {"id": "4", "comment": "こんにちは", "prime": True},
            {"id": "5", "comment": "こんにちは", "prime": True},
            {"id": "6", "comment": "こんにちは", "prime": True},
        ]
        data = "test"
        button1 = "Prev"
        context = {"data": data,
                   "topics":topics,
                   "button1":button1
                   }

        return render(request,"bbs/index.html",context)

    
    def post(self, request, *args, **kwargs):

        #予めifでname属性の値が存在するかチェックする。
        if "message" in request.POST:

            #TODO:実際にはここでDBにデータを保存する。
            print(request.POST["message"])


        #トップページにリダイレクト。urls.pyのname、app_nameで指定した値が使える。
        return redirect("bbs:index")


index   = BbsView.as_view()
