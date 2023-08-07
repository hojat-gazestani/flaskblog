from flask import Flask, render_template
app = Flask(__name__)

posts = [
    { 
        'author': 'Arman',
        'title': 'Blog Post 1',
        'content': 'First post contenct',
        'data_posted': 'April 23, 2023'
    },
    { 
        'author': 'Hojat',
        'title': 'Blog Post 2',
        'content': 'Second post contenct',
        'data_posted': 'April 23, 2023'
    },
]

@app.route("/")
@app.route("/home")
def home():
    return(render_template('home.html', posts=posts))

@app.route("/about")
def about():
    return(render_template('about.html', title='About'))

if __name__ == '__main__':
    app.run(debug=True)

