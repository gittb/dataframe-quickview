# File: dataframe_quickview/__init__.py
import pandas as pd
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def quickview(df):
    app.config['df'] = df
    app.run()

pd.DataFrame.quickview = quickview

@app.route("/")
def home():
    df = app.config['df']
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    start = (page - 1) * per_page
    end = start + per_page
    data = df.iloc[start:end].to_dict(orient='records')
    total_pages = (len(df) // per_page) + 1
    return render_template("index.html", data=data, columns=list(df.columns), total_pages=total_pages, current_page=page)

@app.route("/histogram", methods=['POST'])
def histogram():
    column = request.form['column']
    df = app.config['df']
    histogram_data = df[column].value_counts().to_dict()
    return jsonify(histogram_data)

if __name__ == "__main__":
    data = {'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10], 'C': [3, 6, 9, 12, 15]}
    df = pd.DataFrame(data)

    df.quickview()
