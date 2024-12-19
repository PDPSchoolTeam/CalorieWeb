# import json
import requests
from django.db import connection
from django.shortcuts import render

from .forms import ImageUploadForm
import tempfile
# from app.form import ContactForm
# from app.models import Post


def home(request):
    return render(request, 'index.html')

def Fitnes(request):
    return render(request, 'Fitnes.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')





#
# def contact(request):
#     if request.method == 'GET':
#         context = {'form': ContactForm()}
#         return render(request, 'contact.html', context)
#     elif request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('main')
#         else:
#             return render(request, 'contact.html', {'form': form})








def base(request):
    return render(request, 'base.html')


# def profile(request):
#     posts = Post.objects.all()
#     return render(request, 'profile.html',context={'posts':posts})

# def search_food(request):
#     data = None
#     error = None

#
#


#


# def search_food(request):
#     data = None
#     error = None
#
#     if request.method == "POST":
#         # Foydalanuvchidan mahsulot nomini olish
#         product_name = request.POST.get('product_name', '')
#         language = request.POST.get('lang', 'en')  # Tilni tanlash, standart `en`
#
#         if product_name:
#
#             url = "https://dietagram.p.rapidapi.com/apiFood.php"
#
#             querystring = {"name": "Jabłko", "lang": "pl"}
#
#             headers = {
#                 "x-rapidapi-key": "64b34f3a0amsh9a063160a218e1fp1cca5bjsn30a43e5792c7",
#                 "x-rapidapi-host": "dietagram.p.rapidapi.com"
#             }
#
#
#
#             try:
#                 response = requests.get(url, headers=headers, params=querystring)
#
#                 if response.status_code == 200:
#                     data = response.json()
#                 else:
#                     error = f"API xatosi: {response.status_code} - {response.text}"
#             except requests.exceptions.RequestException as e:
#                 error = f"So'rov xatosi: {str(e)}"
#         else:
#             error = "Mahsulot nomini kiriting."
#
#     return render(request, 'food.html', {"data": data, "error": error})


def search(request):

    query = request.GET.get('query', '')
    results = []

    if query:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT type, name, calories, protein,img_url
                FROM (
                    SELECT 'Ovqat' AS type, name, calories, protein, img_url FROM app_product
                    UNION ALL
                    SELECT 'Ichimlik' AS type, name, calories, protein,img_url FROM drinks
                    UNION ALL
                    SELECT 'Shirinlik' AS type, name, calories, protein,img_url FROM desserts
                ) AS combined
                WHERE name LIKE %s
            """, [f'%{query}%'])
            results = cursor.fetchall()

        if request.method == 'POST':
            form = ImageUploadForm(request.POST, request.FILES)
            if form.is_valid():
                image = request.FILES['image']

                with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
                    for chunk in image.chunks():
                        temp_file.write(chunk)
                    temp_file_path = temp_file.name


                url = "https://taobao-datahub.p.rapidapi.com/item_search_image_2"
                querystring = {"imgUrl": f"{request.build_absolute_uri('/media/')}{image}", "pageSize": "10"}

                headers = {
                    "x-rapidapi-key": "YOUR_RAPIDAPI_KEY",
                    "x-rapidapi-host": "taobao-datahub.p.rapidapi.com"
                }

                response = requests.get(url, headers=headers, params=querystring)

                if response.status_code == 200:
                    result = response.json()
                else:
                    result = {"error": "API dan ma'lumot olishda xatolik yuz berdi."}
        else:
            form = ImageUploadForm()

    return render(request, 'food.html', {'results': results, 'query': query})

