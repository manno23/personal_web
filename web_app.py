from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") 
def root():
    return render_template('root.html')

@app.route('/blog')
@app.route('/blog/<name>')
def blog(name=None):
    return render_template('blog.html', name=name)

if __name__ == "__main__":
    app.run()
