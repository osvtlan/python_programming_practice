class DrawingMaterial:
    def __init__(self, attr_name):
        self.attr_name = attr_name

    def __get__(self, inst, owner):
        return inst.__dict__.get(self.attr_name, None)

    def __set__(self, inst, value):
        allowed_options = ["Oil paints", "Watercolor", "Graphic"]
        if value in allowed_options:
            inst.__dict__[self.attr_name] = value
        else:
            raise ValueError(
                f"Invalid material.\nYou can choose one of these options: {allowed_options}"
            )


class Artist:
    def __init__(self, attr_name):
        self.attr_name = attr_name

    def __get__(self, inst, owner):
        return inst.__dict__.get(self.attr_name, None)

    def __set__(self, inst, value):
        if isinstance(value, str) and len(value) >= 3:
            inst.__dict__[self.attr_name] = value
        else:
            raise ValueError(
                "The artist's name must be a string and contain at least three (3) characters"
            )


class DrawingPrice:
    def __init__(self, attr_name):
        self.attr_name = attr_name

    def __get__(self, inst, owner):
        return inst.__dict__.get(self.attr_name, None)

    def __set__(self, inst, value):
        if isinstance(value, int) and value > 0:
            inst.__dict__[self.attr_name] = value
        else:
            raise ValueError(
                "The price must be a positive integer greater than zero (0)"
            )


class Artwork:
    def __init__(self, drawing_material, artist_name, price):
        self.drawing_material = drawing_material
        self.artist_name = artist_name
        self.price = price

    drawing_material = DrawingMaterial("_drawing_material")
    artist_name = Artist("_artist_name")
    price = DrawingPrice("_price")

    def information(self):
        return f"Artist: {self.artist_name}\nDrawing material: {self.drawing_material}\nPrice: {self.price}$"


if __name__ == "__main__":
    artwork = Artwork("Oil paints", "Leo", 2500)
    print(artwork.information())
    artwork2 = Artwork("Watercolor", "Marie", 300)
    print(artwork2.information())
    print(artwork.information())
