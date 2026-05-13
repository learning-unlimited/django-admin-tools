"""
Dashboard registry.
"""


class Registry(object):
    """
    Registry for application dashboards.
    """
    registry = {}

    def register(cls, klass, app_name):
        from admin_tools.dashboard.dashboards import Dashboard
        if not issubclass(klass, Dashboard):
            raise ValueError('%s is not an instance of Dashboard' % klass)
        if app_name in cls.registry:
            raise ValueError(
                'A dashboard has already been registered for app "%s"' %
                app_name
            )
        cls.registry[app_name] = klass
    register = classmethod(register)


def register(cls, *args, **kwargs):
    """
    Register a custom dashboard into the global registry.
    """
    Registry.register(cls, *args, **kwargs)


def autodiscover(blacklist=[]):
    """
    Automagically discover custom dashboards and menus for installed apps.
    Optionally you can pass a ``blacklist`` of apps that you don't want to
    provide their own app index dashboard.
    """
    from django.conf import settings
    from importlib import import_module, util

    blacklist.append('admin_tools.dashboard')
    blacklist.append('admin_tools.menu')
    blacklist.append('admin_tools.theming')

    for app in settings.INSTALLED_APPS:
        # skip blacklisted apps
        if app in blacklist:
            continue

        # try to import the app
        try:
            import_module(app).__path__
        except AttributeError:
            continue

        if util.find_spec('%s.dashboard' % app) is None:
            continue

        # looks like we found it so import it !
        import_module('%s.dashboard' % app)
