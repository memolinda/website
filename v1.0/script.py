from flask import Flask

app=Flask(__name__)

@app.route('/') #create a decorator for the home page

def home(): #content in the decorator
    return "Home contents goes here!"

@app.route('/about/') #create an about page

def about():
    return "About contents goes here!"

if __name__=="__main__":
    app.run(debug=True)
