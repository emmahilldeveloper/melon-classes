"""Classes for melon orders."""

class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from!"""

    # the following 2 lines can be included, but are not necessary because 
    # AbstractMelonOrder should never be instantiated directly

    order_type = None
    tax = 0

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""

        if self.species == 'holiday melon':
            base_price = 5 * 1.5
            total = (1 + self.tax) * self.qty * base_price
        else:
            base_price = 5
            total = (1 + self.tax) * self.qty * base_price
            if self.order_type == "international" and self.qty < 10:
                total = ((1 + self.tax) * self.qty * base_price) + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
   
class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    order_type = 'government'

    def __init__(self, species, qty):
        super().__init__(species, qty)
        self.passed_inspection = False
        
    def mark_inspection(self, passed):
        self.passed_inspection = passed


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax = 0.08
    order_type = 'domestic'

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty)

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = 'international'
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)

        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
