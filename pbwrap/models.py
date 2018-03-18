class Paste(object):
    """Defines a Paste from Pastebin paste contains the following fields:
       key,
       date,
       title,
       size,
       expire_date,
       private,
       format_short,
       format_long,
       url,
       hits.
    """

    def __init__(self, paste_dict):
        for k, v in paste_dict.items():
            setattr(self, k, v)

    def __cmp__(self, x):
        return vars(self) == vars(x)


class User(object):
    """Defines a user contains the following fields:
       name
       format_short
       expiration
       avatar_url
       private
       website
       email
       location
       account_type
    """
    def __init__(self, user_dict):
        for k, v in user_dict.items():
            setattr(self, k, v)
