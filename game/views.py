from django.shortcuts import render

# Create your views here.

class MainView():

    """
    A view of the main game page.
    """
    # We cannot easily override FormView since this view uses multiple forms

    template_name = "game/main.html"
