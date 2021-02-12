from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import Product

@registry.register_document
class ProductDocument(Document):
    class Index:
        name = 'products'

    url = fields.TextField(attr='get_absolute_url')
    class Django:
        model = Product
        fields = ['id', 'title', 'description']