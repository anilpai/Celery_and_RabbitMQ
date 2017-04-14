from __future__ import absolute_import
from celery import Celery
app = Celery('test_celery',
             broker='amqp://jon:snow@localhost/jon_vhost',
             backend='rpc://',
             include=['test_celery.tasks'])