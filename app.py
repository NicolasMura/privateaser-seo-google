# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from forms import SeoAnalyserForm
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
app.config.from_object('config')


@app.route('/', methods=['GET', 'POST'])
def google_position():
    itemList = []
    itemListDebug = []
    error = None
    form = SeoAnalyserForm(request.form)
    if request.method == 'POST':
        if form.validate():
            # Get html response
            keywords = request.form['keywords'].replace(' ', '+')
            requested_url = 'https://www.google.fr/search?q=' + keywords
            html_response = requests.get(requested_url)
            print(html_response.status_code)
            html_doc = html_response.content

            # Get BeautifulSoup object
            bsObj = BeautifulSoup(html_doc, "html5lib")

            # Get all items in Google SEO results that match 'privateaser.com'
            items = bsObj.find_all('div', {'class': 'g'})
            tags = ['<cite>', '</cite>', '<b>', '</b>']
            for index, item in enumerate(items):
                position = index + 1
                link_raw = item.find('cite')
                link = str(item.find('cite'))
                link.replace('<cite>', '')
                for tag in tags:
                    link = link.replace(tag, '')
                if(link.find('privateaser.com') != -1):
                    itemList.append(
                        {
                            "keywords": keywords,
                            "position": position,
                            "link": link,
                        }
                    )

                itemListDebug.append(
                    {
                        "keywords": keywords,
                        "link_raw": link_raw,
                        "link": link,
                        "position": position,
                    }
                )

    return render_template(
        'index.html',
        form=form, error=error, itemList=itemList, itemListDebug=itemListDebug)
