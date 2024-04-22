import os
import google.generativeai as genai
import PIL
from googlesearch import search


def find_recycling_centers(query):
    results = search(query)
    return results


def gemini_api(image_path):
    os.environ['GOOGLE_API_KEY'] = 'AIzaSyCRnbt2sS3okoyl4IcAGeRcsyK3w0m8Sk8'
    # genai.configure(api_key="AIzaSyCRnbt2sS3okoyl4IcAGeRcsyK3w0m8Sk8")

    # Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
    # GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')

    genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

    img = PIL.Image.open(image_path)

    model = genai.GenerativeModel('gemini-pro-vision')

    response = model.generate_content([
        "simply provide only the names of product from this trash that can be recycled and normal person can get some money and "
        "if there are not any then just return 'no such products' ",
        img], stream=True)
    response.resolve()
    return response.text
