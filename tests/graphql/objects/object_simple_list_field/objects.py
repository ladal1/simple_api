from simple_api.adapters.graphql.graphql import GraphQLAdapter
from simple_api.adapters.utils import generate
from simple_api.object.actions import Action
from simple_api.object.datatypes import PlainListType, IntegerType

from simple_api.adapters.graphql.utils import build_patterns


def non_null(request, params, **kwargs):
    return [i for i in range(10)]


def null(request, params, **kwargs):
    return None


def list_non_null_elem_null(request, params, **kwargs):
    return [1, 2, 3, None, None, None, 7, 8, 9]


actions = {
    "getNonNull": Action(return_value=PlainListType(IntegerType()), exec_fn=non_null),
    "getNull": Action(return_value=PlainListType(IntegerType(nullable=True), nullable=True), exec_fn=null),
    "getListNullElemNonNull": Action(return_value=PlainListType(IntegerType(), nullable=True), exec_fn=null),
    "getListNonNullElemNull": Action(return_value=PlainListType(IntegerType(nullable=True)),
                                     exec_fn=list_non_null_elem_null),
}


schema = generate(GraphQLAdapter, actions)
patterns = build_patterns("api/", schema)
