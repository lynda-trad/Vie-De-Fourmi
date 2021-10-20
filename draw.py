from PIL import Image, ImageDraw


def rectangle(output_path, lab, endingPath, printPath):
    imageSize = len(lab) * 2
    rectSize = int(len(lab) / 2)

    image = Image.new("RGB", (imageSize, imageSize), "#F5F5DC")
    draw = ImageDraw.Draw(image)
    # a room is a white filled rectangle with black contour
    # Sd room is a white filled rectangle with green contour
    # Sv room is a white filled rectangle with red contour
    # draw.rectangle([(j * rectSize, i * rectSize), (j + 1 * rectSize, i + 1 * rectSize)], fill="black")

    # an ant is a black dot
    # draw.ellipse((x - r, y - r, x + r, y + r), fill="black")

    # link between rooms are black lines
    # draw.line(shape, fill="black", width = 2)
    image.save(output_path)
    image.show()

