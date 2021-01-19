from import_export import resources
from .models import Bank

class BankResource(resources.ModelResource):
    class meta:
        model = Bank