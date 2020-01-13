import unittest
# target = __import__("converter.py")
# combine = target.combine_ips
from converter import combine_ips
from converter import convert_line

class TestCombine(unittest.TestCase):
  def test_any(self):
    line = 'any,0'
    self.assertEqual(convert_line(line), 'any;0')
    line = '1.0.0.255/any'
    self.assertEqual(convert_line(line), line)
  def test_sample(self):
    ips = ['10.10.10.0/24','10.10.11.0/24','10.10.12.0/24']
    self.assertEqual(combine_ips(ips), '10.10.10.0/23;10.10.12.0/24')
  def test_mask(self):
    line = '1.2.3.4/255.255.0.0'
    self.assertEqual(convert_line(line), '1.2.3.4/255.255.0.0')
  def test_text(self):
    name = 'mr.samuel.l.jackson'
    text = 'sometexthere'
    self.assertEqual(convert_line(name), name)
    self.assertEqual(convert_line(text), text)
  def test_invalid_number(self):
    numbers = '42,2.4'
    self.assertEqual(convert_line(numbers), ';'.join(numbers.split(',')))
if __name__ == '__main__':
  unittest.main()
