from graphene_django.utils import GraphQLTestCase

from adapters.utils import generate
from adapters.graphql.graphql import GraphQLAdapter
from object.actions import Action
from object.fields import StringField
from object.object import Object
from tests.graphql_test_utils import get_graphql_url, remove_ws


def non_null(*args, **kwargs):
    return "nonNull"


def null(*args, **kwargs):
    return None


class Actions(Object):
    actions = {
        "non_null": Action(return_value=StringField(), exec_fn=null),
        "null": Action(return_value=StringField(nullable=True), exec_fn=non_null)
    }


schema = generate(GraphQLAdapter, [Actions])


class Test(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    GRAPHQL_URL = get_graphql_url(__file__)

    def test_schema(self):
        self.assertEqual(
            remove_ws(str(self.GRAPHQL_SCHEMA)),
            remove_ws(
                """
                schema {
                  query: Query
                }

                type Query {
                  nonNull: String!
                  null: String
                }
                """
            )
        )

    def test_request_non_null(self):
        resp = self.query(
            """
            query{
              nonNull
            }
            """
        )

        self.assertResponseHasErrors(resp)

    def test_request_null(self):
        resp = self.query(
            """
            query{
              null
            }
            """
        )

        exp = {
          "data": {
            "null": "nonNull"
          }
        }

        self.assertResponseNoErrors(resp)
        self.assertJSONEqual(resp.content, exp)
