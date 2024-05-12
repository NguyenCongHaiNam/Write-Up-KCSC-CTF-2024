from PIL import Image

# Load hình ảnh
image = Image.open("Shadow.png")
pixel_access = image.load()

# Mở file để ghi kết quả
with open("pixel_values.txt", "w") as file:
    for y in range(image.height):
        for x in range(image.width):
            # Lấy giá trị RGB của pixel tại vị trí (x, y)
            rgb = pixel_access[x, y]
            # Chuyển đổi giá trị RGB sang dạng hex
            hex_value = "{:02x} {:02x} {:02x}".format(rgb[0], rgb[1], rgb[2])
            # Ghi giá trị hex vào file
            file.write(f"{hex_value} ")
