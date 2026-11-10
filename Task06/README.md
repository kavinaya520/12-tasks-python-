# Task 6 - Functions

- Returning gives a value back for reuse (amount * 2 works); printing only shows text.
- Local variables exist only inside the function; global variables are visible everywhere.
  Constants can be read inside functions but should not be modified, because that causes hidden changes.
- Every function has a docstring.

| Style | Reuse | Repeated logic | Maintainability |
|---|---|---|---|
| One long script | none | high | poor |
| Functions | high | none | good |
| lambda | for tiny one-line helpers | none | hard to read if long |

Function-call overhead is a small constant per call, so processing n entries is still O(n).
