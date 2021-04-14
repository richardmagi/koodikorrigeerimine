import datetime

def tänane_kuupäev():
    return datetime.date.today()

def kuupäev_str(p_kp):
    # saab sisendiks kuupäeva ja tagastab selle sõnena formaadis (pp.kk.aaaa)
    return p_kp.strftime("%d.%m.%Y")

def arvuta_visiidi_kuupäev(p_külastuse_kuupäev):
    täna = tänane_kuupäev()
    # liidame pool aastat (182 päeva) viimasele külastusele
    uus_visiidiaeg = p_külastuse_kuupäev + datetime.timedelta(182)
    if uus_visiidiaeg <= täna:
        uus_visiidiaeg = täna + datetime.timedelta(1)
    return uus_visiidiaeg

def kirjuta_logifaili(p_kommentaar, p_väärtus):
    # saab parameetrina kommentaari ning väärtuse, mis tuleb kirjutada logifaili
    # kirjutab need andmed logifaili koos kuupäeva ja kellaajaga
    praegu = datetime.datetime.now()
    fail = open("logifail.log", "a", encoding="UTF-8")
    rida = praegu.strftime("%d.%m.%Y") + " " + praegu.strftime("%X") + " " + p_kommentaar + ": " + str(p_väärtus)
    fail.write(rida + "\n")
    fail.close()

print("Hambaid tuleks lasta kontrollida vähemalt kaks korda aastas.")
print("Millal viimati hambaarsti juures käisid?")

try:
    kuupäev = input("Sisesta kuupäev (kujul pp.kk.aaaa): ")
    kirjuta_logifaili("Kasutaja sisend: ", kuupäev)
    i_päev, i_kuu, i_aasta = map(int, kuupäev.split('.'))
    külastuse_kuupäev = datetime.date(i_aasta, i_kuu, i_päev)
    
    if külastuse_kuupäev > tänane_kuupäev():
        print("Tulevikus ei saanud visiidil käia.")
    else:
        print("Viimane külastus oli: " + kuupäev_str(külastuse_kuupäev))
        uus_külastus = arvuta_visiidi_kuupäev(külastuse_kuupäev) 
        print("Peaksid minema uuele visiidile umbes: " + kuupäev_str(uus_külastus))
except Exception as vale_formaat:
    print("Sisestasid kuupäeva vales formaadis!")
    kirjuta_logifaili("Tekkis viga", vale_formaat)
