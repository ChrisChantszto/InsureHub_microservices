from flask import Flask, request, send_file
from flask_cors import CORS
import json
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os

app = Flask(__name__)
CORS(app)

@app.route('/export-to-pdf', methods=['POST'])
def export_to_pdf():
    data = request.json

    # convert json to html

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('mytemplate.html')
    template_vars = {"data": data}
    html_out = template.render(template_vars)

    # convert html to pdf using weasyprint

    HTML(string=html_out).write_pdf("output.pdf")

    return send_file('output.pdf', as_attachment=True)

@app.route('/output.pdf')
def return_pdf():
    try:
        response = send_file('output.pdf', as_attachment=True)
        print('The download is complete.')
        return response
    except Exception as e:
        return str(e)
    
if __name__ == '__main__':
    app.run(port=5000) 