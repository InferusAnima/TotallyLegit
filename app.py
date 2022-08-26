from flask import Flask, render_template, request
# from prediction import predict
import base64
from flask_cors import CORS
import workWithImage
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
CORS(app)
@app.route('/')
def index():
   return render_template('upload.html')

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
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

      return workWithImage.get_type("temp/file")


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2898)