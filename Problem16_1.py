def parse_name():
  try:
      name = input("Enter a first name and last name (e.g., John Doe): ").strip()
      parts = name.split()
      if len(parts) != 2:
          raise ValueError("Input must contain exactly two words: a first name and a last name.")
      first_name, last_name = parts
      print(f"{last_name}, {first_name[0].upper()}.")
  except Exception as e:
      print(f"Error: {e}")
