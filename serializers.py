from django.core import serializers

# assuming obj is a model instance
serialized_obj = serializers.serialize('json', [ obj, ])