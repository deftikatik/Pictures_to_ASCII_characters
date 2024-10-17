import os
from PIL import Image
import time

# Путь к папке на Android (основной раздел)
android_main_dir = "/storage/emulated/0/"

# Имя файла
img_filename = "123.jpg"

# Полный путь к изображению
img_path = os.path.join(android_main_dir, img_filename)

# Проверяем, существует ли файл
if os.path.exists(img_path):
    # Открываем изображение
    img = Image.open(img_path)

    # Изменение размера изображения
    width, height = img.size
    aspect_ratio = height / width
    new_width = 100  # Вы можете изменить это значение для более детального изображения
    new_height = int(aspect_ratio * new_width * 0.55)
    img = img.resize((new_width, new_height))

    # Перевод изображения в черно-белое
    img = img.convert('L')

    # Символы для замены яркости
    ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

    # Функция для преобразования пикселя в символ
    def pixel_to_ascii(pixel_value):
        return ASCII_CHARS[pixel_value // 34]

    # Преобразование изображения в ASCII
    ascii_image = []
    for y in range(new_height):
        row = ""
        for x in range(new_width):
            pixel_value = img.getpixel((x, y))
            row += pixel_to_ascii(pixel_value)
        ascii_image.append(row)

    # Функция для поочередного вывода символов с задержкой
    def print_picture(picture, delay=0.1):
        for row in picture:
            for char in row:
                print(char, end='', flush=True)
                time.sleep(delay / len(row))
            print()

    # Вызов функции для поочередного вывода ASCII изображения
    print_picture(ascii_image)

else:
    print(f"Файл {img_filename} не найден в директории {android_main_dir}")
