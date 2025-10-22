# app.py
from flask import Flask, render_template, request, send_from_directory
from crowd_analysis import analyze_crowd
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return "No file uploaded."
    
    file = request.files['image']
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    density, alert = analyze_crowd(filepath)
    return render_template("result.html", density=density, alert=alert, filename=file.filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)


    






# from flask import Flask, render_template, request, send_from_directory
# from crowd_analysis import analyze_crowd
# import os

# app = Flask(__name__)
# UPLOAD_FOLDER = "uploads"
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/analyze', methods=['POST'])
# def analyze():
#     if 'image' not in request.files:
#         return "No file uploaded."
    
#     file = request.files['image']
#     filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#     file.save(filepath)

#     count, alert = analyze_crowd(filepath)
#     return render_template("result.html", count=count, alert=alert, filename=file.filename)

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# if __name__ == "__main__":
#     app.run(debug=True)
