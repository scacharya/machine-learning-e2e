<<<<<<< HEAD
"""
This file is loaded (only) one with the module

Keeping track of all the known data source
1) local CSV file
2) Remote CSV file
"""

=======
# Keep all module specific, one time only code here
import mle2e
from enum import Enum

class DataTypes(Enum):
    CSV = 1
    ZIP = 2
    GZIP = 3
    TABLE = 4

print("Module", __name__, " initialized...")
>>>>>>> e2af0991ee6b82f7658116e0a001c96183496403
