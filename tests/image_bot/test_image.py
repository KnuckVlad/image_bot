import unittest

from application.image_preprocessing.image import Image

from tests.settings import IMAGES_PATH

PROPERTIES=['width', 'height', 'format', 'colors_count', 'mono']

class ImageTests(unittest.TestCase):

    def test_params_exist(self):
        # TODO : use mock images
        image_path = ''.join([IMAGES_PATH, 'mono.png'])
        image = Image(image_path)
        self.assertEqual(all(key in image.get_params() for key in PROPERTIES), True)

    def test_image_is_mono(self):
        # TODO : use mock images
        image_path = ''.join([IMAGES_PATH, 'mono.png'])
        image = Image(image_path)
        self.assertEqual(image.get_params()['mono'], True)

    def test_image_is_not_mono(self):
        # TODO : use mock images
        image_path = ''.join([IMAGES_PATH, 'test.jpg'])
        image = Image(image_path)
        self.assertEqual(image.get_params()['mono'], False)


if __name__ == "__main__":
    unittest.main()
