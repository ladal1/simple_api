from .objects import schema
from tests.graphql.graphql_test_utils import remove_ws, GraphQLTestCase


class Test(GraphQLTestCase):
    GRAPHQL_SCHEMA = schema
    REF_GRAPHQL_SCHEMA = """
        schema {
          query: Query
          mutation: Mutation
        }
        
        type ActionInfo {
          name: String!
          parameters: [FieldInfo!]!
          data: [FieldInfo!]!
          return_type: String!
          permitted: Boolean!
          deny_reason: String
          retry_in: Duration
          mutation: Boolean!
          __str__: String!
        }
        
        scalar Duration
        
        type FieldInfo {
          name: String!
          typename: String!
          default: String
          __str__: String!
        }
        
        type Mutation {
          ShortCustomUserCreate(data: ShortCustomUserCreateInput!): ShortCustomUser!
          ShortCustomUserUpdate(data: ShortCustomUserUpdateInput!, id: Int!): ShortCustomUser!
          ShortCustomUserDelete(id: Int!): Boolean!
          ShortPostCreate(data: ShortPostCreateInput!): ShortPost!
          ShortPostUpdate(data: ShortPostUpdateInput!, id: Int!): ShortPost!
          ShortPostDelete(id: Int!): Boolean!
        }
        
        type ObjectInfo {
          name: String!
          pk_field: String
          actions: [ActionInfo!]!
          __str__: String!
        }
        
        type Query {
          ShortPostDetail(id: Int!): ShortPost!
          ShortPostList(filters: ShortPostFiltersInput): ShortPostList!
          ShortCustomUserDetail(id: Int!): ShortCustomUser!
          ShortCustomUserList(filters: ShortCustomUserFiltersInput): ShortCustomUserList!
          __types: [TypeInfo!]!
          __objects: [ObjectInfo!]!
          __actions: [ActionInfo!]!
        }
        
        type ShortCustomUser {
          id: Int!
          first_name: String!
          last_name: String!
          full_name: String!
          __str__: String!
          __actions: [ActionInfo!]!
        }
        
        input ShortCustomUserCreateInput {
          first_name: String!
          last_name: String!
        }
        
        input ShortCustomUserFiltersInput {
          id: Int
          id__exact: Int
          id__gt: Int
          id__gte: Int
          id__in: [Int!]
          id__isnull: Boolean
          id__lt: Int
          id__lte: Int
          first_name: String
          first_name__contains: String
          first_name__endswith: String
          first_name__exact: String
          first_name__icontains: String
          first_name__in: [String!]
          first_name__iregex: String
          first_name__isnull: Boolean
          first_name__regex: String
          first_name__startswith: String
          last_name: String
          last_name__contains: String
          last_name__endswith: String
          last_name__exact: String
          last_name__icontains: String
          last_name__in: [String!]
          last_name__iregex: String
          last_name__isnull: Boolean
          last_name__regex: String
          last_name__startswith: String
          ordering: [String!]
        }
        
        type ShortCustomUserList {
          count: Int!
          data(limit: Int = 20, offset: Int = 0): [ShortCustomUser!]!
          __str__: String!
        }
        
        input ShortCustomUserUpdateInput {
          first_name: String
          last_name: String
        }
        
        type ShortPost {
          id: Int!
          title: String!
          author: ShortCustomUser!
          __str__: String!
          __actions: [ActionInfo!]!
        }
        
        input ShortPostCreateInput {
          title: String!
          author_id: Int!
        }
        
        input ShortPostFiltersInput {
          id: Int
          id__exact: Int
          id__gt: Int
          id__gte: Int
          id__in: [Int!]
          id__isnull: Boolean
          id__lt: Int
          id__lte: Int
          title: String
          title__contains: String
          title__endswith: String
          title__exact: String
          title__icontains: String
          title__in: [String!]
          title__iregex: String
          title__isnull: Boolean
          title__regex: String
          title__startswith: String
          author_id: Int
          author_id__exact: Int
          author_id__gt: Int
          author_id__gte: Int
          author_id__in: [Int!]
          author_id__isnull: Boolean
          author_id__lt: Int
          author_id__lte: Int
          ordering: [String!]
        }
        
        type ShortPostList {
          count: Int!
          data(limit: Int = 20, offset: Int = 0): [ShortPost!]!
          __str__: String!
        }
        
        input ShortPostUpdateInput {
          title: String
          author_id: Int
        }
        
        type TypeInfo {
          typename: String!
          fields: [FieldInfo!]!
          __str__: String!
        }
    """

    REF_META_SCHEMA = {
        "data": {
            "__types": [
                {
                    "typename": "ShortCustomUserFilters",
                    "fields": [
                        {
                            "name": "id",
                            "typename": "Integer"
                        },
                        {
                            "name": "id__exact",
                            "typename": "Integer"
                        },
                        {
                            "name": "id__gt",
                            "typename": "Integer"
                        },
                        {
                            "name": "id__gte",
                            "typename": "Integer"
                        },
                        {
                            "name": "id__in",
                            "typename": "[Integer!]"
                        },
                        {
                            "name": "id__isnull",
                            "typename": "Boolean"
                        },
                        {
                            "name": "id__lt",
                            "typename": "Integer"
                        },
                        {
                            "name": "id__lte",
                            "typename": "Integer"
                        },
                        {
                            "name": "first_name",
                            "typename": "String"
                        },
                        {
                            "name": "first_name__contains",
                            "typename": "String"
                        },
                        {
                            "name": "first_name__endswith",
                            "typename": "String"
                        },
                        {
                            "name": "first_name__exact",
                            "typename": "String"
                        },
                        {
                            "name": "first_name__icontains",
                            "typename": "String"
                        },
                        {
                            "name": "first_name__in",
                            "typename": "[String!]"
                        },
                        {
                            "name": "first_name__iregex",
                            "typename": "String"
                        },
                        {
                            "name": "first_name__isnull",
                            "typename": "Boolean"
                        },
                        {
                            "name": "first_name__regex",
                            "typename": "String"
                        },
                        {
                            "name": "first_name__startswith",
                            "typename": "String"
                        },
                        {
                            "name": "last_name",
                            "typename": "String"
                        },
                        {
                            "name": "last_name__contains",
                            "typename": "String"
                        },
                        {
                            "name": "last_name__endswith",
                            "typename": "String"
                        },
                        {
                            "name": "last_name__exact",
                            "typename": "String"
                        },
                        {
                            "name": "last_name__icontains",
                            "typename": "String"
                        },
                        {
                            "name": "last_name__in",
                            "typename": "[String!]"
                        },
                        {
                            "name": "last_name__iregex",
                            "typename": "String"
                        },
                        {
                            "name": "last_name__isnull",
                            "typename": "Boolean"
                        },
                        {
                            "name": "last_name__regex",
                            "typename": "String"
                        },
                        {
                            "name": "last_name__startswith",
                            "typename": "String"
                        },
                        {
                            "name": "ordering",
                            "typename": "[String!]"
                        }
                    ]
                },
                {
                    "typename": "ShortCustomUser",
                    "fields": [
                        {
                            "name": "id",
                            "typename": "Integer!"
                        },
                        {
                            "name": "first_name",
                            "typename": "String!"
                        },
                        {
                            "name": "last_name",
                            "typename": "String!"
                        },
                        {
                            "name": "full_name",
                            "typename": "String!"
                        }
                    ]
                },
                {
                    "typename": "ShortPostFilters",
                    "fields": [
                        {
                            "name": "id",
                            "typename": "Integer"
                        },
                        {
                            "name": "id__exact",
                            "typename": "Integer"
                        },
                        {
                            "name": "id__gt",
                            "typename": "Integer"
                        },
                        {
                            "name": "id__gte",
                            "typename": "Integer"
                        },
                        {
                            "name": "id__in",
                            "typename": "[Integer!]"
                        },
                        {
                            "name": "id__isnull",
                            "typename": "Boolean"
                        },
                        {
                            "name": "id__lt",
                            "typename": "Integer"
                        },
                        {
                            "name": "id__lte",
                            "typename": "Integer"
                        },
                        {
                            "name": "title",
                            "typename": "String"
                        },
                        {
                            "name": "title__contains",
                            "typename": "String"
                        },
                        {
                            "name": "title__endswith",
                            "typename": "String"
                        },
                        {
                            "name": "title__exact",
                            "typename": "String"
                        },
                        {
                            "name": "title__icontains",
                            "typename": "String"
                        },
                        {
                            "name": "title__in",
                            "typename": "[String!]"
                        },
                        {
                            "name": "title__iregex",
                            "typename": "String"
                        },
                        {
                            "name": "title__isnull",
                            "typename": "Boolean"
                        },
                        {
                            "name": "title__regex",
                            "typename": "String"
                        },
                        {
                            "name": "title__startswith",
                            "typename": "String"
                        },
                        {
                            "name": "author_id",
                            "typename": "Integer"
                        },
                        {
                            "name": "author_id__exact",
                            "typename": "Integer"
                        },
                        {
                            "name": "author_id__gt",
                            "typename": "Integer"
                        },
                        {
                            "name": "author_id__gte",
                            "typename": "Integer"
                        },
                        {
                            "name": "author_id__in",
                            "typename": "[Integer!]"
                        },
                        {
                            "name": "author_id__isnull",
                            "typename": "Boolean"
                        },
                        {
                            "name": "author_id__lt",
                            "typename": "Integer"
                        },
                        {
                            "name": "author_id__lte",
                            "typename": "Integer"
                        },
                        {
                            "name": "ordering",
                            "typename": "[String!]"
                        }
                    ]
                },
                {
                    "typename": "ShortPost",
                    "fields": [
                        {
                            "name": "id",
                            "typename": "Integer!"
                        },
                        {
                            "name": "title",
                            "typename": "String!"
                        },
                        {
                            "name": "author",
                            "typename": "ShortCustomUser!"
                        }
                    ]
                }
            ],
            "__objects": [
                {
                    "name": "ShortCustomUser",
                    "pk_field": "id",
                    "actions": [
                        {
                            "name": "ShortCustomUserList",
                            "parameters": [
                                {
                                    "name": "filters",
                                    "typename": "ShortCustomUserFilters",
                                    "default": None
                                }
                            ],
                            "data": [],
                            "mutation": False,
                            "return_type": "Paginated[ShortCustomUser]!",
                            "permitted": True,
                            "deny_reason": None,
                            "retry_in": None
                        },
                        {
                            "name": "ShortCustomUserCreate",
                            "parameters": [],
                            "data": [
                                {
                                    "name": "first_name",
                                    "typename": "String!",
                                    "default": None
                                },
                                {
                                    "name": "last_name",
                                    "typename": "String!",
                                    "default": None
                                }
                            ],
                            "mutation": True,
                            "return_type": "ShortCustomUser!",
                            "permitted": True,
                            "deny_reason": None,
                            "retry_in": None
                        }
                    ]
                },
                {
                    "name": "ShortPost",
                    "pk_field": "id",
                    "actions": [
                        {
                            "name": "ShortPostList",
                            "parameters": [
                                {
                                    "name": "filters",
                                    "typename": "ShortPostFilters",
                                    "default": None
                                }
                            ],
                            "data": [],
                            "mutation": False,
                            "return_type": "Paginated[ShortPost]!",
                            "permitted": True,
                            "deny_reason": None,
                            "retry_in": None
                        },
                        {
                            "name": "ShortPostCreate",
                            "parameters": [],
                            "data": [
                                {
                                    "name": "title",
                                    "typename": "String!",
                                    "default": None
                                },
                                {
                                    "name": "author_id",
                                    "typename": "Integer!",
                                    "default": None
                                }
                            ],
                            "mutation": True,
                            "return_type": "ShortPost!",
                            "permitted": True,
                            "deny_reason": None,
                            "retry_in": None
                        }
                    ]
                }
            ],
            "__actions": []
        }
    }
