# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from forms import SeoAnalyserForm
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
app.config.from_object('config')


@app.route('/', methods=['GET', 'POST'])
def google_position():
    bsObj_test = None
    error = None
    form = SeoAnalyserForm(request.form)
    if request.method == 'POST':
        if form.validate():
            keywords = request.form['keywords'].replace(' ', '+')
            requested_url = 'https://www.google.fr/search?q=' + keywords
            html_response = requests.get(requested_url)
            print(html_response.status_code)

            data = html_response.content
            bsObj = BeautifulSoup(data, "html.parser")
            bsObj_test = bsObj.prettify()
            # print(bsObj.prettify())
            test = bsObj.find('cite', {'class': '_Rm'})
            print(test)

    return render_template(
        'index.html',
        form=form, error=error, bsObj_test=bsObj_test)
