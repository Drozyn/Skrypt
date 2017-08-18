# Skrypt
# -*-coding:utf-8 -*-

import urllib2
while True:
    adres = raw_input('Podaj url: ')
    if not adres:
        print "Help?"
    else:
        con = urllib2.urlopen(adres)
        dane = con.read()
        str = 'size'
        str2 = '}'
        index = dane.find(str)
        index2 = dane.find(str2)
        if index2 - index == 9:
            rozmiar = int(dane[index + 7])
        if index2-index == 10:
            rozmiar =int(dane[index+7])*10 + int(dane[index+8])


        if rozmiar < 2:
            print "CRITICAL"
        elif rozmiar >= 2 and rozmiar<4:
            print "WARNING"
        else:
            print "OK"
        break
raw_input("Press Enter")
