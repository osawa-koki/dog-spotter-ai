import os, glob

from PIL import Image

def generate_image(prompt: str) -> Image:
    return Image.new("RGB", (1024, 1024), (255, 255, 255))

if __name__ == "__main__":
    prompt = "A beautiful landscape with a river and mountains"
    image = generate_image(prompt)
    image.save("generated_image.png")
