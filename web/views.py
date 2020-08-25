from django.shortcuts import render
from utils.auth import check_login
from repository import models
# Create your views here.

@check_login
def index(request):
    # print(request.session.get('user_info'))
    #     博客首页，展示全部博文
    #     :param request:
    #     :return:
    #     """
    #     # return render(request,'index.html')
    #     # 获取文章类型
    article_type_list = models.Article.type_choices
    print(article_type_list)
    return render(request,"index.html",{"article_type_list":article_type_list,})

# from django.shortcuts import render
# from django.shortcuts import redirect
# from repository import models
# # from utils.pagination import Pagination
# from django.urls import reverse

# def index(request, *args, **kwargs):
#     """
#     博客首页，展示全部博文
#     :param request:
#     :return:
#     """
#     # return render(request,'index.html')
#     # 获取文章类型
#     article_type_list = models.Article.type_choices
#     # {},[]
#     if kwargs:
#         article_type_id = int(kwargs['article_type_id'])
#         base_url = reverse('index',kwargs=kwargs)#   all/1.html
#     else:
#         article_type_id = None
#         base_url = '/' # /
#
#     data_count = models.Article.objects.filter(**kwargs).count()
#
#
#     # page_obj = Pagination(request.GET.get('p'),data_count)
#     article_list = models.Article.objects.filter(**kwargs).order_by('-nid')[page_obj.start:page_obj.end]
#     page_str = page_obj.page_str(base_url)
#
#     return render(
#         request,
#         'index.html',
#         {
#             'article_list': article_list,
#             'article_type_id': article_type_id,
#             'article_type_list': article_type_list,
#             'page_str': page_str,
#         }
#     )
