def compute_square_footage(length, width, height):
  """Calculate the square footage of the room."""
  floor_ceiling_area = 2 * length * width
  wall_area = 2 * length * height + 2 * width * height
  total_square_footage = floor_ceiling_area + wall_area
  return total_square_footage

def calculate_gallons_needed(square_footage):
  """Calculate the number of gallons of paint needed."""
  gallons_needed = square_footage / 50
  return gallons_needed

def main():
  while True:
      user_input = input("Would you like to calculate paint needs for a room? (Yes or No): ").strip().lower()
      if user_input == 'yes':
          length = float(input("Enter the length of the room (in feet): "))
          width = float(input("Enter the width of the room (in f
