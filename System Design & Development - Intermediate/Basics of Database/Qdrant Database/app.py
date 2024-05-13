from flask import Flask, flash, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
from pathlib import Path
from PIL import Image
from image_embedding import ImageEmbedding
from database import *

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads/"
current_file_path = Path.cwd()
app.secret_key = "secret key"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
ALLOWED_EXTENSIONS = set(["png", "jpg", "jpeg"])
image_embedding = ImageEmbedding()
database = Database()
database.collection()
database.select_collection()

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def home():
    """home page start

    Returns:
        template: index.html template
    """
    return render_template("index.html")

@app.route("/", methods=["POST"])
def upload_image():
    """upload image in server

    Returns:
        template: index.html template
    """
    if "file" not in request.files:
        flash("No file part")
        return redirect(request.url)
    file = request.files["file"]
    if file.filename == "":
        flash("No image selected for uploading")
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        image = Image.open(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        image_vector = image_embedding.run(image)
        database.upsert(image_vector,filename)
        flash("Image successfully uploaded and displayed below")
        return render_template("index.html", filename=filename)
    else:
        flash("Allowed image types are - png, jpg, jpeg.")
        return redirect(request.url)

@app.route("/display/<filename>")
def display_image(filename):
    """display enter image to website
    """
    return redirect(url_for("static", filename="uploads/" + filename), code=301)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
