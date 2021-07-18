from django.contrib import admin

from tjrapid import settings


class CustomAdminSite(admin.AdminSite):
    def get_app_list(self, request):
        app_list = super().get_app_list(request)
        apps = {x['app_label']: x for x in app_list}
        app_list = []
        for label, model_list in settings.APP_LIST:
            if label not in apps:
                continue
            app = apps[label]
            models = {x['object_name']: x for x in app['models']}
            app['models'] = [models[x] for x in model_list if x in models]
            app_list += [app]
        return app_list
