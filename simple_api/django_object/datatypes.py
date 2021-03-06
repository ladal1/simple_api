from simple_api.object.datatypes import ObjectType, PlainListType, IntegerType
from simple_api.object.object import Object, ObjectMeta
from simple_api.object.registry import object_storage
from simple_api.utils import AttrDict

DEFAULT_LIMIT = 20


def resolve_filtering(request, parent_val, params, **kwargs):
    filters = params.pop("filters", {})
    ordering = filters.pop("ordering", ())
    qs = parent_val.filter(**filters).order_by(*ordering)
    return AttrDict(count=qs.count(), data=qs)


class PaginatedList(ObjectType):
    def __init__(self, to, nullable=False, default=None,
                 nullable_if_input=None, default_if_input=None, **kwargs):
        super().__init__(to=to, nullable=nullable, default=default, resolver=resolve_filtering,
                         nullable_if_input=nullable_if_input, default_if_input=default_if_input, **kwargs)

    def convert(self, adapter, **kwargs):
        self.set_ref()
        object_name = self.to.__name__
        object_module = self.to.__module__

        cls = object_storage.get(object_module, object_name)
        self.parameters = {"filters": ObjectType(cls.filter_type, nullable=True)}

        list_cls = object_storage.get(object_module, object_name + "List")
        obj = ObjectType(list_cls, parameters=self.parameters)
        obj.resolver = self.resolver
        return obj.convert(adapter, **kwargs)

    def to_string(self):
        return "Paginated[{}]".format(self.to.__name__)


def create_associated_list_type(cls):
    def resolve_pagination(request, parent_val, params, **kwargs):
        return parent_val[params["offset"]:(params["offset"] + params["limit"])]

    attrs = {
        "fields": {
            "count": IntegerType(),
            "data": PlainListType(
                ObjectType(cls),
                parameters={
                    "limit": IntegerType(nullable=True, default=DEFAULT_LIMIT),
                    "offset": IntegerType(nullable=True, default=0),
                },
                resolver=resolve_pagination
            )
        },
        "hidden": True,
    }
    ObjectMeta(cls.__name__ + "List", (Object,), attrs, module=cls.__module__)
