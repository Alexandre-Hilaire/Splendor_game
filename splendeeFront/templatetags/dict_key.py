from django.template.defaultfilters import register


@register.filter(name='dict_key')
def dict_key(dictionary, key):
    """Returns the given key from a dictionary."""
    try:
        return dictionary[key]
    except TypeError:
        return dictionary.__dict__[key]
