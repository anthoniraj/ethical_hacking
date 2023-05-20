from flask import Flask, request, render_template

app = Flask(__name__)
app.config['UPLOAD_PATH'] = "uploaded_files"

@app.route("/", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['myfile']
        print(uploaded_file.filetype)
        uploaded_file.save(app.config['UPLOAD_PATH']+"/"+uploaded_file.filename)
        return render_template("upload.html")

    else:
        return render_template("upload.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)