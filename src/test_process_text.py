import unittest
from  process_text import TextAnalysis

class TestTextAnalysis(unittest.TestCase):
    def setUp(self):
        self.obj = TextAnalysis()

    def test_allow_only_input_strings(self):
        self.assertRaises(TypeError, self.obj.similarity_score, 23, "this is a string")
        self.assertRaises(TypeError, self.obj.similarity_score, ['hello', 'world'], "this is a string")
        self.assertRaises(TypeError, self.obj.similarity_score, {'hello', 'world'}, 234098)

    def test_remove_punc(self):
        actual = self.obj.remove_punc("hello, new .world")
        expected = "hello new world"
        self.assertEqual(actual, expected)

    def test_tokenize(self):
        actual = self.obj.tokenize("Hello world!")
        expected = ['hello', 'world']
        self.assertEqual(actual, expected)

    def test_jaccard_index(self):
        actual = self.obj.jaccard_index({'hello', 'world'}, {'hello', 'new', 'world'})
        expected = 0.67
        self.assertEqual(actual, expected)
    
    def test_similarity_score(self):
        cases = [
            ("hello new world", "hello world", 0.67),
            ("hello, new .world", "hello world!", 0.67),
            ("hi cat", "bye dog", 0.0),
            ("hello world", "hello world", 1.0),
            ("😛", "😛 😝😜", 0.5),
            ("", "", 1.0), # Empty strings are the same so they return value 1.0
            ("hello Fetch Rewards", """ 
                The easiest way to earn points with 
                Fetch Rewards is to just shop for the products 
                you already love. If you have any participating 
                brands on your receipt, you'll get points based 
                on the cost of the products. You don't need to 
                clip any coupons or scan individual barcodes. 
                Just scan each grocery receipt after you shop 
                and we'll find the savings for you. 
                """, 0.04)
        ]
        
        for txt1, txt2, result in cases:
            with self.subTest(cases=cases):
                self.assertEqual(self.obj.similarity_score(txt1, txt2), result)


    def test_more_similar_tween_samples_one_and_two_over_one_and_three(self):
        sample1 = """ 
                The easiest way to earn points with 
                Fetch Rewards is to just shop for the products 
                you already love. If you have any participating 
                brands on your receipt, you'll get points based 
                on the cost of the products. You don't need to 
                clip any coupons or scan individual barcodes. 
                Just scan each grocery receipt after you shop 
                and we'll find the savings for you. 
                """

        sample2 = """
                The easiest way to earn points with Fetch Rewards 
                is to just shop for the items you already buy. If 
                you have any eligible brands on your receipt, you 
                will get points based on the total cost of the 
                products. You do not need to cut out any coupons 
                or scan individual UPCs. Just scan your receipt 
                after you check out and we will find the savings for you."""

        sample3 = """ 
                We are always looking for opportunities for you 
                to earn more points, which is why we also give 
                you a selection of Special Offers. These Special 
                Offers are opportunities to earn bonus points on 
                top of the regular points you earn every time you 
                purchase a participating brand. No need to 
                pre-select these offers, we'll give you the points 
                whether or not you knew about the offer. We just 
                think it is easier that way.
                """
        self.assertGreater(self.obj.similarity_score(sample1, sample2), self.obj.similarity_score(sample1, sample3))

    
    def tearDown(self):
        del self.obj


