def scroll_text():
  def duplicate_text(text, length):
      while len(text) < length:
          text += text
      return text[:length]

  def shift_text(text, direction):
      if direction == "right":
          return text[-1] + text[:-1]
      elif direction == "left":
          return text[1:] + text[0]

  try:
      text = input("Enter a line of text: ")
      char_per_line = int(input("Enter the number of characters per line: "))
      num_lines = int(input("Enter the number of lines to print: "))
      direction = input("Enter scroll direction (left or right): ").strip().lower()
      if direction not in ("left", "right"):
          raise ValueError("Scroll direction must be 'left' or 'right'.")

      duplicated_text = duplicate_text(text, char_per_line)
      for _ in range(num_lines):
          print(duplicated_text)
          duplicated_text = shift_text(duplicated_text, direction)
  except ValueError as e:
      print(f"Error: {e}")
