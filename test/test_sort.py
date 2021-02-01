import pysort
import unittest
from pysort import bubble_sort, bucket_sort, cocktail_sort, counting_sort, heap_sort,\
  insertion_sort, merge_sort, quick_sort, radix_sort, selection_sort, shell_sort


data_list = [2, 8, 7, 1, 3, 5, 6, 4]


class TestSort(unittest.TestCase):
    def test_bubble_sort(self):
        sort_list = bubble_sort.sort(data_list)
        self.assertIs(type(sort_list), list)

    def test_bucket_sort(self):
        sort_list = bucket_sort.sort(data_list)
        self.assertIs(type(sort_list), list)

    def test_cocktail_sort(self):
        sort_list = cocktail_sort.sort(data_list)
        self.assertIs(type(sort_list), list)

    def test_counting_sort(self):
        sort_list = counting_sort.sort(data_list)
        self.assertIs(type(sort_list), list)

    def test_heap_sort(self):
        sort_list = heap_sort.sort(data_list)
        self.assertIs(type(sort_list), list)

    def test_insertion_sort(self):
        sort_list = insertion_sort.sort(data_list)
        self.assertIs(type(sort_list), list)

    def test_merge_sort(self):
        sort_list = merge_sort.sort(data_list)
        self.assertIs(type(sort_list), list)

    def test_quick_sort(self):
        sort_list = quick_sort.sort(data_list)
        self.assertIs(type(sort_list), list)

    def test_radix_sort(self):
        sort_list = radix_sort.sort(data_list)
        self.assertIs(type(sort_list), list)

    def test_selection_sort(self):
        sort_list = selection_sort.sort(data_list)
        self.assertIs(type(sort_list), list)

    def test_shell_sort(self):
        sort_list = shell_sort.sort(data_list)
        self.assertIs(type(sort_list), list)


if __name__ == '__main__':
    unittest.main()


