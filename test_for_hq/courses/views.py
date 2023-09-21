from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.db.models import Count, Sum

from .models import ProductAccess, ViewingHistory, Lesson, Product, User
from .serializers import LessonSerializer


def home(request):
    return HttpResponse("Welcome to the homepage!")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_lessons(request):
    # Получаем продукты, к которым у пользователя есть доступ
    user_products = ProductAccess.objects.filter(user=request.user).values_list('product', flat=True)

    # Получаем историю просмотров для пользователя
    viewings = ViewingHistory.objects.filter(user=request.user)

    # Получаем уроки из продуктов, к которым у пользователя есть доступ
    lessons = Lesson.objects.filter(products__in=user_products)

    # Сериализуем уроки
    serialized_lessons = LessonSerializer(lessons, many=True).data

    # Добавляем информацию о просмотрах к урокам
    for lesson in serialized_lessons:
        viewing = viewings.filter(lesson_id=lesson["id"]).first()
        if viewing:
            lesson["viewed_time"] = viewing.viewed_time
            lesson["is_watched"] = viewing.is_watched
        else:
            lesson["viewed_time"] = 0
            lesson["is_watched"] = False

    return Response(serialized_lessons)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_lessons(request, product_id):
    # Проверяем, есть ли у пользователя доступ к продукту
    has_access = ProductAccess.objects.filter(user=request.user, product_id=product_id).exists()
    if not has_access:
        return Response({"detail": "Access denied to this product."}, status=403)

    # Получаем уроки из указанного продукта
    lessons = Lesson.objects.filter(products__id=product_id)

    # Получаем историю просмотров для пользователя и выбранного продукта
    viewings = ViewingHistory.objects.filter(user=request.user, lesson__in=lessons)

    # Сериализуем уроки
    serialized_lessons = LessonSerializer(lessons, many=True).data

    # Добавляем информацию о просмотрах к урокам
    for lesson in serialized_lessons:
        viewing = viewings.filter(lesson_id=lesson["id"]).first()
        if viewing:
            lesson["viewed_time"] = viewing.viewed_time
            lesson["is_watched"] = viewing.is_watched
            lesson["last_viewed"] = viewing.updated_at
        else:
            lesson["viewed_time"] = 0
            lesson["is_watched"] = False
            lesson["last_viewed"] = None

    return Response(serialized_lessons)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_statistics(request):
    # Получаем все продукты
    products = Product.objects.all()

    stats = []
    total_users = User.objects.count()

    for product in products:
        # Получаем уроки продукта
        lessons = Lesson.objects.filter(products=product)

        # Получаем историю просмотров для всех уроков этого продукта
        viewings = ViewingHistory.objects.filter(lesson__in=lessons)

        # Получаем количество пользователей, имеющих доступ к этому продукту
        user_count = ProductAccess.objects.filter(product=product).count()

        product_data = {
            'product_name': product.name,
            'viewed_lessons_count': viewings.filter(is_watched=True).count(),
            'total_view_time': viewings.aggregate(Sum('viewed_time'))['viewed_time__sum'] or 0,
            'users_count': user_count,
            'purchase_percentage': (user_count / total_users) * 100 if total_users > 0 else 0
        }

        stats.append(product_data)

    return Response(stats)
