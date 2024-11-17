from django import template
from superadmin.models import *
from datetime import datetime
import os
# import requests

register = template.Library()


@register.simple_tag()
def instructorname(id):
    try:
        course = Courses.objects.get(id=id)
        course = course.title
    except:
        course = None
    return course

