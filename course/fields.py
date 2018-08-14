from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_fields = for_fields
        super(OrderField, self).__init__(*args, **kwargs)


    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            print("instance", model_instance,type(model_instance))
            print("self.attname", self.attname)
            print(getattr(model_instance, self.attname))
            try:
                qs = self.model.objects.all()
                print("qs", qs)
                if self.for_fields:
                    print("self.for_fields", self.for_fields)
                    for field in self.for_fields:
                        print(field)
                        print(getattr(model_instance, field))
                    query = {field: getattr(model_instance, field) for field in self.for_fields}
                    print("query", query)
                    qs = qs.filter(**query)
                    print("qs", qs)
                last_item = qs.latest(self.attname)
                print("last_item", last_item)
                value = last_item.order + 1
                print("value", value)
            except ObjectDoesNotExist:
                value = 0
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(OrderField, self).pre_save(model_instance, add)
