from simple_api.adapters.graphql.graphql import GraphQLAdapter
from simple_api.adapters.utils import generate
from simple_api.object.actions import Action
from simple_api.object.datatypes import IntegerType, ObjectType, StringType, PlainListType
from simple_api.object.object import Object
from simple_api.utils import AttrDict

from simple_api.adapters.graphql.utils import build_patterns


def resolve(request, parent_val, params, **kwargs):
    return parent_val["records"][params["offset"]:(params["offset"] + params["limit"])]


class Person(Object):
    fields = {
        "name": StringType(),
        "age": IntegerType(),
    }


class PersonList(Object):
    output_fields = {
        "count": IntegerType(),
    }
    fields = {
        "records": PlainListType(
            ObjectType(Person),
            parameters={
                "limit": IntegerType(nullable=True, default=20),
                "offset": IntegerType(nullable=True, default=0),
            },
            resolver=resolve
        )
    }


def get(request, params, **kwargs):
    return AttrDict(count=len(params["input"]), records=params["input"])


actions = {
    "get": Action(parameters={"input": ObjectType(PersonList)}, return_value=ObjectType(PersonList), exec_fn=get)
}


schema = generate(GraphQLAdapter, actions)
patterns = build_patterns("api/", schema)
