import unittest

import pytest

import Notenberechnung as NB


class Notenberechnung_Tests(unittest.TestCase):
    def test_calculate_grade__given_negative_points_returns_value_error(self):
        # arrange
        invalid_points = -1
        max_possible_points = 100

        # act
        with pytest.raises(ValueError):
            NB.calculate_grade(invalid_points, max_possible_points)

    def test_calculate_grade__given_points_above_max_returns_value_error(self):
        # arrange
        invalid_points = 101
        max_possible_points = 100

        # act
        with pytest.raises(ValueError):
            NB.calculate_grade(invalid_points, max_possible_points)

    def test_calculate_grade__given_valid_number_returns_percentage_grade(self):
        # arrange
        valid_points = 77
        max_possible_points = 100

        # act
        result = NB.calculate_grade(valid_points, max_possible_points)

        # assert
        self.assertEqual(result, 77)

    def test_calculate_grade__given_number_above_maximum_points_returns_value_error(self):
        # arrange
        valid_points = 54
        invalid_max_possible_points = -123

        # act
        with pytest.raises(ValueError):
            NB.calculate_grade(valid_points, invalid_max_possible_points)


    def test_calculate_grade__given_two_invalid_numbers_returns_value_error(self):
        # arrange
        invalid_points = -255
        invalid_max_points = -255

        # act
        with pytest.raises(ValueError):
            NB.calculate_grade(invalid_points, invalid_max_points)


    def test_get_grade_as_text__given_upper_edge_percent_returns_grade_1_text(self):
        # arrange
        percent = 100
        expected = "sehr gut"

        # act
        grade_as_text = NB.get_grade_as_text(percent)

        # assert
        self.assertEqual(grade_as_text, expected)

    def test_calculate_grade__given_lower_edge_percent_returns_grade_1_text(self):
        # arrange
        percent = 92
        expected = "sehr gut"

        # act
        grade_as_text = NB.get_grade_as_text(percent)

        # assert
        self.assertEqual(grade_as_text, expected)

    def test_get_grade_as_text__given_upper_edge_percent_returns_grade_2_text(self):
        # arrange
        percent = 91
        expected = "gut"

        # act
        grade_as_text = NB.get_grade_as_text(percent)

        # assert
        self.assertEqual(grade_as_text, expected)

    def test_calculate_grade__given_lower_edge_percent_returns_grade_2_text(self):
        # arrange
        percent = 81
        expected = "gut"

        # act
        grade_as_text = NB.get_grade_as_text(percent)

        # assert
        self.assertEqual(grade_as_text, expected)

    def test_get_grade_as_text__given_upper_edge_percent_returns_grade_3_text(self):
        # arrange
        percent = 80
        expected = "befriedigend"

        # act
        grade_as_text = NB.get_grade_as_text(percent)

        # assert
        self.assertEqual(grade_as_text, expected)

    def test_get_grade_as_text__given_lower_edge_percent_returns_grade_3_text(self):
        # arrange
        percent = 67
        expected = "befriedigend"

        # act
        grade_as_text = NB.get_grade_as_text(percent)

        # assert
        self.assertEqual(grade_as_text, expected)

    def test_get_grade_as_text__given_upper_edge_percent_returns_grade_4_text(self):
        # arrange
        percent = 66
        expected = "ausreichend"

        # act
        grade_as_text = NB.get_grade_as_text(percent)

        # assert
        self.assertEqual(grade_as_text, expected)

    def test_get_grade_as_text__given_lower_edge_percent_returns_grade_4_text(self):
        # arrange
        percent = 50
        expected = "ausreichend"

        # act
        grade_as_text = NB.get_grade_as_text(percent)

        # assert
        self.assertEqual(grade_as_text, expected)

    def test_get_grade_as_text__given_upper_edge_percent_returns_grade_5_text(self):
        # arrange
        percent = 49
        expected = "mangelhaft"

        # act
        grade_as_text = NB.get_grade_as_text(percent)

        # assert
        self.assertEqual(grade_as_text, expected)

    def test_get_grade_as_text__given_lower_edge_percent_returns_grade_5_text(self):
        # arrange
        percent = 30
        expected = "mangelhaft"

        # act
        grade_as_text = NB.get_grade_as_text(percent)

        # assert
        self.assertEqual(grade_as_text, expected)

    def test_get_grade_as_text__given_upper_edge_percent_returns_grade_6_text(self):
        # arrange
        percent = 29
        expected = "ungenügend"

        # act
        grade_as_text = NB.get_grade_as_text(percent)

        # assert
        self.assertEqual(grade_as_text, expected)

    def test_get_grade_as_text__given_lower_edge_percent_returns_grade_6_text(self):
        # arrange
        percent = 0
        expected = "ungenügend"

        # act
        grade_as_text = NB.get_grade_as_text(percent)

        # assert
        self.assertEqual(grade_as_text, expected)

    def test_calculate_grade__given_text_returns_type_error(self):
        # arrange
        invalid_points = "10"
        max_possible_points = 100

        # act
        with pytest.raises(TypeError):
            NB.calculate_grade(invalid_points, max_possible_points)

    def test_calculate_grade__given_text_2_returns_type_error(self):
        # arrange
        invalid_points = 10
        max_possible_points = "100"

        # act
        with pytest.raises(TypeError):
            NB.calculate_grade(invalid_points, max_possible_points)

    def test_get_grade_as_text__given_text_returns_type_error(self):
        # arrange
        percent = "10"

        # act
        with pytest.raises(TypeError):
            NB.get_grade_as_text(percent)

    def test_get_grade_as_text__given_negative_value_return_value_error(self):
        # arrange
        percent = -1

        # act
        with pytest.raises(ValueError):
            NB.get_grade_as_text(percent)


if __name__ == '__main__':
    unittest.main()


# coverage run --branch .\2409\TestCases.py; coverage report
