from flask import Flask, render_template, request
from process_text import TextAnalysis

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    '''Renders main html page. If user has previously entered text inputs and submitted them
    the text inputs as well as the calculated similarity score will be disaplayed'''

    # Set default strings if user hasn't entered any text onto the form
    score = ""
    txt1 = "sample text"
    txt2 = "sample text"

    if request.method == 'POST':
        txt1 = str(request.form.get("input1"))
        txt2 = str(request.form.get("input2"))
        obj = TextAnalysis()
        score = obj.similarity_score(txt1, txt2)
    return render_template("homepage.html", score = score, input1 = txt1, input2 = txt2)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')