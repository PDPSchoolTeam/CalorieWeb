from fuzzywuzzy import process

products = ["Lagmon", "Palov", "Manti", "Somsa", "Shashlik"]

search_term = input("Mahsulot nomini kiriting: ").lower()

best_match, score = process.extractOne(search_term, [product.lower() for product in products])

if score >= 80:
    print(f"Topilgan mahsulot: {best_match} (Moslik balli: {score}%)")
else:
    print("Mos keladigan mahsulot topilmadi.")
