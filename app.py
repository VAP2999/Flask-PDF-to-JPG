from flask import Flask, request, jsonify, render_template
import os
from pdf2image import convert_from_path

app = Flask(__name__)

# Directory to store the images
output_directory = 'output_images'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'pdf_file' not in request.files:
        return jsonify({'error': 'No file part'})

    pdf_file = request.files['pdf_file']

    if pdf_file.filename == '':
        return jsonify({'error': 'No selected file'})

    if pdf_file and pdf_file.filename.endswith('.pdf'):
        pdf_name = os.path.splitext(pdf_file.filename)[0]
        pdf_path = os.path.join(output_directory, pdf_file.filename)
        pdf_file.save(pdf_path)

        images = convert_from_path(pdf_path, poppler_path=r'C:\Program Files (x86)\poppler-23.08.0\Library\bin')

        for i, image in enumerate(images):
            output_file_path = os.path.join(output_directory, f'{pdf_name}_page{i}.jpg')
            image.save(output_file_path, 'JPEG')

        return "SUCCESSFULLYYYYY"

    return jsonify({'error': 'Invalid file format'})



@app.route('/output/<filename>')
def uploaded_file(filename):
    return send_from_directory(output_directory, filename)





if __name__ == '__main__':
    app.run(debug=True)


