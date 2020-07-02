from flask import Flask,render_template,request
import analyze_tweet

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/country",methods=['POST'])    
def country():
    return render_template('index.html')

@app.route("/state",methods=['POST'])    
def state():
    return render_template('index.html')

@app.route("/index.html")    
def index2():
    return render_template('index.html')   
    
@app.route("/dashboard.html")    
def dashboard():
    return render_template('dashboard.html')   
    
@app.route("/statistics.html")    
def statistics():
    return render_template('statistics.html')   
    
if __name__ =='__main__':
    analyze_tweet.analyze()
    app.run(debug=True)