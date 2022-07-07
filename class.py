class py_sample:
    def sub_sets(self,sset):
        return self.sub_setsRecur([],sorted(sset))
    def subsetRecur(self,current,sset):
        if sset:
            return self.subsetRecur(current,sset[1:])+self.subsetRecur(current+sset[0],sset[1:])
        return [current]
for name in py_sample.__dict__:
        print(name)