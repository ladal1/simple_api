from simple_api.adapters.graphql.graphql import GraphQLAdapter
from simple_api.adapters.utils import generate
from simple_api.django_object.django_object import DjangoObject

from simple_api.adapters.graphql.utils import build_patterns

from .models import CustomUser as CustomUserModel, Book as BookModel, Subscription as SubscriptionModel, Lease as LeaseModel


class CustomUser(DjangoObject):
    model = CustomUserModel


class Book(DjangoObject):
    model = BookModel


class Subscription(DjangoObject):
    model = SubscriptionModel


class Lease(DjangoObject):
    model = LeaseModel


schema = generate(GraphQLAdapter)
patterns = build_patterns("api/", schema)
