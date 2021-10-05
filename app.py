from flask import Flask, render_template, request, redirect, flash
from tensorflow.keras.models import load_model
import os

# import tensorflow as tf
# from tensorflow import keras
# from keras.preprocessing.image import img_to_array
# from keras.applications.vgg16 import preprocess_input
# from keras.applications.vgg16 import decode_predictions
# from keras.applications.vgg16 import VGG16

# model = load_model()
app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#model = VGG16()
@app.route("/")
def home():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def predict():
    if 'imagefile' not in request.files:
        #flash('No file part')
        return redirect(request.url)
    uploadedFile = request.files['imagefile']
    if uploadedFile and allowed_file(uploadedFile.filename):
        uploadedFile.save(os.path.join(app.config['UPLOAD_FOLDER'], uploadedFile.filename))
    #img_path = './uploads/' + uploadedFile.filename
    #uploadedFile.save(img_path)

    #print(img_path)

    # image = load_image(img_path, target_size=(224,224))
    # image = img_to_array(image)
    # image = image.reshape(1, image.shape[0], image.shape[1], image.shape[2])
    # image = preprocess_input(image)

    # preds = model.predict(image)
    # label = decode_predictions(preds)
    # label = label[0][0]

    # classification = '%s (%.2f%%)' % (label[1], label[2] * 100)

    return render_template('index.html', prediction = 'classification', output_img_path = uploadedFile)

# Real Time Route

@app.route("/app")
def appp():
    return render_template('video.html')

    
@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == '__main__':
    app.run(debug=True, port=7000)
</filename>
#src="{{output_img_path | default('../static/images/default_img.png')}}"
#<!-- src="../static/images/pred7.PNG" -->