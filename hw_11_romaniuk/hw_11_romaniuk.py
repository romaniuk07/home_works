from abc import ABC, abstractmethod
# Опишіть об'єкти мистецтва для музею. скористайтесь всіма 5 принципами: абстракція, наслідування, поліморфізм,
# скриття, інкапсуляція. додайте property, setter. Створіть хоча-б по одному інстансу кожного класу і викличте методи


class Artwork(ABC):
    def __init__(self, title, artist, year):
        self._title = title
        self._artist = artist
        self._year = year

    def display_info(self):
        print(f"Title: {self._title}\nArtist: {self._artist}\nYear: {self._year}")


class Painting(Artwork):
    def __init__(self, title, artist, year, medium):
        super().__init__(title, artist, year)
        self._medium = medium

    def display_info(self):
        super().display_info()
        print(f"Medium: {self._medium}")


class Sculpture(Artwork):
    def __init__(self, title, artist, year, material):
        super().__init__(title, artist, year)
        self._material = material

    def display_info(self):
        super().display_info()
        print(f"Material: {self._material}")


class Photograph(Artwork):
    def __init__(self, title, artist, year, style):
        super().__init__(title, artist, year)
        self._style = style

    def display_info(self):
        super().display_info()
        print(f"Style: {self._style}")


class DigitalArt(Artwork):
    def __init__(self, title, artist, year, software):
        super().__init__(title, artist, year)
        self._software = software

    def display_info(self):
        super().display_info()
        print(f"Software: {self._software}")


if __name__ == "__main__":
    painting = Painting("Мазня", "Якась жінка", 2023, "Фарба снєжка")
    sculpture = Sculpture("Піраміда", "Размес", 2589, "Ракушняк")
    photograph = Photograph("НЛО", "Хтось", 2010, "Тарілка над Жашковом")
    digital_art = DigitalArt("Дизайн сайту", "Unknown", 2020, "Adobe Photoshop")

    painting.display_info()
    print()
    sculpture.display_info()
    print()
    photograph.display_info()
    print()
    digital_art.display_info()