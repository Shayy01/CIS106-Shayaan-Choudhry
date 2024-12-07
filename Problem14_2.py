class Car:
  def __init__(self, make, model, sticker_price):
      self.make = make
      self.model = model
      self.sticker_price = sticker_price

  def discount_price(self):
      return 0.90 * self.sticker_price


class Sport(Car):
  def __init__(self, make, model, sticker_price):
      super().__init__(make, model, sticker_price)
      self.sport_wheels = 'N'
      self.sport_engine = 'N'
      self.sport_interior = 'N'

  def add_sport_wheels(self, option):
      self.sport_wheels = option

  def add_sport_engine(self, option):
      self.sport_engine = option

  def add_sport_interior(self, option):
      self.sport_interior = option

  def price_with_options(self):
      price = self.sticker_price
      if self.sport_wheels == 'Y':
          price += 1000.00
      if self.sport_engine == 'Y':
          price += 3000.00
      if self.sport_interior == 'Y':
          price += 2000.00
      return price


# Test the Sport class
sport_car = Sport('Porsche', '911 Carrera', 120000.00)

# Add options
sport_car.add_sport_wheels('Y')  # Add sport wheels
sport_car.add_sport_engine('Y')  # Add sport engine
sport_car.add_sport_interior('N')  # Do not add sport interior

# Display car details and prices
print(f"Car Make: {sport_car.make}")
print(f"Car Model: {sport_car.model}")
print(f"Sticker Price: ${sport_car.sticker_price:.2f}")
print(f"Discount Price: ${sport_car.discount_price():.2f}")
print(f"Price with Options: ${sport_car.price_with_options():.2f}")
