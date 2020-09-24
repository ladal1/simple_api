from functools import singledispatch

from django.db.models import IntegerField, AutoField, CharField, TextField

from django_object.utils import extract_fields_from_model, filter_fields_from_model
from object.datatypes import IntegerType, PlainListType, BooleanType, StringType
from utils import Storage


@singledispatch
def determine_filters_for_django_field(field):
    return {}


@determine_filters_for_django_field.register(AutoField)
@determine_filters_for_django_field.register(IntegerField)
def determine_filters_for_integer(field):
    return {
        "exact": IntegerType(),
        "gt": IntegerType(),
        "gte": IntegerType(),
        "in": PlainListType(IntegerType()),
        "isnull": BooleanType(),
        "lt": IntegerType(),
        "lte": IntegerType(),
    }


@determine_filters_for_django_field.register(CharField)
@determine_filters_for_django_field.register(TextField)
def determine_filters_for_string(field):
    return {
        "contains": StringType(),
        "endswith": StringType(),
        "icontains": StringType(),
        "in": PlainListType(StringType()),
        "iregex": StringType(),
        "isnull": BooleanType(),
        "regex": StringType(),
        "startswith": StringType(),
    }


def determine_filters(model, only_fields, exclude_fields):
    fields = filter_fields_from_model(model, only_fields, exclude_fields)
    filters = {}
    for name, field in fields.items():
        for filter_name, filter_type in determine_filters_for_django_field(field).items():
            filters["{}__{}".format(name, filter_name)] = filter_type
    return filters


class ModelFiltersStorage(Storage):
    def store(self, model, cls):
        self.get(model)
        to_keep = set(determine_filters(model, tuple(cls.fields.keys()), None).keys())
        to_remove = set(self.storage[model].keys()).difference(to_keep)
        for key in to_remove:
            del self.storage[model][key]

    def get(self, model):
        if model not in self.storage:
            self.storage[model] = determine_filters(model, None, None)
        return self.storage[model]


model_filters_storage = ModelFiltersStorage()