# -*- coding: utf-8 -*-

from wtforms import Form, StringField, IntegerField
from wtforms.validators import Required, URL


class SeoAnalyserForm(Form):
    website = StringField(
        u'Site web',
        validators=[Required(), URL(message='Adresse invalide')],
        default='www.privateaser.com'
    )
    keywords = StringField(
        u'Mots-clés',
        validators=[Required()]
    )
    max_page = IntegerField(
        u'Descendre jusqu\'à la page',
        default=1
    )
