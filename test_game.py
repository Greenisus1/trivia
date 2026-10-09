import unittest,random,collections
import game
modules={'trivia':game}
class Tests(unittest.TestCase):
 def test_trivia_options(self):
  qs=modules['trivia'].questions();self.assertEqual(set(q[0] for q in qs),set(range(5)))
  for _,q,opts,answer,_ in qs:self.assertEqual(len(set(opts)),4,q);self.assertIn(answer,range(4))
 def test_trivia_python(self):
  for topic,q,opts,a,_ in modules['trivia'].questions():
   if topic==2:self.assertEqual(str(eval(q[8:-4])),opts[a])
if __name__=="__main__":unittest.main()
