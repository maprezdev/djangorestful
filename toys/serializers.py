from rest_framework import serializers
from toys.models import Toy


class ToySerializer(serializers.Serializer):
    # The fields we wish to serialized
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=250)
    release_date = serializers.DateTimeField()
    toy_category = serializers.CharField(max_length=200)
    was_included_in_home = serializers.BooleanField(required=False)

    """
    1. The create method receives the validated data in the validated_data argument.
    2. The code creates and returns a new Toy instance based on the received validated data
    """
    def create(self, validated_data):
        return Toy.objects.create(**validated_data)

    """ 
    1. The update method receives an existing Toy instance that is being updated and the 
    new validated data in the instance and validated_data arguments.
    3. The code updates the values for the attributes of the instance with the updated attribute values retrieved from 
    the validated data.
    2. Finally, the code returns the updated and saved instance.
    """
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.toy_category = validated_data.get('toy_category', instance.toy_category)
        instance.was_included_in_home = validated_data.get('was_included_in_home', instance.was_included_in_home)
        instance.save()
        return instance
