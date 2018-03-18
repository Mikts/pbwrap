# Pastebin API wrapper for Python (pbwrap)

>**Python API wrapper for the Pastebin Public API.  
Lifetime pro endpoints are not yet supported!**  
**Only  _Python 3_ supported!**

## Documentation

This wrapper is based on **Pastebin** API read their Documentation [**here.**](https://pastebin.com/api)  
for extra information and usage guide.

### Usage
Import and instantiate a Pastebin Object.
```Python
from pbwrap import Pastebin

pastebin = Pastebin(api_dev_key)
```

### Examples

##### Get User Id
Returns a string with the user_id created after authentication.
```Python
user_id = pastebin.get_user_id(username, password)
```

##### Get Trending Pastes details
Returns a list containing Paste objects of the top 18 trending Pastes.

```Python
trending_pastes = pastebin.get_trending()
```

### Type models

#### Paste

Some API endpoints return paste data in xml format the wrapper either converts them in a python dictionary format  
or returns them as Paste objects which contain the following fields:

* **key**
* **date** in  **_UNIX_**
* **title**
* **size**
* **expire_date**
* **private**
* **format_short**
* **format_long**
* **url**
* **hits**

## License
pbwrap is released under [**MIT License**](../LICENSE)
