from flask import Flask, render_template
app = Flask(__name__)
#in the function return render_template(‘index.html’)
@app.route("/index")
def me():
    #Create a variable
    name = 'Flask1'
    return render_template('index.html', index_variable = name)
@app.route("/mother")
def mother():
    #Create a variable
    name = 'Flask2'
    return render_template('mother.html', index_variable = name)   
app.run(debug=True)
@app.route("/friend")
def friend():
    #Create a variable
    name = 'Flask3'
    return render_template('friend.html', index_variable = name)   
app.run(debug=True)
@app.route("/father")
def father():
    #Create a variable
    name = 'Flask4'
    return render_template('father.html', index_variable = name)   
app.run(debug=True)



