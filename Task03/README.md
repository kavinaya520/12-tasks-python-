# Task 3 - Variables and Constants

Python does not enforce constants (there is no const keyword). UPPER_CASE names are a PEP 8
convention that tells other programmers not to reassign them, and reviewers and tools rely on it.

| Approach | Effort to update a rate | Places to change | Time/memory |
|---|---|---|---|
| Magic numbers | high, search the whole program | every occurrence | no difference |
| Named constants | low | 1 | negligible |
| RATE_CARD dictionary | low | 1 entry | tiny lookup cost |

Chosen design: named constants (clear and fast). The dictionary is better when rates change by
season (see Task 12).
