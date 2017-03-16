from src import debug


class DictObj(dict):
    """
        Class DictObj, which allows to access to the dictionary values like attributes
    """
    def __init__(self, *args, **kwargs):
        """
            Class constructor
        """
        super().__init__(*args, **kwargs)
        for key, value in self.items():
            if type(value) is dict:
                value = DictObj(value)
            # Add keys and values to object to have access them.
            # Especially important for nested dict.
            self[key] = value

    def __setattr__(self, name, value):
        """
            @see python customizing attribute access (Magic Methods)
        """
        self[name] = value

    def __getattr__(self, name):
        """
            @see python customizing attribute access (Magic Methods)
        """
        try:
            return self[name]
        except (KeyError, AttributeError):
            debug.log().error("Invalid key '{}' of object '{}'".format(name, self))

    def __setitem__(self, key, value):
        """
            @see python customizing attribute access (Magic Methods)
        """
        if type(value) is dict:
            value = DictObj(value)
        super().__setitem__(key, value)  # super() for avoid recursion

    def __getitem__(self, item):
        """
            @see python customizing attribute access (Magic Methods)
        """
        try:
            value = None
            tmp = super().__getitem__(item)  # super() for avoid recursion
            # Check on empty dictionary, for avoid wrong value.
            # Because the check of empty dictionary get False.
            # In this case, condition would be skipping and method return value equal None.
            if not tmp or tmp:
                value = tmp
                if type(value) is dict:
                    value = DictObj(value)
            return value
        except (KeyError, AttributeError):
            debug.log().error("Invalid key '{}' of object '{}'".format(item, self))
