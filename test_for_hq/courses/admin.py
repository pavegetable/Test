from django.contrib import admin
from .models import Product, ProductAccess, Lesson, LessonProductMapping, ViewingHistory

admin.site.register(Product)
admin.site.register(ProductAccess)
admin.site.register(Lesson)
admin.site.register(LessonProductMapping)
admin.site.register(ViewingHistory)
