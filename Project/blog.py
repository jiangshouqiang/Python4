
from django.db import models

urls = (
    '/','Index',
    '/view/(\d+)','View',
    '/delete/(\d+)','Delete',
    '/edit/(\d+)','Edit',
)

t_globals = {
    'datestr':web.datestr
}

