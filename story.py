print "Di sebuah taman, terdapat peta harta karun. Karena tertarik, anda mulai mengikuti jalur tersebut. Setelah mengikutinya, terdapat 2 cabang. Cabang mana yang anda pilih? cabang 1 atau cabang 2?"
var=input(">")
print var
if var == 1:
    print "Selamat datang di cabang satu, saat ini anda harus memilih jalur kembali. Jalur mana yang anda pilih? 1/2/3"
    angka=input(">") 
    print angka
    if angka == 1:
       print "Ups, Jebakan!"
    elif angka == 2:
       print "Selamat, harta karun ini milik anda"
    else:
       print "Kasian deh, salah jalan hahaha"
elif var == 2:
   print "Selamat datang di cabang dua, saat ini anda harus memilih jalur kembali. Jalur mana yang anda pilih? 1/2"
   angka_2=input(">")
   print angka_2
   if angka_2 == 1:
      print "Jeng jeng jeng jeng, anda nyasar!"
   elif angka_2 == 2:
      print "Hm, mending balik lagi deh"
   else:
      print "Woy jangan ngaco"
print "end"
    
