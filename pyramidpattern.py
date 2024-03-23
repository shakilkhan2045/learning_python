def pyramid_pattern(rows):
    for i in range(0, rows):
       for j in range(0, rows - i - 1):
            print(end=" ")
        for j in range(0, i + 1):
            print("*", end=" ")
      print()

# Example usage:
rows = 5
pyramid_pattern(rows)
