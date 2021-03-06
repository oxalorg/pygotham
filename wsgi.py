"""WSGI application."""

from werkzeug.contrib.fixers import ProxyFix
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from pygotham import admin, api, frontend

application = DispatcherMiddleware(
    frontend.create_app(), {
        '/admin': admin.create_app(),
        '/api/v1': api.create_app(),
    },
)

application = ProxyFix(application)

if __name__ == '__main__':
    run_simple(
        '0.0.0.0', 5000, application, use_reloader=True, use_debugger=True)
