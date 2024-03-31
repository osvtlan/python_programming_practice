import unittest
from descriptor import Artwork


class TestDescriptors(unittest.TestCase):
    def test_artwork_information(self):
        artwork = Artwork("Oil paints", "Leo", 2500)
        expected_output = "Artist: Leo\nDrawing material: Oil paints\nPrice: 2500$"
        self.assertEqual(artwork.information(), expected_output)

    def test_valid_artwork(self):
        artwork = Artwork("Oil paints", "Leo", 2500)
        self.assertEqual(artwork.drawing_material, "Oil paints")
        self.assertEqual(artwork.artist_name, "Leo")
        self.assertEqual(artwork.price, 2500)

    def test_valid_material(self):
        artwork = Artwork("Oil paints", "Leo", 2500)
        self.assertEqual(artwork.drawing_material, "Oil paints")

        artwork = Artwork("Watercolor", "Alice", 500)
        self.assertEqual(artwork.drawing_material, "Watercolor")

        artwork = Artwork("Graphic", "Bob", 1000)
        self.assertEqual(artwork.drawing_material, "Graphic")

    def test_valid_name_length(self):
        artwork = Artwork("Oil paints", "Leo", 2500)
        self.assertEqual(artwork.artist_name, "Leo")

        artwork = Artwork("Oil paints", "Alice", 500)
        self.assertEqual(artwork.artist_name, "Alice")

        artwork = Artwork("Oil paints", "Bob", 1000)
        self.assertEqual(artwork.artist_name, "Bob")

    def test_valid_price(self):
        artwork = Artwork("Oil paints", "Leo", 1)
        self.assertEqual(artwork.price, 1)

        artwork = Artwork("Oil paints", "Alice", 500)
        self.assertEqual(artwork.price, 500)

        artwork = Artwork("Oil paints", "Bob", 1000)
        self.assertEqual(artwork.price, 1000)

    def test_invalid_material(self):
        with self.assertRaises(ValueError) as context:
            Artwork("Invalid material", "Leo", 2500)
        self.assertEqual(
            str(context.exception),
            "Invalid material.\nYou can choose one of these options: ['Oil paints', 'Watercolor', 'Graphic']",
        )

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as context:
            Artwork("Oil paints", "A", 2500)
        self.assertEqual(
            str(context.exception),
            "The artist's name must be a string and contain at least three (3) characters",
        )

        with self.assertRaises(ValueError) as context:
            Artwork("Oil paints", 45, 2500)
        self.assertEqual(
            str(context.exception),
            "The artist's name must be a string and contain at least three (3) characters",
        )

    def test_invalid_price(self):
        with self.assertRaises(ValueError) as context:
            Artwork("Oil paints", "Leo", -2500)
        self.assertEqual(
            str(context.exception),
            "The price must be a positive integer greater than zero (0)",
        )

        with self.assertRaises(ValueError) as context:
            Artwork("Oil paints", "Leo", 0)
        self.assertEqual(
            str(context.exception),
            "The price must be a positive integer greater than zero (0)",
        )

        with self.assertRaises(ValueError) as context:
            Artwork("Oil paints", "Leo", 0.1)
        self.assertEqual(
            str(context.exception),
            "The price must be a positive integer greater than zero (0)",
        )

    def test_several_instances_initial_data(self):
        artwork1 = Artwork("Oil paints", "Leo", 2500)
        artwork2 = Artwork("Watercolor", "Marie", 300)

        self.assertEqual(
            artwork1.information(),
            "Artist: Leo\nDrawing material: Oil paints\nPrice: 2500$",
        )
        self.assertEqual(
            artwork2.information(),
            "Artist: Marie\nDrawing material: Watercolor\nPrice: 300$",
        )

    def test_change_material_valid(self):
        artwork = Artwork("Oil paints", "Leo", 2500)
        artwork.drawing_material = "Watercolor"
        self.assertEqual(
            artwork.information(),
            "Artist: Leo\nDrawing material: Watercolor\nPrice: 2500$",
        )

    def test_change_material_invalid(self):
        artwork = Artwork("Oil paints", "Leo", 2500)
        with self.assertRaises(ValueError):
            artwork.drawing_material = "Acrylic"
        self.assertEqual(
            artwork.information(),
            "Artist: Leo\nDrawing material: Oil paints\nPrice: 2500$",
        )

    def test_change_artist_name_valid(self):
        artwork = Artwork("Oil paints", "Leo", 2500)
        artwork.artist_name = "Marie"
        self.assertEqual(
            artwork.information(),
            "Artist: Marie\nDrawing material: Oil paints\nPrice: 2500$",
        )

    def test_change_artist_name_invalid(self):
        artwork = Artwork("Oil paints", "Leo", 2500)
        with self.assertRaises(ValueError):
            artwork.artist_name = "A."
        self.assertEqual(
            artwork.information(),
            "Artist: Leo\nDrawing material: Oil paints\nPrice: 2500$",
        )

    def test_change_price_valid(self):
        artwork = Artwork("Oil paints", "Leo", 2500)
        artwork.price = 3000
        self.assertEqual(
            artwork.information(),
            "Artist: Leo\nDrawing material: Oil paints\nPrice: 3000$",
        )

    def test_change_price_invalid(self):
        artwork = Artwork("Oil paints", "Leo", 2500)
        with self.assertRaises(ValueError):
            artwork.price = -3000
        self.assertEqual(
            artwork.information(),
            "Artist: Leo\nDrawing material: Oil paints\nPrice: 2500$",
        )


if __name__ == "__main__":
    unittest.main()
