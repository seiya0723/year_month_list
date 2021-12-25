from django.shortcuts import render,redirect

from django.views import View
from .models import Topic
from .forms import TopicForm,YearMonthForm

class BbsView(View):

    def get(self, request, *args, **kwargs):

        context = {}

        form    = YearMonthForm(request.GET)

        if form.is_valid():
            cleaned = form.clean()

            context["topics"]    = Topic.objects.filter(dt__year=cleaned["year"],dt__month=cleaned["month"]).order_by("-dt")
        else:
            context["topics"]    = Topic.objects.order_by("-dt")



        #月別アーカイブの表示
        #最新と最古のデータを手に入れる。
        newest  = Topic.objects.order_by("-dt").first()
        oldest  = Topic.objects.order_by("dt").first()

        year_month_list = []

        if newest and oldest:

            newest_dt   = newest.dt
            now_year    = oldest.dt.year
            now_month   = oldest.dt.month

            #TODO:最古から1ヶ月ずつずらして最新になったら終わり
            while True:
                year_month          = {}
                year_month["link"]  = "?year=" + str(now_year) + "&month=" + str(now_month)
                year_month["label"] = str(now_year) + "年" + str(now_month) + "月"

                copied              = year_month.copy()

                year_month_list.append(copied)

                if now_month >= newest_dt.month and now_year >= newest_dt.year:
                    break
                else:
                    if now_month == 12:
                        now_year += 1
                        now_month = 1
                    else:
                        now_month += 1

        context["year_month_list"]  = year_month_list


        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        form    = TopicForm(request.POST)
        
        if form.is_valid():
            form.save()

        print(form.errors)

        return redirect("bbs:index")

index   = BbsView.as_view()

