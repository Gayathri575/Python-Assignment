import csv
import random

electronics = [
    "Apple iPhone 14",
    "Apple iPhone 14 Pro",
    "Apple iPhone 15",
    "Samsung Galaxy S21",
    "Samzung Galaxy S21",   # typo
    "Samsung Galaxy S22",
    "OnePlus Nord",
    "OnePlus Nrod",         # typo
    "Dell Inspiron Laptop",
    "HP Pavilion Laptop",
    "Sony Headphones",
    "Boat Headphones"
]

fashion = [
    "Nike Running Shoes",
    "Nike Runing Shoes",   # typo
    "Adidas Sports T-Shirt",
    "Puma Casual Shoes",
    "Levi's Blue Jeans",
    "Lee Blue Jeans",
    "Allen Solly Shirt",
    "H&M Cotton Shirt",
    "Zara Women's Top",
    "Roadster Men's Jacket"
]

groceries = [
    "Aashirvaad Wheat Flour",
    "Aashirwad Wheat Flour",  # typo
    "Tata Salt",
    "Tata Lite Salt",
    "Fortune Sunflower Oil",
    "Fortune Refined Oil",
    "Maggi 2-Minute Noodles",
    "Maggie Noodles",        # typo
    "Amul Butter",
    "Amul Fresh Milk"
]

all_products = electronics + fashion + groceries

with open("products.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["product_id", "product_name"])

    for product_id in range(1, 501):
        product_name = random.choice(all_products)
        writer.writerow([product_id, product_name])

print(" file created with 500 products")
