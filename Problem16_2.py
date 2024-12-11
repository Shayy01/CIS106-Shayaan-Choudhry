def clean_and_reverse():
  def clean_text(text):
      return ' '.join(text.split())

  def reverse_text(text):
      return text[::-1]

  def process_text():
      text = input("Enter a line of text: ")
      cleaned_text = clean_text(text)
      reversed_text = reverse_text(cleaned_text)
      return reversed_text

  print(process_text())