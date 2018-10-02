from django.shortcuts import render
from django.views.generic import View
from pure_pagination import PageNotAnInteger, EmptyPage, Paginator
from .models import CourseOrg, CityDict


class OrgView(View):
    """
    课程机构列表功能
    """
    def get(self, request):
        # 课程机构
        all_orgs = CourseOrg.objects.all()
        all_nums = all_orgs.count()
        #城市
        all_citys = CityDict.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)
        return render(request, "org-list.html", {
            "all_orgs": orgs,
            "all_citys":all_citys,
            "all_nums": all_nums,
        })