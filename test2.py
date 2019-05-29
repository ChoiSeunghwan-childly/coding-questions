import unittest

class MyTestCase(unittest.TestCase):
    
    def test_cal(self):
        f = open("./mytest.txt", "w+")
        for i in range(10):
            f.write(str(i) + "\n")
        f.seek(0)
        
        sum = 0
        arr = []
        for line in f.readlines():
            sum += int(line.strip())
            arr.append(line.strip())
            print(line, end='')

        print(sum, end='\n')
        print(arr )
        f.close()

if __name__ == '__main__':
    unittest.main()
        