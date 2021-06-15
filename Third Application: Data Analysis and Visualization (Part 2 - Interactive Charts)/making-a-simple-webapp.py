import justpy as jp


# A Quasar page is like the Main Component for Justpy Web Framework.

def app():
    # QDiv is another component of JustPy.
    wp = jp.QuasarPage() # We are creating a Quasar page object instance. Will return that instance.
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md") # H1 Element
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis", classes="text-body1") # p Element
    return wp

jp.justpy(app) # It expects a function that returns a Quasar page.

# Execute this script and go to: http://127.0.0.1:8000

# NOTE:

# For Quasar styles (to create H, p, other tags and also give ALL kind of styles to the page) go to:
# https://quasar.dev/style/stylus-variables

# In our case, since we want h3 and p tags to work, go to Typography: https://quasar.dev/style/typography

# To create h3 element, we need to assign "text-h3" class to the Div tag, as seen on line 8 above ^^^.

# Every time you make a modification, you have to stop the Web Server by issuing Ctrl + C and then re-run it.
