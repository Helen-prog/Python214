from django.contrib import admin
from .models import Order, StatusCrm


class OrderAdm(admin.ModelAdmin):
    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    list_filter = ('order_status', 'order_dt')
    list_editable = ('order_status', 'order_phone')
    fields = ('id', 'order_status', 'order_dt', 'order_name', 'order_phone')
    readonly_fields = ('id', 'order_dt')


admin.site.register(Order, OrderAdm)
admin.site.register(StatusCrm)
