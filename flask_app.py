from flask import Flask, render_template, request, redirect
from main import gemini_api
from main import find_recycling_centers

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', response_text=None)


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    # Save the uploaded file as "image.jpg"
    file.save('image.jpg')
    results = {}
    response_text = gemini_api(image_path='image.jpg')
    if response_text != 'no such products':
        query = "names of the recycling centers near me and their address"
        result_ = find_recycling_centers(query)

        for idx, result in enumerate(result_, start=1):
            results[idx] = result

    return render_template('index.html', response_text=response_text, results=results)


if __name__ == '__main__':
    app.run(debug=True)
