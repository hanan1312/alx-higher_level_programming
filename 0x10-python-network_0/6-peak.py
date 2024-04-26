#!/usr/bin/python3
""" function that finds a peak in a list of unsorted integers. """

def find_peak(list_of_integers):
  """
  Finds a peak element in an unsorted list of integers.

  Args:
      list_of_integers: A list of integers.

  Returns:
      The index of a peak element in the list, or None if no peak is found.

  Time complexity: O(log n)
  """
  if len(list_of_integers) == 0:
    return None

  left = 0
  right = len(list_of_integers) - 1

  while left < right:
    mid = left + (right - left) // 2

    # Check if mid is a peak (both neighbors are smaller)
    if (mid == 0 or list_of_integers[mid] > list_of_integers[mid - 1]) and \
        (mid == len(list_of_integers) - 1 or list_of_integers[mid] > list_of_integers[mid + 1]):
      return mid

    # If left half is greater, search for peak there
    if list_of_integers[mid] < list_of_integers[left]:
      right = mid - 1
    else:
      left = mid + 1

  # If entire loop completes, no peak is found
  return None

