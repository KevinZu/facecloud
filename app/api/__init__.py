import os
from flask import Flask, request, redirect, url_for, Response, render_template
from werkzeug import secure_filename
import json

UPLOAD_FOLDER = '/root/src/test/img'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

base_route = '/v1'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS




# api: PersonnelDataEntry
@app.route(base_route + '/PersonnelDataEntry', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        print(request.args)
        print(request.files)
        file = request.files['file']
        print(file.filename)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            t = {
                'IsSuccess' : True,
                'Count' : 2
            }

            return Response(json.dumps(t),mimetype='application/json')
            # return '''redirect(url_for('uploaded_file',
                                    # filename=filename))
                                    # '''
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


if __name__ == '__main__':
    app.run()