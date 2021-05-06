# getDataFromBusinessInsider
Get Data from Business Insider with Scrapy and Cloud Firestore (Firebase)

Scrapy Framework ile businessinider'dan veri cekme ve Firebase'e gonderme

Scrapy ile cektiginiz datayi /// scrapy crawl projectname -o istediginizjsonismi.json

olusturdugunuz json dosyasini firebase'e gondermek istiyorsaniz kodun dizininden cmd dosyasi acin ve assagidaki kodlari yazin = 

///   main.py data.json add users-demo-add
main kismina yazdigim kodu aliniz ve calistiriniz 

main kisminda cred = credentials.Certificate('service-accountkey.json') 
yazili olan yeri kendi firestore'unuzu entegre ettikten sonra dosyanin ismini yaziniz aksi halde calismaz


data.json => projedeki json dosyaniz 

users-demo-add => burasi firestore'da collection name'i

Umarim faydali olur saglicakla kalin
