# =====================================================================================================================
# Heap
# =====================================================================================================================
# Heap is a complete binary tree ( Max. possible ht. is log(n) )
# - Cannot be used for searching ele
# - used only for 1. inserting 2. Deleting (that too only max/min)

import os, time

class Heap:
    """
    KEY: Indices start from 1 not 0.
        + parent_idx        = child_idx//2
        + left_child_idx    = parent_idx*2
        + right_child_idx   = parent_idx*2 + 1 


    DATA MEMBERS
        + _list                     : internal list representation of heap
        + __internal_list_size      : actual size of internal list
        + _size                     : size of heap

    METHODS
        + insert_from(lst)          : calls `__siftUp` on every ele of lst left to right
                                        - makes room if load increases using __make_room()
                                        -  O(nlogn)
                                        - `__heapify` [ O(n) ammortized] is better than `__sift_up`

    HELPER METHODS
        + __get_cur                 : returns to the last position idx (>=1 cz inices start from 1) in _list of heap
        + __append                  : appends to last empty pos of _list making sure indices start from 1
        + __make_room(max_ratio)    : if `_list` is full more than `max_ratio` increases size
        + __sift_up                 : 
        + __hepify                  : 
    """

    def __init__(self, contents=[], initial_size=10):
        # Note: idxs start from 1 not 0
        self._list  = [None]*initial_size 
        self._size  = 0

        self.__internal_list_size = initial_size

        # build heap
        self.insert_from(contents)
    
    # ----------------------------------------------------------
    # Insertion
    # ----------------------------------------------------------
    def __get_cur(self):
        return  self._size + 1

    def __append(self, e):
        """
        makes sure indices start from 0

        Note: does not append to `Heap`. Appends to `_list`
        """
        self._list[self.__get_cur()] = e
        self._size += 1
        # no need to increment self.cur by 1 because,
        # it is dependant on size. (_size + 1)

    def __make_room(self, max_ratio=0.75, factor=2):
        # No need to make room at beginig of internal list 
        # as it will never be empty.
        cur_ratio = self._size / self.__internal_list_size
        if cur_ratio > max_ratio:
            new_list = [None] * (factor * self.__internal_list_size)
            for idx, e in enumerate(self._list):
                new_list[idx] = e
            # update:
            # self._size remains same
            self._list = new_list 
            self.__internal_list_size = factor * self.__internal_list_size

    def __siftUp(self, e):
        """
        TIME:   O(logn)
        """

        # simply append e to the end of internal list
        self.__append(e)
        
        # sift up appended `e` from it's cur pos `self._size` to rightful positon
        # by succesively bringing down smaller parents until bigger parent is reached
        cur_idx = self._size
        par_idx = self._size // 2
        par_ele = self._list[par_idx]

        while (par_idx >= 1) and (e > par_ele):
            
            # bring parent **down** to it's child posn. if (cur_ele > par_ele)
            # note: but not swapping i.e bringing cur_ele to top 
            # (will be done in end of while loop)
            self._list[cur_idx] = par_ele

            # update:
            # cur_idx -> it's parent
            # par_idx -> it's parent
            cur_idx = cur_idx // 2
            par_idx = par_idx // 2
            par_ele = self._list[par_idx]
        
        # as `cur_idx`  will be updated to it's parent idx which is
        # the rightful place
        self._list[cur_idx] = e

    def insert_from(self, a_sequence, method="siftup"):
        """
        heapify is more efficient       --> O(n) ammortized
        Here, we are using __siftUp     --> O(nlogn)

        TIME        : O(nlogn)
        """
        # Note: idxs start from 1 not 0
        for e in a_sequence:

                # initial condition (executed only once)
                # directly add root as there won't be anything to compare
                if self._size == 0:
                    self.__append(e)
                    continue

                # makeroom if load > 0.75 ratio
                self.__make_room(0.75)

                # add element to heap using heapify/siftup
                if   method == "siftup"  : self.__siftUp(e)
                elif method == "heapify" : self.__heapify(e)

                

if __name__ == '__main__':
    
    lst = [11,77,33,66,99,33,66,44,-44,-22,-33]
    h = Heap(lst)
    
    # internal list retaining conceptual max-top tree
    print(h._list)