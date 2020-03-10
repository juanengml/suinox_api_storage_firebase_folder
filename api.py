import os
import urllib.request
from werkzeug.datastructures import ImmutableMultiDict
from flask import Flask, request
from werkzeug.utils import secure_filename

from flask import Flask

UPLOAD_FOLDER = 'folder'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


@app.route('/file-upload', methods=['POST'])
def upload_file():
  try:
    data = request.files.to_dict(flat=True)[''] # checa
    data.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(data.filename)))
    return {"mesage":"rodou"}
  except:
    return {"mesage":"deu ruim"}  
if __name__ == "__main__":
    app.run(debug=True)
