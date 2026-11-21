# Sample price per square foot (in rupees) for each location
LOCATION_PRICES = {
    "Bengaluru": 9500,
    "Hyderabad": 8000,
    "Chennai": 6300,
    "Pune": 7500,
    "Mumbai": 17500,
    "Kurnool": 4800,
}

# Furnishing adjustment: extra % added to the price
FURNISHING_ADJUSTMENT = {
    "Unfurnished": 0.00,       # no change
    "Semi-Furnished": 0.05,    # +5%
    "Fully-Furnished": 0.10,   # +10%
}

# Fixed amount added for each bedroom and bathroom
PRICE_PER_BEDROOM = 100000
PRICE_PER_BATHROOM = 50000

# Older houses are cheaper: 1% reduction per year, but never more than 30%
AGE_REDUCTION_PER_YEAR = 0.01
MAX_AGE_REDUCTION = 0.30


def calculate_price(location, area, bhk, bathrooms, age, furnishing):
    # Step 1: area x price per square foot of that location
    price_per_sqft = LOCATION_PRICES[location]
    price = area * price_per_sqft

    # Step 2: add amount for bedrooms and bathrooms
    price = price + (bhk * PRICE_PER_BEDROOM)
    price = price + (bathrooms * PRICE_PER_BATHROOM)

    # Step 3: add furnishing percentage
    price = price + (price * FURNISHING_ADJUSTMENT[furnishing])

    # Step 4: reduce price based on property age
    reduction = age * AGE_REDUCTION_PER_YEAR
    if reduction > MAX_AGE_REDUCTION:
        reduction = MAX_AGE_REDUCTION
    price = price - (price * reduction)

    # Returns a whole number (no decimals)
    return int(price)