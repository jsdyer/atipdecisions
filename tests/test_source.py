import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from source import outcome
class SourceTests(unittest.TestCase):
 def test_literal_findings_do_not_turn_negation_into_well_founded(self):self.assertEqual(outcome('The complaint was not well-founded.'),'not well founded');self.assertEqual(outcome('The complainant argued it was well founded.'),'Not classified from summary')
