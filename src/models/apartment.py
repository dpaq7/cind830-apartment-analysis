class Apartment:
    def __init__(self, id=None, category=None, title=None, body=None, amenities=None, 
                 bathrooms=None, bedrooms=None, currency=None, fee=None, has_photo=None,
                 pets_allowed=None, price=None, price_display=None, price_type=None,
                 square_feet=None, address=None, cityname=None, state=None,
                 latitude=None, longitude=None, source=None, time=None):
        self.id = id
        self.category = category
        self.title = title
        self.body = body
        self.amenities = amenities
        self.bathrooms = bathrooms
        self.bedrooms = bedrooms
        self.currency = currency
        self.fee = fee
        self.has_photo = has_photo
        self.pets_allowed = pets_allowed
        self.price = price
        self.price_display = price_display
        self.price_type = price_type
        self.square_feet = square_feet
        self.address = address
        self.cityname = cityname
        self.state = state
        self.latitude = latitude
        self.longitude = longitude
        self.source = source
        self.time = time
    
    def get_summary(self):
        return f"Apartment ID: {self.id}\nPrice: {self.price_display}\nSize: {self.square_feet} sq ft\nLocation: {self.cityname}, {self.state}\nBedrooms: {self.bedrooms}\nBathrooms: {self.bathrooms}"
    
    def __str__(self):
        return self.get_summary()
    
    def __repr__(self):
        return f"Apartment(id={self.id}, price={self.price}, city='{self.cityname}')"