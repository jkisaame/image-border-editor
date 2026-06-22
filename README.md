# Image Border Editor

A lightweight, cross-platform graphical user interface (GUI) utility written in Python that allows users to easily add clean white or black borders to their images. 

This repository supports development across Windows x86 and Windows ARM64 architectures, with binaries compiled via PyInstaller.

## Features
* **Simple GUI:** Intuitive layout built entirely with native Python interface components.
* **Dynamic Sizing:** Choose between Small, Medium, and Large presets.
* **Customizable Architecture:** Clean code structure allowing easy modification of underlying pixel widths.
* **Open Source:** Released under the GPL 3.0 License.

---

## Technical Specifications & Dependencies

### Prerequisites
To run the source code directly, you need **Python 3.x** installed on your system. 

### Standard Libraries Used
These packages come pre-installed with Python and require no extra installation:
* `tkinter` / `ttk` — Handles the window layout, dropdown selectors, and button actions.
* `filedialog` / `messagebox` — Powers the native OS file selectors and popup notifications.

### Third-Party Dependencies
The application relies on the **Pillow (PIL)** library for robust image manipulation. Install it via pip:

```bash
pip install Pillow
