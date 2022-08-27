from flask import Flask, render_template, request
# from prediction import predict
import base64
import sys
from flask_cors import CORS
import workWithImage
import prediction
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
CORS(app)
@app.route('/')
def index():
   return render_template('upload.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
   # print("Vanya lox")
   # print(request)
   if request.method == 'POST':
      try:
         f = request.files['file']
         f.save("temp/file")
      except:

         fi = request.get_json()["file"].split(",")[-1]
         fi = base64.b64decode(fi)
         f = open("temp/file","wb")
         f.write(fi)
         f.close()
      response = prediction.predict("gen_1","temp/file")
      m = max(response)
      print(response)
      if m == response[0]:
         return "счет"
      elif m == response[1]:
         return "счет-фактура"
      elif m == response[2]:
         return "другое"
      # return response


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2898)