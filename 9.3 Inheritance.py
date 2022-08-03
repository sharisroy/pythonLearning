class Country:
    def nameOfCountry(self):
        print("Bangladesh")


class City(Country):
    def nameOfCity(self):
        print("Dhaka")


class District(City):
    def nameOfDistrict(self):
        print("Mirpur")


class Thana(District):
    def nameOfThana(self):
        print("Mirpur Model Thana")

t = Thana()
t.nameOfCountry()
t.nameOfCity()
t.nameOfDistrict()
t.nameOfThana()