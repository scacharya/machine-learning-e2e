# Keep all module specific, one time only code here
import mle2e
from enum import Enum

class DataTypes(Enum):
    CSV = 1
    ZIP = 2
    GZIP = 3
    TABLE = 4

print("Module", __name__, " initialized...")
