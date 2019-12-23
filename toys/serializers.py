from rest_framework import serializers
from toys.models import Toy


class ToySerializer(serializers.ModelSerializer):
    """T"""

    class Meta:
        model = Toy  # model related to the serializer
        fields = ('id',  # field names that we want to include in the serialization within a tuple
                  'name',
                  'description',
                  'release_date',
                  'toy_category',
                  'was_included_in_home'
                  )
