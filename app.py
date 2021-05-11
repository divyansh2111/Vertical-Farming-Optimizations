from flask import Flask, render_template, url_for, request, redirect
import tensorflow as tf
import pickle, sklearn
import numpy as np
import os, cv2
from efficientnet.tfkeras import EfficientNetB7

app = Flask(__name__)

nut_mod = pickle.load(open('models/Nutrient_model.sav', 'rb'))
# model1 = tf.keras.models.load_model("models/EfficientNet.h5")
json_file = open('models/EfficientNet.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model1 = tf.keras.models.model_from_json(loaded_model_json)
# load weights into new model
model1.load_weights("models/EfficientNet_weights.h5")
cnt = 0

def get_recomm(model, crop, env_temp, env_humidity, env_ph, env_rainfall):
    crops = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
            'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
            'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
            'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']

    crop_encoding = [0]*len(crops)
    for indx in range(len(crops)):
      if crops[indx]==crop:
        crop_encoding[indx] = 1
        break

    features = np.array([env_temp,env_humidity,env_ph,env_rainfall] + crop_encoding).reshape(1,-1)
    nutrients = model.predict(features)[0]
    # print("Optimal concentrations of\nN =",nutrients[0], "\nP =",nutrients[1], "\nK =",nutrients[2])
    return nutrients

def process(img):
    return cv2.resize(img/255.0, (512, 512)).reshape(-1, 512, 512, 3)

def predict(model, img):
    preds = model.layers[2](model.layers[1](model.layers[0](process(img)))).numpy()[0]
    # print(preds)
    if list.index(preds.tolist(), max(preds)) == 0:
        pred = "Healthy"
    if list.index(preds.tolist(), max(preds)) == 1:
        pred = "Diseased [Scabs]"
    if list.index(preds.tolist(), max(preds)) == 2:
        pred = "Diseased [Rust]"
    if list.index(preds.tolist(), max(preds)) == 3:
        pred = "Diseased [Multiple]"
    return pred



@app.route("/")
def initial_file():
  return render_template('index.html')

@app.route("/nutrients", methods=['GET', 'POST'])
def nutrients_run():
  if request.method == 'POST':
    val = request.form
    print()
    nutrients = [0,0,0]
    nutrients = get_recomm(nut_mod, str(val['plant']), val['temp'], val['humid'], val['pH'], val['water'])
    # print(nutrients)
    return render_template('nutrients.html', potassium=round(nutrients[2],2), phosphorus=round(nutrients[1],2), nitrogen=round(nutrients[0],2))
  return render_template('nutrients.html')

@app.route("/disease", methods=['GET', 'POST'])
def disease_pred():
  global cnt
  if request.method == 'POST':
    img_file = request.files["image"]
    # print("FFFF ----- ", img_file.filename)
    if img_file:
      img_name = str(img_file.filename).split('.')[0] + str(cnt) + str(img_file.filename).split('.')[1]
      img = os.path.join(os.getcwd(), 'static', 'images', img_name)
      cnt+=1
      img_file.save(img)
      image = cv2.imread(img)
      # image = process(image)
      # print(image.shape)
      pred = "FF"
      pred = predict(model1, image)
      # print(img_file.filename)
      return render_template('disease.html', img = img_name, prediction=pred)
  return render_template('disease.html')

@app.route("/presentation")
def presentation():
  return redirect('https://drive.google.com/file/d/1-OSwgN72lzQEiV3zimvwKy6MFOwyt0jy/view?usp=sharing')

if __name__ == '__main__':
  # port = int(os.environ.get("PORT", 5000))
  app.run(debug = True, host='0.0.0.0', port=8080)