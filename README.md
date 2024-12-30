# Flask-PDF-to-JPG


This project provides a simple web application built using Flask that allows users to upload a `.pdf` file and convert each page of the PDF into a `.jpg` image. The images are then stored in the `output_images` directory and can be accessed via a browser.

## Features

- Upload a `.pdf` file to the server.
- Convert each page of the PDF into a `.jpg` image.
- Each image is saved in the `output_images` directory with the naming convention `<pdf_name>_pageX.jpg`.
- The converted images are accessible via the browser.

## Project Structure

```
/PDF-to-JPG-Converter
│
├── /templates
│   ├── index.html               # HTML template for the upload form
├── app.py                       # Flask app script
├── /output_images               # Folder for storing the converted images
├── requirements.txt             # Required Python packages
└── README.md                    # This README file
```

## Installation

### Prerequisites
Ensure you have Python 3.x installed on your machine.

1. **Clone the repository**:
  

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   You can install the required dependencies using the `requirements.txt` file.

   ```bash
   pip install -r requirements.txt
   ```

4. **Install Poppler**:
   The `pdf2image` library requires **Poppler** to be installed. You can download it from the [Poppler website](https://poppler.freedesktop.org/).

   After installing Poppler, ensure that its binary is in your system's PATH, or provide the path explicitly in the script (e.g., `poppler_path=r'C:\Program Files (x86)\poppler-23.08.0\Library\bin'` for Windows).

### Run the App

1. **Start the Flask application**:
   ```bash
   python app.py
   ```

   The application will run locally at `http://127.0.0.1:5000/`.

2. **Upload your PDF file**:
   - Open the application in your browser (`http://127.0.0.1:5000/`).
   - Use the form to upload a `.pdf` file that you want to convert into JPG images.
   - The app will convert each page of the PDF to a `.jpg` file and store it in the `output_images` directory.

### Usage

- Go to `http://127.0.0.1:5000/` in your browser.
- Select a `.pdf` file to upload.
- The PDF will be converted to individual `.jpg` images, with each image representing a page of the PDF.
- The images will be saved in the `output_images` directory and can be accessed via the URL `http://127.0.0.1:5000/output/<filename>`.

### API Endpoints

#### **POST `/upload`**

- **Parameters**: 
  - `pdf_file`: The PDF file to be uploaded.

- **Response**: 
  - A success message: `"SUCCESSFULLYYYYY"`
  - Or an error message if the file is missing or invalid.

- **Example Request**:
  ```bash
  curl -X POST -F "pdf_file=@path_to_pdf_file.pdf" http://127.0.0.1:5000/upload
  ```

- **Example Response**:
  ```json
  {
    "message": "SUCCESSFULLYYYYY"
  }
  ```

#### **GET `/output/<filename>`**

- **Parameters**: 
  - `filename`: The name of the converted image file to access.

- **Response**: 
  - The `.jpg` image file corresponding to the provided filename.

- **Example Request**:
  ```bash
  curl http://127.0.0.1:5000/output/<filename>
  ```

- **Example Response**: The response will be the actual image file.

### Error Handling

The application checks for the following errors:

- **No file part**: If no file is provided in the request.
- **No selected file**: If the file selected is empty or not selected properly.
- **Invalid file format**: If the uploaded file is not a `.pdf` file.
  
These errors will be returned with a relevant error message in JSON format.

### Requirements

- Python 3.x or higher
- Flask
- pdf2image (for converting PDF to images)
- Pillow (for image processing)
- Poppler (required by pdf2image)

You can install the required Python libraries via the `requirements.txt` file:

```bash
pip install -r requirements.txt
```
