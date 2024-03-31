class CustomMeta(type):
    prefix = "custom_"

    def __new__(mcs, name, bases, attrs):
        custom_attrs = {}
        for k, v in attrs.items():
            if not (k.startswith("__") and k.endswith("__")):
                custom_k = f"{CustomMeta.prefix}{k}"
                custom_attrs[custom_k] = v
        for k in custom_attrs:
            del attrs[k[len(CustomMeta.prefix):]]
        attrs.update(custom_attrs)
        attrs["__setattr__"] = mcs.__setattr__
        return type.__new__(mcs, name, bases, attrs)

    def __setattr__(self, key, value):
        if not (key.startswith("__") and key.endswith("__")):
            super(type(self), self).__setattr__(f"{CustomMeta.prefix}{key}", value)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


if __name__ == "__main__":
    inst = CustomClass()
    inst.dynamic = "added later"
