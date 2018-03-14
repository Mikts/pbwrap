# Python Pastebin API Wrapper (ppaw)

>**The wrapper is still a WIP take the following usage guide   
with a grain of salt and expect things to change.**  

>**Simple python wrapper for the Pastebin Public API.  
Lifetime pro endpoints are not yet supported!**  
**Only  _Python 3_ supported at the moment!**

## Documentation

This wrapper is based on **Pastebin** API read their Documentation [**here.**](https://pastebin.com/api)

### Usage
Import and instantiate a Pastebin Object.
```Python
import ppaw

pastebin = ppaw.Pastebin(dev_key)
```

### Examples

##### Get User Id
Returns a string with the user_id created after authentication.
```Python
user_id = pastebin.get_user_id(dev_key, username, password)
```

##### Get Trending Pastes details
Returns a list containing Paste objects of the top 18 trending Pastes.

```Python
trending_pastes = pastebin.get_trending(dev_key)
```
