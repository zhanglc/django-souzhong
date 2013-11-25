# -*- coding: utf-8 -*-
from django.db import models


class Term(models.Model):
    name = models.CharField('term name', max_length=50, unique=True)

    def __unicode__(self):
        return u'%s' % self.name


class Magnet(models.Model):
    name = models.CharField('magnet name', max_length=255)
    link = models.TextField('magnet link')
    pub_date = models.DateTimeField('date published', auto_now=True)
    term = models.ManyToManyField(Term)
    adult = models.SmallIntegerField('magnet movie type', default=1)

    def __unicode__(self):
        return u'%s' % self.name

    @models.permalink
    def get_absolute_url(self):
        return ('magnet', (), {'magnet_id': self.id, 'name': self.name})