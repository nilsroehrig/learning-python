import justpy as jp


def app():
    page = jp.QuasarPage()
    headline = jp.H1(a=page, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    paragraph = jp.QDiv(a=page, text="These graphs represent course review analysis")
    return page


jp.justpy(app)
