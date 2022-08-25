from flask import Flask, render_template, request
from prediction import predict
import base64
from flask_cors import CORS
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
      data = predict("temp/file")[0]
      m = max(data)
      if data[0] == m:
         return dict(type="bill",max=str(m),output=str(list(data)))
      elif data[1] == m:
         return dict(type="bill_to_pay",max=str(m),output=str(list(data)))
      elif data[2] == m:
         return dict(type="facture",max=str(m),output=str(list(data)))
      elif data[3] == m:
         return dict(type="other",max=str(m),output=str(list(data)))
      else:
         return dict(type="we dont know", max=str(m), output=str(list(data)))

if __name__ == '__main__':
    app.run(host='0.0.0.0')