

class Text(str):
    def duplicate(self):
        return self+self


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list0 = TrackableList()
list0.append("1")

text = Text("Python")
print(text.duplicate())
list1 = list("python")
list1.append("aaaa")
print(list1)
