# Task 7 - Module

- `import milkrate` : use as milkrate.payout(...)
- `from milkrate import payout` : use payout(...) directly
- `import milkrate as mr` : use a short name, mr.payout(...)
- `if __name__ == "__main__":` runs the demo only when the file is run directly. When imported,
  __name__ is "milkrate", so the demo table is not printed (output_use.txt shows this).
- Without this check the demo would print every time the module is imported.
- math and decimal are standard modules (ready-made functions and exact decimal numbers).
- Python looks for modules in the script's directory first, then the folders in sys.path.
- Importing from a module is better than copying functions: a rate revision is made in one file.
  The first import costs a small one-time load; later imports are read from the sys.modules cache.
