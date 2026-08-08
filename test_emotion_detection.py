import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestSentimentAnalyzer(unittest.TestCase):
    def test_joy_dominant_emotion(self):
        emotions = emotion_detector('I am glad this happened')
        self.assertEqual(emotions['dominant_emotion'], 'joy')
    
    def test_anger_dominant_emotion(self):
        emotions = emotion_detector('I am really mad about this')
        self.assertEqual(emotions['dominant_emotion'], 'anger')

    def test_disgust_dominant_emotion(self):
        emotions = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(emotions['dominant_emotion'], 'disgust')
    
    def test_sadness_dominant_emotion(self):
        emotions = emotion_detector('I am so sad about this')
        self.assertEqual(emotions['dominant_emotion'], 'sadness')

    def test_fear_dominant_emotion(self):
        emotions = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(emotions['dominant_emotion'], 'fear')

if __name__ == "__main__":
    unittest.main()
