from pyramid.httpexceptions import HTTPError
from pyramid.httpexceptions import HTTPNotFound
from oekocms.views import error_view
from oekocms.views import exception_decorator
from fanstatic import Library
from fanstatic import Resource
import kotti.static as ks


lib_oekocms = Library('oekocms', 'static')
view_css =  Resource(lib_oekocms, "layout.css", depends=[ks.view_css])
edit_css =  Resource(lib_oekocms, "edit.css", depends=[ks.edit_css])
nav_css =  Resource(lib_oekocms, "primary-navigation.css")


def add_fanstatic_resources(config):
    ks.view_needed.add(view_css)
    ks.view_needed.add(nav_css)
    ks.edit_needed.add(edit_css)


def includeme(config):
    config.include('pyramid_zcml')
    config.load_zcml('configure.zcml')
    config.add_view(
        error_view,
        context=HTTPNotFound,
        renderer='oekocms:templates/view/error-404.pt',
    )
    config.add_view(
        error_view,
        context=HTTPError,
        renderer='oekocms:templates/view/error.pt',
    )
    config.add_view(
        error_view,
        decorator=exception_decorator,
        context=Exception,
        renderer='oekocms:templates/view/error.pt',
    )
    config.add_static_view('static-oekocms', 'oekocms:static')
    config.override_asset('kotti', 'oekocms:kotti-overrides/')
    add_fanstatic_resources(config)