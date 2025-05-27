from api.models import Category, Product

def create_categories():
    categories = [
        "Processors",
        "Graphics Cards",
        "Motherboards",
        "RAM (Memory)",
        "Hard Drives (HDD)",
        "Solid State Drives (SSD)",
        "Computer Cases",
        "Power Supplies",
        "Cooling Systems",
        "Monitors",
        "Keyboards",
        "Mice",
        "Sound Cards",
        "Network Cards",
        "Optical Drives",
        "Cables and Adapters",
        "Webcams",
        "Gaming Accessories"
    ]

    for cat_name in categories:
        Category.objects.get_or_create(name=cat_name)

    print("Категории созданы (или уже существуют).")


def seed_database():
    categories = {
        "Processors": [
            {"name": "Intel Core i7", "stock": 15, "price": 299.99, "description": "8-core 11th Gen processor"},
            {"name": "AMD Ryzen 5", "stock": 20, "price": 229.99, "description": "6-core CPU, great for gaming"},
        ],
        "Graphics Cards": [
            {"name": "NVIDIA RTX 3070", "stock": 10, "price": 599.99, "description": "Powerful GPU for 1440p gaming"},
        ],
        "RAM (Memory)": [
            {"name": "Corsair Vengeance 16GB", "stock": 50, "price": 89.99, "description": "DDR4 3200MHz dual channel kit"},
        ],
        "Solid State Drives (SSD)": [
            {"name": "Samsung 970 EVO 1TB", "stock": 30, "price": 149.99, "description": "NVMe M.2 SSD"},
        ],
        "Power Supplies": [
            {"name": "EVGA 600W Bronze", "stock": 25, "price": 59.99, "description": "Reliable PSU with 80+ efficiency"},
        ]
    }

    for cat_name, products in categories.items():
        category, _ = Category.objects.get_or_create(name=cat_name)
        for p in products:
            Product.objects.get_or_create(
                name=p["name"],
                defaults={
                    "stock": p["stock"],
                    "price": p["price"],
                    "description": p["description"],
                    "category": category
                }
            )

    print("✅ База данных успешно заполнена тестовыми категориями и продуктами.")