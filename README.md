# 🖼️ OpenCV Image Processing Collection

This repository contains a collection of Python scripts demonstrating various **image processing**, **computer vision**, and **OpenCV** functionalities. Each module is organized by functionality for easy learning and experimentation.

---
## 📁 Folder Structure

### 🔹 read
Start by learning how to read and display images and videos.
- `read_img.py` — Read and display an image  
- `read_video.py` — Capture and display video streams  

---

### 🔹 rescaling and resizing
Learn how to modify image and video dimensions.
- `change_resolution.py` — Change video capture resolution  
- `rescale_img.py` — Rescale image dimensions  
- `rescale_video.py` — Rescale video frames dynamically  

---

### 🔹 essential functions
Understand basic image processing operations.
- `blur.py` — Apply basic blurring  
- `crop_resize.py` — Crop and resize images  
- `dialte.py` — Perform dilation on binary images  

---

### 🔹 blurring
Dive deeper into noise reduction and smoothing filters.
- `Averaging.py` — Mean filter  
- `bilateral.py` — Bilateral filtering (preserves edges)  
- `blur.py` — Basic blurring using convolution  
- `gausian.py` — Gaussian blur for smooth filtering  
- `median.py` — Median blur for salt-and-pepper noise reduction  

---

### 🔹 colour_spaces
Explore color transformations and channel manipulations.
- `colour_spaces.py` — Convert between BGR, HSV, LAB, and other color spaces  
- `split_merge.py` — Split and merge color channels  

---

### 🔹 transformations
Learn to modify image geometry and orientation.
- `flip.py` — Flip images horizontally or vertically  
- `rotation.py` — Rotate images by given angles  
- `translation.py` — Shift (translate) images spatially  

---

### 🔹 masking
Isolate and highlight specific regions of an image.
- `mask.py` — Create and apply masks to highlight image regions  

---

### 🔹 bitwise
Perform logical operations between images.
- `bitwise.py` — AND, OR, NOT, and XOR operations  

---

### 🔹 histogram
Analyze image intensity and color distributions.
- `coloured_histogram.py` — Plot color histograms  
- `grayscale_histogram.py` — Plot grayscale histograms  

---

### 🔹 draw
Draw custom shapes and annotations on images.
- `draw.py` — Draw lines, rectangles, circles, and text using OpenCV  

---

### 🔹 additional scripts
Explore advanced effects and operations.
- `edge_cascade.py` — Edge detection using Canny  
- `eroded.py` — Erosion operation  
- `gradients.py` — Sobel and Laplacian gradients  
- `greyscale.py` — Convert images to grayscale  

---

### 🔹 photos
Sample images for testing and experimentation.
- `cat.jpg`  
- `cats 2.jpg`  
- `cats.jpg`  
- `park.jpg`

---

## ⚙️ Requirements

Install the required dependencies using:
```bash
pip install opencv-python numpy matplotlib
```

---


## 🎯 Purpose

This project serves as a **comprehensive OpenCV practice set** to understand:

-  **Image Processing Fundamentals** — Learn how to read, manipulate, and enhance images using OpenCV.
-  **Filters and Transformations** — Apply various filters like blurring, Gaussian, median, and perform geometric transformations like rotation, flipping, and translation.
-  **Histograms, Masking, and Bitwise Operations** — Explore pixel intensity distributions, masking techniques, and logical operations on images.
-  **Real-Time Video Processing** — Work with live video feeds, frame manipulation, and resolution scaling.
