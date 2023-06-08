from veriler import veriler 
import json

for i in range(0, 5):
    yeni_veri = {
        "id": f"id{i}",
        "saat": f"saat{i}",
        "link": f"resim{i}"
    }
    veriler[str(i)] = yeni_veri
