from functools import singledispatch

import graphene

from adapters.graphql.registry import get_class
from object.datatypes import StringType, IntegerType, ObjectType, PlainListType


@singledispatch
def convert_list_output_type(type, adapter, **kwargs):
    raise NotImplementedError


@convert_list_output_type.register(StringType)
def convert_output_string_type(type, adapter, **kwargs):
    if type.nullable:
        return graphene.String
    return graphene.NonNull(graphene.String)


@convert_list_output_type.register(IntegerType)
def convert_output_integer_type(type, adapter, **kwargs):
    if type.nullable:
        return graphene.Int
    return graphene.NonNull(graphene.Int)


@convert_list_output_type.register(ObjectType)
def convert_output_object_type(type, adapter, **kwargs):
    if type.nullable:
        return get_class(type.to).output
    return graphene.NonNull(get_class(type.to).output)


@convert_list_output_type.register(PlainListType)
def convert_output_list_type(type, adapter, **kwargs):
    if type.nullable:
        return graphene.List(type.of.convert(adapter, list=True))
    return graphene.NonNull(graphene.List(type.of.convert(adapter, list=True)))
