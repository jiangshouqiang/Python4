import pickle
d = dict(name="bob",age=20,score=99)
fh = open("pick.txt","wb")
pickle.dump(d,fh)
fh.close()

f = open("pick.txt","rb")
d = pickle.load(f)
f.close()
print(d)
