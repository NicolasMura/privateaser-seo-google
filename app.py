# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from forms import SeoAnalyserForm
app = Flask(__name__)
app.config.from_object('config')


@app.route('/', methods=["GET", "POST"])
def google_position():
    form = SeoAnalyserForm()
    if form.validate():
        print(form)
    return render_template('index.html', form=form)
