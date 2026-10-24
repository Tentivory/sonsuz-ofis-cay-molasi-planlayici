#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Ofis Çay Molası Planlayıcı
Dünyanın en bilimsel, en resmi ve en gereksiz çay molası planlama sistemi.
Kayyum onaylıdır. (gizli not: bürokrasi her şeyi yutar)
"""

import time
import random
import sys

def resmi_mesajlar():
    mesajlar = [
        "Sayın yetkili, çay molası başlatılmıştır. İdare eder.",
        "Resmi çay demleme protokolü aktif. Lütfen bekleyiniz.",
        "Mola süresi uzatıldı. Gerekçe: çay henüz demlenmedi.",
        "Ofis çayı bilimsel olarak en optimal sıcaklıkta.",
        "Çay bardağı resmi olarak dolduruldu. İşlem tamamlandı.",
        "Sıradaki mola: 5 dakika sonra. Ama aslında 50.",
        "Çay içmeden iş yapılamaz. Bu bir yasadır.",
        "Mola iptal edildi. Gerekçe: çay bitti. Yeni çay demleniyor.",
        # gizli siyasi: her şey kontrollü, kayyum gözetiminde
        "Tüm molalar üst makamlarca onaylanmıştır. Endişe etmeyiniz.",
        "Çay demlenirken evren genişliyor. Bu normaldir."
    ]
    return random.choice(mesajlar)

def sonsuz_mola():
    print("=== RESMİ ÇAY MOLASI PLANLAYICI BAŞLATILDI ===")
    print("Bu sistem sonsuza kadar çalışır. Durdurmak için Ctrl+C.")
    print("Ciddiye alınız. İdare eder.\n")
    
    sayac = 0
    try:
        while True:
            sayac += 1
            print(f"[{sayac}] {resmi_mesajlar()}")
            time.sleep(random.uniform(2, 5))  # gerçek bekleme, çok ciddi
            if sayac % 7 == 0:
                print(">>> Resmi uyarı: Çay bardağı yeniden dolduruluyor. Lütfen ayağa kalkmayınız.")
    except KeyboardInterrupt:
        print("\nMola sonlandırıldı. Ama çay hâlâ demleniyor. İdare eder.")
        sys.exit(0)

if __name__ == "__main__":
    sonsuz_mola()
