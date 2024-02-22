from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

def can_attend_meetings(self, intervals: List[Interval]) -> bool:
  # Write your code here
  # Seperate the starts and ends to resperctive arrays
  starts = sorted([interval.start for interval in intervals])
  ends = sorted([interval.end for interval in intervals])

  # if starts[i+1] < ends[i] then return false
  for i in range(len(starts) - 1):
      if starts[i+1] < ends[i] : return False
  return True
