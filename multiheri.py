class A:
    def t(self):
        print("Test1")
class B:
    def t1(self):
        print("Test2")
class C(A,B):
    def t2(self):
        print("Test3")
obj=C()
obj.t2()
obj.t()
obj.t1()
print(issubclass(C,B))
print(issubclass(A,B))