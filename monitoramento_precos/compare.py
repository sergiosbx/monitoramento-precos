class Compare:
    def __init__(self, conf, price):
        self.price = price
        self.last_price = conf.last_price
        self.parameter = conf.parameter
        self.comparison_type = conf.comparison_type.lower()

    def execute(self):
        return getattr(locals()['self'], self.comparison_type)()

    def decrease_margin(self):
        return MarginCompare(self.price, self.last_price, self.parameter).decrease_margin()

    def increase_margin(self):
        return MarginCompare(self.price, self.last_price, self.parameter).increase_margin()

    def variation(self):
        return VariationCompare(self.price, self.last_price, self.parameter).variation()

    def diff(self):
        return self.price != self.last_price

    def less(self):
        return self.price < self.last_price

    def bigger(self):
        return self.price > self.last_price

    def less_than(self):
        return self.price < self.parameter

    def bigger_then(self):
        return self.price > self.parameter


class Margin():
    def __init__(self, last_price, parameter):
        self.last_price = last_price
        self.parameter = parameter

    @property
    def margin(self):
        return self.parameter / 100.00 * self.last_price


class MarginCompare(Margin):

    INCREASE = '+'
    DECREASE = '-'

    def __init__(self, price, last_price, parameter):
        self.price = price
        super().__init__(last_price, parameter)

    def decrease_margin(self):
        return self.price < self._base_value(self.DECREASE)

    def increase_margin(self):
        return self.price > self._base_value(self.INCREASE)

    def _base_value(self, operator):
        return eval(f'{self.last_price} {operator} {self.margin}')


class VariationCompare(Margin):
    def __init__(self, price, last_price, parameter):
        self.price = price
        super().__init__(last_price, parameter)

    def variation(self):
        roof = self.last_price + self.margin
        floor = self.last_price - self.margin
        return self.price > roof or self.price < floor
