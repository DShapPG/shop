from api.models import Category

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


