# Filter for word app
# 最终的版本:ModelViewSet
# 自定义分页器配置
from deprecated.classic import deprecated
from rest_framework.pagination import PageNumberPagination


@deprecated
class DIYPagination(PageNumberPagination):
    page_query_param = 'pager'  # 默认是page
    page_size = 5  # 每一页可以显示的条数
    max_page_size = 50  # 前端最多可以请求到第50页
