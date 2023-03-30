import io
import base64
import random
from PIL import Image, ImageDraw, ImageFont

def generateValidateCodeImage(code):
    font_path = 'arialbd.ttf'
    font_size = 30
    noise_level = 0.15

    # 生成隨機字符串
    text = code

    # 設置字體
    font = ImageFont.truetype(font_path, font_size)

    # 計算圖片尺寸
    text_width, text_height = font.getsize(text)
    img_width = text_width + 20
    img_height = text_height + 5

    # 生成空白圖片
    img = Image.new('RGB', (img_width, img_height), color=(255, 255, 255))

    # 添加噪聲線
    draw = ImageDraw.Draw(img)
    for i in range(15):
        x1, y1 = random.randint(0, img_width), random.randint(0, img_height)
        x2, y2 = random.randint(0, img_width), random.randint(0, img_height)
        draw.line((x1, y1, x2, y2), fill=(200, 200, 200), width=1)

    # 繪製文字
    x = (img_width - text_width) / 2
    y = (img_height - text_height) / 2

    gradient = [(255, 0, 0), (0, 0, 255)]  # 紅色到藍色的漸層
    gradient.sort()  # 將漸層顏色從小到大排序
    for i, char in enumerate(text):
        font_size_variation = random.randint(-3, 3)
        if font_size_variation != 0:
            # 如果字體大小有變化，就重新生成字體
            font = ImageFont.truetype(font_path, font_size + font_size_variation)
        fill = tuple(random.randint(min(gradient[j][k], gradient[j+1][k]), max(gradient[j][k], gradient[j+1][k])) for j in range(len(gradient)-1) for k in range(3))
        draw.text((x + i * text_width / len(text), y), char, font=font, fill=fill)

    # 添加噪聲
    pixels = img.load()
    for i in range(img_width):
        for j in range(img_height):
            if random.random() < noise_level:
                pixels[i, j] = tuple(random.randint(128, 255) for _ in range(3))

    # 将图像对象转换为 base64 编码的字符串
    with io.BytesIO() as buffer:
        img.save(buffer, format='PNG')
        img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

    # 返回base64编码的字符串和图像对象
    return img_base64