""" General-use interface provided by `krakenex`.
Internally, classes are in separate modules, but they are also exported
to the top-level namespace, so the following uses are possible:
.. code-block:: python
   # recommended, unlikely to result in namespace collisions
   import krakenex
   kraken = krakenex.API()
   # OK for simple scripts
   from krakenex import *
   kraken = API()
   # can be explicit in both cases
   # <some import form here>
   kraken = krakenex.api.API()
"""

# "public interface"
from .kraken import KrakenAPI
__all__ = ['API']