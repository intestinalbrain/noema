__author__ = 'master'

from django.shortcuts import render_to_response

def view(template):
    def decor(func):
        def wrapper(*args, **kwargs):
            return render_to_response(template, func(*args, **kwargs))
        return wrapper
    return decor

