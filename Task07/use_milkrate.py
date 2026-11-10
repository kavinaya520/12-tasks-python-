"""Second script: imports milkrate and calls payout()."""
import sys
import milkrate
import milkrate as mr
from milkrate import payout

print("payout(10, 3.5, 8.5)    =", payout(10, 3.5, 8.5))
print("milkrate.payout(...)    =", milkrate.payout(8.5, 4.2, 8.7))
print("mr.rate_per_litre(...)  =", mr.rate_per_litre(3.1, 8.3))
print("milkrate cached in sys.modules:", "milkrate" in sys.modules)
print("first sys.path entry (current directory):", sys.path[0] or "(cwd)")
