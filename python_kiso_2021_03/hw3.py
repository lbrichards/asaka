import unittest

'''
    """
    今回の宿題は多分正解がインターネットに載っている可能性があります。
    勉強のため、なるべくインターネット検索をせずにご自分で、
    あるいは生徒同士で相談してプログラムを書きましょう！
    """




宿題その１

【フィボナッチ数列】とは、最初の二項が1で、第三項以降の項が
すべて直前の二項の和になっている数列。

では、j項までのフィボナッチ数列を出力とする
fib(j)という関数を書いてください。正しければ、下記のtest_problem_1()
が成功します。
'''


def fib(j):
    output = [1, 1]
    for i in range(j-2):
        output.append(output[-2] + output[-1])
    return output






'''
宿題その２

フィボナッチ数列の項数が多くなるに連れて、n＋１番の項をn番の項で割った値が
「黄金比」呼ばれる値に収束します。

この黄金比を求めるため

golden_ratio(n)

という関数を書いてください。上記のfib(j)を利用しても良い。

ヒント：リストの内包表現を利用すると一行で書くことが可能です
'''


def gold_ratio(n):
    f = fib(n)
    return f[-1]/f[-2]




class LessonThreeHomeworkTest(unittest.TestCase):

    def test_problem_1(self):
        self.assertEqual(fib(2), [1,1])
        self.assertEqual(fib(10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_problem_2(self):
        phi = (1 + 5**0.5) / 2 #　<--これも黄金比
        self.assertEqual(gold_ratio(4), 1.5)
        self.assertEqual(gold_ratio(10), 1.6176470588235294)
        self.assertEqual(gold_ratio(100), phi)

