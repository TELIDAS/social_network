from django_filters import rest_framework as filters
from . import models


class LikeFilter(filters.FilterSet):
    date_from = filters.DateTimeFilter(field_name="liked_time",
                                       lookup_expr="gte")
    date_to = filters.DateTimeFilter(field_name="liked_time",
                                     lookup_expr="lte")

    class Meta:
        model = models.Like
        fields = ("date_from", "date_to")
