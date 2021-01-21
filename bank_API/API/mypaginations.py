from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 4
    max_limit = 4
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000
    