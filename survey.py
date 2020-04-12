from flask import Flask, render_template, request, redirect
app=Flask(__name__)

@app.route('/')
def fill_the_form():
    return render_template('form.html')

@app.route('/result', methods=['POST'])
def confirm_survey():
    print('*'*50)
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form['location']
    language_from_form = request.form['coding language']
    comment_from_form = request.form['comment']
    return render_template("result.html", name=name_from_form, location=location_from_form,language=language_from_form,comment=comment_from_form)

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again."
if __name__== '__main__':
    app.run(debug=True)