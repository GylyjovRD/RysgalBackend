from django.contrib import admin

from .models import Order, OrderItems

class OrderItemsInline(admin.StackedInline):
    model = OrderItems
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "status", "total_price", "is_active", "region"]
    list_editable = ["status", "is_active"]
    list_per_page = 20
    inlines = [OrderItemsInline]

admin.site.register(Order, OrderAdmin)
# admin.site.register(OrderItems)