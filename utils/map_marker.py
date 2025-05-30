import tkinter as tk
from PIL import Image, ImageTk

def get_scaled_coordinates(event):
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()
    image_width = canvas.image_width
    image_height = canvas.image_height

    x_offset = (canvas_width - image_width) // 2
    y_offset = (canvas_height - image_height) // 2

    if x_offset <= event.x <= x_offset + image_width and y_offset <= event.y <= y_offset + image_height:
        relative_x = event.x - x_offset
        relative_y = event.y - y_offset

        scaled_x = int((relative_x / image_width) * 330)
        scaled_y = int((relative_y / image_height) * 165)
        print(f"Original Coordinates: ({relative_x}, {relative_y})")
        print(f"Scaled Coordinates: ({scaled_x}, {scaled_y})")
    else:
        print("Clicked outside the image")

def resize_image(event=None):
    # Ensure the window dimensions are valid
    window_width = root.winfo_width()
    window_height = root.winfo_height()

    if window_width <= 1 or window_height <= 1:
        return  # Skip resizing until valid dimensions are available

    aspect_ratio = original_image.width / original_image.height
    if window_width / window_height > aspect_ratio:
        new_width = int(window_height * aspect_ratio)
        new_height = window_height
    else:
        new_width = window_width
        new_height = int(window_width / aspect_ratio)

    tk_image = ImageTk.PhotoImage(original_image.resize((new_width, new_height), Image.Resampling.NEAREST))

    canvas.delete("all")
    canvas.image_width, canvas.image_height = new_width, new_height

    x_offset = (window_width - new_width) // 2
    y_offset = (window_height - new_height) // 2

    canvas.create_image(x_offset, y_offset, anchor=tk.NW, image=tk_image)
    canvas.image = tk_image

def load_image(image_path):
    global canvas, original_image

    original_image = Image.open(image_path)
    canvas = tk.Canvas(root)
    canvas.pack(fill=tk.BOTH, expand=True)

    resize_image()
    root.bind("<Configure>", resize_image)
    canvas.bind("<Button-1>", get_scaled_coordinates)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Scalable Image Coordinate Mapper")

    image_path = "textures/ui/assets/earth_smp_map.png"
    load_image(image_path)

    root.mainloop()
