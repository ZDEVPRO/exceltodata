from import_export import resources
from home.models import ExeltoData


class ExeltoDataResources(resources.ModelResource):
    class Meta:
        model = ExeltoData
