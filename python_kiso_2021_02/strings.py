import unittest
import doctest

class LessonTwoTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_quotation_marks1(self):
        '''
        文字列にアポストロフィ（'）も入れることができます。
        '''

        #　バックスラッシュを使う場合
        # "\"は一般的に「エスケープ・キャラクター」とも呼ばれます。
        print('doesn\'t')

        # ダブルクォーテーション・マークを使う場合
        print("doesn't")

        self.assertEqual('doesn\'t', "doesn't")

        # ダブルクォーテーション・マークを含めるときは、シングルクォーテーション・マークに
        # 間に挟まれていればよい

        s1= '"Yes," they said.'
        # あるいは、バックスラッシュを使ってもよい。
        s2 = "\"Yes,\" they said."

        self.assertEqual(s1,s2)

    def test_quotation_marks2(self):
        """
        パイソン・コンソールでは、入力した文字列はおうむ返しされます。
        出力のフォーマットは入力した通りではないのでご注意ください。

        出力においては
        ・特殊文字（タブ、改行、）はバックスラッシュでescapeされます
        ・文字列はシングルクォーテーション・マークに挟まれます

        print()関数を使えば、人間のより読みやすいようにフォーマットされます。

        例えば、print()関数を使うと"\n"が改行に置き換わります。
        """

        '''
        特殊文字を置き換えせずに、そのまま出力したい場合は、最初の
        クォーテーション・マークの前に"r"をつけます。
        '''

        s1 = r'C:\name'
        s2 = 'C:\name'

        print(s1)
        print(s2) # \nは改行と言う意味になります。

        # "console_examples.txt"というファイルにご参照ください。
        doctest.testfile("console_examples.txt")

    def test_concat1(self):
        s1 = 'Py'
        s2 = 'thon'
        self.assertEqual(s1+s2, 'Python') #　足し算オペレーター

    def test_concat2(self):
        s1 = "Py" "thon"  #　同じ行であれば、オペレーターなしでも連結されます
        self.assertEqual(s1, 'Python')

    def test_concat3(self):
        s1 = ("Py" "thon" # 真ん中の空白は無視されます
              " is" # 文字の前後の空白は無視されません。
              " great"
              )
              #　複数行に渡る連結は(...)に囲めばよい
        self.assertEqual(s1, 'Python is great')

    def test_multiline(self):
        s1 = """once upon a time..."""

        s2 = """once upon 
        a time..."""  # トリプル・クォーテーション・マーク間の改行は、改行記号として文字列に含まれる

        # 改行記号を含めたくない場合はバックスラッシュを右側に追加すれば良い
        s3 = ("""\
once upon \
a time...\
""")

    #注意：バックスラッシュの右側に空白が入るとこの機能は無効となります。

        self.assertNotEqual(s1, s2)
        self.assertEqual(s1, s3)

    def test_add_multiply(self):

        s1 = 'hello' * 2 + ' world'
        s2 = 'hellohello world'

        self.assertEqual(s1,s2)

    def test_slicing_indexing(self):

        # "console_examples2.txt"というファイルにご参照ください。
        doctest.testfile("console_examples2.txt")


if __name__ == '__main__':
    unittest.main()