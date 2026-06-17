import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageOps

class ImageBorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Image Border Editor")
        self.root.geometry("400x280")
        self.image_path = None

        # 1. Load Image Button
        self.btn_load = tk.Button(root, text="1. Load Image", command=self.load_image, width=20, bg="#e1e1e1")
        self.btn_load.pack(pady=15)

        # 2. Border Size Selection Dropdown
        self.lbl_size = tk.Label(root, text="2. Select Border Size:")
        self.lbl_size.pack(pady=2)
        
        # We use a ttk Combobox for the dropdown menu
        self.size_dropdown = ttk.Combobox(root, values=["Small", "Medium", "Large"], state="readonly", width=18)
        self.size_dropdown.set("Medium")  # Set 'Medium' as the default choice
        self.size_dropdown.pack(pady=5)

        # 3. Action Buttons (Initially disabled until image is loaded)
        self.btn_white = tk.Button(root, text="Add White Border", command=lambda: self.add_border("white"), state=tk.DISABLED, width=20)
        self.btn_white.pack(pady=5)

        self.btn_black = tk.Button(root, text="Add Black Border", command=lambda: self.add_border("black"), state=tk.DISABLED, width=20)
        self.btn_black.pack(pady=5)

    def load_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp")])
        if self.image_path:
            messagebox.showinfo("Success", "Image loaded successfully!")
            self.btn_white.config(state=tk.NORMAL)
            self.btn_black.config(state=tk.NORMAL)

    def add_border(self, color):
        if not self.image_path:
            return
        
        # Map the dropdown text selection to actual pixel values
        size_mapping = {
            "Small": 100,
            "Medium": 300,
            "Large": 600
        }
        
        # Get the selected thickness from the dropdown
        selected_size_name = self.size_dropdown.get()
        border_width = size_mapping[selected_size_name]
        
        try:
            # Open image and apply the dynamically selected border width
            img = Image.open(self.image_path)
            bordered_img = ImageOps.expand(img, border=border_width, fill=color)
            
            # Save the new image
            save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")])
            if save_path:
                bordered_img.save(save_path)
                messagebox.showinfo("Saved", f"Saved with a {selected_size_name} ({border_width}px) {color} border!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not process image: {e}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageBorderApp(root)
    root.mainloop()