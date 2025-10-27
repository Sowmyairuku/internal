from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pwd')
        if not username:
            return '''<script>alert("Username cannot be empty.");window.location='/'</script>'''
        if not password:
            return '''<script>alert("Password cannot be empty.");window.location='/'</script>'''
        if len(password) < 6:
            return '''<script>alert("Password must be at least 6 characters long.");window.location='/'</script>'''
        return redirect(url_for('submit', username=username))
    return render_template('form.html')
@app.route('/submit')
def submit():
    username = request.args.get('username', '')
    return render_template('result.html', username=username)

if __name__ == "__main__":
    app.run(debug=True)
