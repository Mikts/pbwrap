"""Import the main classes of the wrapper."""

from pbwrap.pbwrap import Pastebin
from pbwrap.models import Paste

try:
    from pbwrap.asyncpbwrap import AsyncPastebin
except ImportError:
    pass
