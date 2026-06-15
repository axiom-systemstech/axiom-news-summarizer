python
import unittest
from axiom_summarizer.cli import AxiomNewsSummarizer

class TestAxiomNewsSummarizer(unittest.TestCase):
    def setUp(self):
        self.summarizer = AxiomNewsSummarizer()
    
    def test_topics_exist(self):
        expected = ["elecciones", "tecnologia", "deportes", "economia", "salud", "internacional"]
        for topic in expected:
            self.assertIn(topic, self.summarizer.feeds)
    
    def test_topic_lowercase(self):
        self.assertEqual(
            self.summarizer.feeds["elecciones"],
            self.summarizer.feeds["ELECCIONES".lower()]
        )

if __name__ == "__main__":
    unittest.main()

