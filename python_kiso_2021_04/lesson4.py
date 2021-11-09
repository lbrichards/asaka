import unittest

class LessonFourTests(unittest.TestCase):

    def setUp(self):
        ...


    def test_problem_3_1(self):
        """
        numbers （リスト）の中から条件を満たすもののみを出力しましょう。

        条件１：５で割り切れる
        条件２：１５０より大きい場合は飛ばして次へ行く
        条件３：５００より大きい場合、プログラムを止める
        """
        numbers = [12,75,150,180,145,525]
        output = []
        for number in numbers:
            if number > 500:
                break
            elif number > 150:
                continue
            elif number % 5 ==0:
                output.append(number)
        self.assertEqual(output, [75, 150, 145])

    def test_problem_3_2(self):
        """
        while loopを用いて、数字の桁数を数えましょう。
        試験用の数字入力は735802とします。
        """
        number = 735802
        counter = 0
        while number:
            number = number // 10
            counter +=1
        self.assertEqual(counter, 6)

    def test_problem_3_3(self):
        """
        上記と同じ条件ですが、リストを利用しましょう。
        """
        number = 735802
        counter = 0
        digits = list(str(number))
        """
        whileを使うという条件がなければlen(digits)でもよかった。
        """
        while digits:
            digits.pop()
            counter +=1
        self.assertEqual(counter, 6)

    def test_problem_3_4(self):
        n = 5
        for i in range(n, 0, -1):
            for j in range(i, 0, -1):
                print(j, end='')
            print()

    def test_problem_3_5(self):
        mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        result = []
        for i in range(len(mylist)):
            if i%2:
                result.append(mylist[i])

        self.assertEqual(result, [20,40,60,80,100])



if __name__ == '__main__':
    unittest.main()