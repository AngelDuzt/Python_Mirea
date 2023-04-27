from contextlib import contextmanager


class HTML:
    _result = ''

    @contextmanager
    def body(self):
        self._result += '<body>\n'
        yield
        self._result += '</body>'

    @contextmanager
    def div(self):
        self._result += '<div>\n'
        yield
        self._result += '</div>\n'

    def p(self, string):
        self._result += '<p>' + string + '</p>\n'

    def get_code(self):
        print(self._result)


html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')
html.get_code()