from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Customer, Restaurant

# Registro de usuarios
def register(request):
    if request.method == 'POST':
        data = request.POST
        user = User.objects.create_user(
            username=data['username'],
            password=data['password']
        )
        if data['type'] == 'restaurant':
            Restaurant.objects.create(user=user, name=data['name'])
        elif data['type'] == 'customer':
            restaurant = Restaurant.objects.get(id=data['restaurant_id'])
            Customer.objects.create(user=user, restaurant=restaurant)
        return JsonResponse({'message': 'User registered successfully!'})
