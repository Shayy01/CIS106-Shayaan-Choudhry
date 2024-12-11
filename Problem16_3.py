def parse_csv():
  def split_csv(line):
      return [item.strip() for item in line.split(",")]

  def process_csv():
      line = input("Enter a line of comma-separated values: ")
      items = split_csv(line)
      for item in items:
          print(item)

  process_csv()
