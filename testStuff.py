#!/bin/dev/env python


def testPoppin(arr1):
  arr1.pop(0)

arr1 = [1, 2, 3, 4, 5]

while len(arr1) > 0:
  testPoppin(arr1)
  print(arr1)
