# import json
import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


# def search_food(request):
#     data = None
#     error = None

#

def recipe_detail_view(request):
    if request.method == "GET":
        recipe_id = request.GET.get("id", "")

        # ID yuborilmagan bo'lsa, xato qaytaring
        if not recipe_id:
            return JsonResponse({"error": "Recipe ID is required"}, status=400)

        try:
            # API ma'lumotlari
            url = "https://recipes-api3.p.rapidapi.com/rapidapi/recipes/"
            querystring = {"type": "get-recipe", "id": recipe_id}
            headers = {
                "x-rapidapi-key": "64b34f3a0amsh9a063160a218e1fp1cca5bjsn30a43e5792c7",
                "x-rapidapi-host": "recipes-api3.p.rapidapi.com"
            }

            # API so'rovi
            response = requests.get(url, headers=headers, params=querystring)

            if response.status_code == 200:
                recipe_data = response.json()

                # Ma'lumotlarni HTML sahifasiga uzatish
                return render(request, "recipe_detail.html", {"recipe": recipe_data})
            else:
                return JsonResponse(
                    {"error": "Failed to fetch recipe data", "status_code": response.status_code},
                    status=response.status_code
                )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=405)

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