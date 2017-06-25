import ctypes


class DynamicArray(object):
    def __init__(self):
        self.numOfElements = 0
        self.capacity = 1
        self.myArrayA = self._make_array(self.capacity)

    def __get_capacity__(self):
        return self.capacity

    def __len__(self):
        return self.numOfElements

    def get_item(self, input_index):
        if not 0 <= input_index < self.numOfElements:
            return IndexError("Input Index is out of Bounds")
        return self.myArrayA[input_index]

    def append_item(self, input_element):
        if self.numOfElements == self.__get_capacity__():
            self._resize(2 * self.capacity)
        self.myArrayA[self.numOfElements] = input_element
        self.numOfElements += 1

    def _resize(self, new_capacity):
        my_array_b = self._make_array(new_capacity)
        for i in range(self.numOfElements):
            my_array_b[i] = self.myArrayA[i]

        self.myArrayA = my_array_b
        self.capacity = new_capacity

    @staticmethod
    def _make_array(input_capacity):
        return (input_capacity * ctypes.py_object)()


myArray = DynamicArray()
print(myArray.__len__())
myArray.append_item(23)
myArray.append_item(3)
myArray.append_item(2323)
myArray.append_item(2323)
myArray.append_item(2323)
myArray.append_item(2323)
print(myArray.__get_capacity__())
print(len(myArray))