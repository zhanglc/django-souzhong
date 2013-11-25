# -*- coding: utf-8 -*-
import datetime
from models import Magnet
from haystack import indexes


class MagnetIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    term = indexes.CharField(model_attr='term')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Magnet

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(pub_date__lte = datetime.datetime.now())