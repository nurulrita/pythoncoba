my_list=[]
my_hobby=['eating', 'sleeping', 'fangirling', 'nothing to do', 'stalking']
print my_list
print my_hobby[1], my_hobby[4]
print "My third hobby is {}".format(my_hobby[2])
print "My main hobby is {1} and my second hobby is {0}".format(my_hobby[4],"watching")
print "I have {} hobbies".format(len(my_hobby))

#ini untuk melampirkan hobby
for hobby in my_hobby:
    print hobby
#untuk menambah hobby di akhir
my_hobby.append('watching')
print my_hobby

hobby_a=raw_input('input hobby anda:')
my_hobby.append(hobby_a)
print my_hobby

#menambah hobby sesuai indeks yang diinginkan
my_hobby.insert(0,'breathing')
print my_hobby

#memberi tahu urutan
print my_hobby.index('nothing to do')

#menghapus dengan elemen
rem=raw_input("masukkan hobby yang ingin dihapus:")
my_hobby.remove(rem)
print my_hobby

#menghapus dengan index
my_hobby.pop(0)
print my_hobby

#mensorting
my_hobby.sort()
print my_hobby

#menreverse
my_hobby.reverse()
print my_hobby
