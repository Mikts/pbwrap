# Pastebin API wrapper for Python (pbwrap)
[![PyPI version](https://badge.fury.io/py/pbwrap.svg)](https://badge.fury.io/py/pbwrap)
[![Build Status](https://travis-ci.org/Mikts/pbwrap.svg?branch=master)](https://travis-ci.org/Mikts/pbwrap)
[![Coverage Status](https://coveralls.io/repos/github/Mikts/pbwrap/badge.svg)](https://coveralls.io/github/Mikts/pbwrap)


>**Python API wrapper for the Pastebin Public API.  
**Only  _Python 3_ supported!**

## Documentation

This wrapper is based on **Pastebin** API read their Documentation [**here.**](https://pastebin.com/doc_api)  
for extra information and usage guide.

### Usage
For a full list of the methods offered by the package [**Read.**](http://pbwrap.readthedocs.io/en/latest/)

#### Quickstart
Import and instantiate a Pastebin Object.
```Python
from pbwrap import Pastebin

pastebin = Pastebin(api_dev_key)
```

### Examples

##### Get User Id
Returns a string with the user_id created after authentication.
```Python
user_id = pastebin.authenticate(username, password)
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
* **date** in  **_UNIXTIME_**
* **title**
* **size**
* **expire_date**
* **private**
* **format_short**
* **format_long**
* **url**
* **hits**

## License
pbwrap is released under [**MIT License**](./LICENSE)
