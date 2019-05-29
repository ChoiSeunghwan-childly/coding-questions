import unittest

def reverseString(_str):
    return _str[::-1]

def reverseString2(_str):
    stack = []

    for ch in _str:
        stack.append()

    result = ""
    while len(stack) > 0:
        result += stack.pop()
    
    return result

def anagram(_input1, _input2):
    if len(_input1) != len(_input2):
        return False

    for i in range(len(_input1)):
        if _input1[i] not in _input2:
            return False

    return True

class CustomTests(unittest.TestCase):
    
    # def test_case1(self):
    #     _input = "abced"
    #     self.assertEqual("decbb", reverseString(_input))

    # def test_case2(self):
    #     _input1 = "hoho"
    #     _input2 = "hoho"
    #     self.assertTrue(anagram(_input1, _input2))

    def test_create_file(self):
        with open("./test.txt", mode="w+") as f:
            for i in range(10):
                f.write("hello" + str(i) +"\n")

    def test_read_file(self):
        with open("./test.txt", mode="r") as f:
            for line in f.readlines():
                print(line, end='')
            

if __name__ == '__main__':
    unittest.main()