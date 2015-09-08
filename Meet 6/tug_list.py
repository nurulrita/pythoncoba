makanan = ['nasi', 'ayam', 'kentang']
print makanan
mkn = raw_input('Tambahkan makanan :')
makanan.append(mkn)
print makanan
print
mkn2 = raw_input('Input makanan lagi :')
indx = input('indeks:')
makanan.insert(indx,mkn2)
print makanan
mkn3 = raw_input('input makanan untuk mengetahui indeks:')
print makanan.index(mkn3)
print 
print makanan
rmv = raw_input('masukkan makanan yang ingin dihapus:')
makanan.remove(rmv)
print makanan
print
'''rename_=raw_input('masukkan nama makanan yang ingin diganti:')
nwmkn = raw_input('masukkan nama baru untuk {}:'.format(rename_))
makanan.remove(rename_)
makanan.insert(indx,nwmkn)
print makanan
print'''
rename_=raw_input('masukkan nama makanan yang ingin diganti:')
new = makanan.index(rename_)
print "letak indeks nama yang akan diganti {}".format(makanan.index(rename_))
makanan[new] = raw_input('masukkan nama baru untuk {}:'.format(rename_))
print makanan
