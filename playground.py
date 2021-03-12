from flask import Flask, render_template 
app = Flask(__name__)    

@app.route('/play')
def index():
    return render_template('/index.html', times = 3, color = 'rgb(154, 188, 247)')

@app.route('/play/<int:times>')
def repeat(times):
    return render_template('/index.html', times= int(times), color = 'rgb(154, 188, 247)')

@app.route('/play/<int:times>/<color>')
def repeat_with_color(times, color):
    return render_template('/index.html', times= int(times), color=color)

if __name__=="__main__":   
    app.run(debug=True)  
    