from rest_framework.pagination import PageNumberPagination


class ClickPaginator(PageNumberPagination):
    page_size = 25
    max_page_size = 50
