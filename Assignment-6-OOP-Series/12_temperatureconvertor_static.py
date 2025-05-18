class TemperatureConverter:
    @staticmethod
    def celcius_to_fehrenheit(c):
        return (c * 9 / 5) + 32

print(TemperatureConverter.celcius_to_fehrenheit(38))