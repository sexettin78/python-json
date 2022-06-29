import json

ornek = {"bilgiler":[{"Ad":"Furkan","Soyad":"D"},{"Ad":"Sexettin","Soyad":"A"}]}
ornekload = '{"bilgiler":[{"Ad":"Furkan","Soyad":"D"},{"Ad":"Sexettin","Soyad":"A"}]}'

#json.dump(ornek) #bu fonksiyon ile json verileri oluşturabiliriz. ancak bu fonksiyon json çıktısını bir dosyaya yazdırır

json.dumps(ornek) #bu fonksiyon ile oluşturacağımız verileri ekran çıktısı olarak alabiliriz

json.dumps(ornek, ensure_ascii= False) #ensure_ascii false yaparak türkçe karakterlerde sıkıntı oluşmasını önleriz

#json.load(ornekload) #json verileri dosyadan okunur. değer döndürmez

json.loads(ornekload) #verileri parametre olarak atar

cevir_json = json.loads(ornekload)

"~~~~JSON VERİLERİNİ AYRIŞTIRMAK~~~~"
print(cevir_json['bilgiler']) #--> yazarsak önümüze bilgiler katmanındaki veriler gelir
print(cevir_json['bilgiler'] [0]) #--> yazarsak önümüze ilk çekirdeğin verileri gelir
#print(cevir_json['bilgiler'] ["Ad"]) #--> yazarsak önümüze Ad çekirdeklerinin verileri gelir
print(str(cevir_json['bilgiler'] [0] ["Ad"])) #--> yazarsak önümüze ilk çekirdekteki Ad çekirdeğinin verileri gelir


"""
JSON ------ PYTHON (JSON ifadelerinin python karşılıkları)
object      dict
array       list, tuple(sadece okunabilir liste)
String      str
Number      int, float
true        True
false       False
none        None
"""