import pbwrap.formatter as formatter
from pbwrap import Pastebin
from pbwrap.constants import API_OPTIONS
from pbwrap.models import Paste

try:
    import aiohttp

    class AsyncPaste:
        """Defines a Paste from Pastebin paste which contains the following fields:
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

        def __init__(self, paste_dict, verify_ssl=True):
            self.key = None
            self.verify_ssl = verify_ssl
            for k, v in paste_dict.items():
                setattr(self, k, v)

        def __cmp__(self, x):
            return vars(self) == vars(x)

        async def get_raw_text(self):
            """Fetch the text of a paste via the public API.
                :returns: the paste's text
                :rtype: string, None
            """
            if self.key is not None:
                r = await aiohttp.get("https://pastebin.com/raw/" + self.key, **self.general_params())
                return await r.text
            return None

        async def scrape_raw_text(self):
            """Fetch the ext of a paste via the Paid API.
                :returns: the paste's text
                :rtype: string, None
            """
            if self.key is not None:
                parameter = {"i": self.key}
                r = await aiohttp.get(
                    "https://scrape.pastebin.com/api_scrape_item.php", params=parameter,
                    **self.general_params()
                )

                return await r.text
            return None

        def general_params(self):
            """Returns parameters that should be included in every request

                :returns: The options to be passed to aiohttp.*
                :rtype: dictionary
            """
            return {
                "verify_ssl": self.verify_ssl
            }

    class AsyncPastebin(Pastebin):
        """Async version of Pastebin class.

        Represents your communication with the Pastebin API through its functions
        you can use every API endpoint avalaible.

        Most functions require at least an api_dev_key parameter.
        Functions for manipulating your pastes through the API require an api_user_key.
        """

        def __init__(self, dev_key=None, verify_ssl=True):
            """Instantiate a Pastebin Object

            :param api_dev_key: Your API Pastebin key
            :type api_dev_key: string

            :param verify_ssl: If False, skips ssl certificate verification. Default: True
            :type verify_ssl: bool
            """
            super().__init__(api_dev_key=dev_key, verify_ssl=verify_ssl)

        @staticmethod
        async def get_raw_paste(paste_id, verify_ssl=True):
            """Return raw string of given paste_id.

            get_raw_paste(pasted_id)

            :type paste_id: string
            :param paste_id: The ID key of the paste

            :param verify_ssl: If `False`, does not verify ssl certificate. Default: True
            :type verify_ssl: bool

            :returns: the text of the paste
            :rtype: string
            """
            r = await aiohttp.get("https://pastebin.com/raw/" + paste_id, verify_ssl=verify_ssl)
            return await r.text

        @staticmethod
        async def get_archive(verify_ssl=True):
            """Return archive paste link list.Archive contains 25 most recent pastes.

            :param verify_ssl: If `False`, does not verify ssl certificate. Default: True
            :type verify_ssl: bool

            :returns: a list of url strings
            :rtype: list
            """
            r = await aiohttp.get("https://pastebin.com/archive", verify_ssl=verify_ssl)

            return formatter.archive_url_format(await r.text)

        @staticmethod
        async def get_recent_pastes(limit=50, lang=None, verify_ssl=True):
            """get_recent_pastes(limit=50, lang=None)

                Return a list containing dictionaries of paste.

                :param limit: the limit of the items returned defaults to 50
                :type limit: int

                :param lang: return only pastes from certain language defaults to None
                :type lang: string

                :param verify_ssl: If `False`, does not verify ssl certificate. Default: True
                :type verify_ssl: bool

                :returns: list of Paste objects.
                :rtype: list(Paste)
            """
            parameters = {"limit": limit, "lang": lang}

            r = await aiohttp.get(
                "https://scrape.pastebin.com/api_scraping.php", params=parameters,
                verify_ssl=verify_ssl
            )
            paste_list = list()
            for paste in await r.json():
                paste_list.append(AsyncPaste(paste, verify_ssl=verify_ssl))
            return paste_list

except ImportError:
    pass
