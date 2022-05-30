# Filter for word app
# 最终的版本:ModelViewSet
# 自定义分页器配置
from deprecated.classic import deprecated
from rest_framework.pagination import PageNumberPagination


@deprecated
class DIYPagination(PageNumberPagination):
    page_query_param = 'page'  # 默认是page
    # 指定提供给用户设置每页数量的参数名(size)
    # 对标limit参数
    page_size_query_param = 'size'  # 默认是size
    page_size = 5  # 每一页可以显示的条数*默认数据
    max_page_size = 50  # 前端但也最多可以请求到50条记录
