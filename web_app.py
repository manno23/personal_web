from flask import Flask, render_template
app = Flask(__name__)


blog_entries = ['ssd', 'hydra', 'firewall', 'firmware']



@app.route("/") 
def root():
    return render_template('root.html')

@app.route('/<name>')
@app.errorhandler(404)
def blog(name=None):
    if name == 'ssd':
        return render_template('ssd.html', name=name)
    if name in blog_entries:
        return render_template('post.html', name=name, article="Incoming...")
    else:
        return render_template('missing.html'), 404


if __name__ == "__main__":
    app.run()

