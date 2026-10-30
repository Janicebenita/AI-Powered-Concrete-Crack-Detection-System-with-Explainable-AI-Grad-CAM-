import unittest
from agent import review_detection


class CrackReviewTests(unittest.TestCase):
    def test_probability_and_box_are_retained_as_evidence(self):
        result = review_detection({"crack_probability": 0.8, "bounding_boxes": [[1, 2, 3, 4]], "gradcam_overlap": 0.7})
        self.assertEqual(result["status"], "crack-evidence")
        self.assertEqual(result["evidence"]["bounding_boxes"], [[1, 2, 3, 4]])


if __name__ == "__main__":
    unittest.main()
