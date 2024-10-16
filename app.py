from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def test():
    return render_template('index.html')
#calls code in index.html and displays on page

if __name__ == "__main__":
    app.run(debug=True, port=5001)
#same as main program (public static void main(String[] args)) for java

# @app.route('/')
#def main_page():
#   return render_template('index.html')
# this runs a page for the web app called index.html - change this for different file names
