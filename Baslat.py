#Sistem bilgileri python-Alperen T
import time
import wmi #Windows Yönetim Araçları kütüphanesi
from colorama import init #Renk kütüphanesi
from colorama import Fore, Back, Style
init()
computer = wmi.WMI() #kütüphanemizi daha kolay kullanmak için değişken atıyoruz.
computer_info = computer.Win32_ComputerSystem()[0] #Değişkenimizi kullanarak pc bilgilerini çekiyoruz.
os_info = computer.Win32_OperatingSystem()[0]
proc_info = computer.Win32_Processor()[0]
gpu_info = computer.Win32_VideoController()[0] #İşlemci hızını bulmak için kütüphanemizi kullanıyoruz.
time.sleep(0.1)

os_name = os_info.Name.encode('utf-8').split(b'|')[0]#Çektiğimiz verileri utf-8 unicode diline çeviriyoruz
os_version = ' '.join([os_info.Version, os_info.BuildNumber]) #Bilgileri numaralandırıyoruz.
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576  # kb dan gb a dönüştürüyoruz.
print(Fore.WHITE)
time.sleep(0.01024) #Bu işlemler bilgisiyarımızı yorduğu için biraz dinlenme noktaları ekliyoruz.
print('OS İsim: {0}'.format(os_name)) #Format biçimini isim olarak ayarılıyoruz.
print('OS Versiyon: {0}'.format(os_version)) #Format biçimini versiyon olarak ayarılıyoruz.
time.sleep(1.01) #Bu işlemler bilgisiyarımızı yorduğu için biraz dinlenme noktaları ekliyoruz.
print('CPU: {0}'.format(proc_info.Name)) #Format biçimini gpu olarak ayarılıyoruz.
time.sleep(0.5) #Bu işlemler bilgisiyarımızı yorduğu için biraz dinlenme noktaları ekliyoruz.
if system_ram > 4.898307800292969: #Eğer ramimiz 4gb dan fazla ise yazı rengini yeşil yapıyoruz ve yeterli/yüksek ram yazıdıryorz.
    print(Fore.GREEN) #yeşil renk
    print("YETERLİ/YÜKSEK RAM") #yeterli yüksek ram
else:
    print(Fore.WHITE) #eğer değilse beyaz renk yapıyoruz

#Burada aslında else kısmına düşük ram yazdırmaya düşünündüm ancak tam 4GB ram olursa ne yapacağımı bilemedim.
#Aslında elif ve else kullanarak da hem 4gb hemde 4gb dan az olabilirdi ama yinede bu karmaşıklağa yol açma ihtimali vardı.
#O yüzden kod satırlarını uzatsada ben kolaylık bakımından bu işlemi tercih ettim.
if system_ram < 4.898307800292969: #RAMİMİZ 4GB dan az ise
    print(Fore.RED) #Kırmızı renk
    print("DÜŞÜK RAM") #DÜŞÜK RAM YAZIYORUZ
else:
    print(Fore.WHITE) #Değilse yazı rengimizi eski haline geri getiriyoruz
print('RAM: {0} GB'.format(system_ram)) #Format biçimini RAM olarak ayarılıyoruz.
time.sleep(1.024) #Bu işlemler bilgisiyarımızı yorduğu için biraz dinlenme noktaları ekliyoruz.
print('Grafik Kart: {0}'.format(gpu_info.Name)) #Format biçimini grafik kartı olarak ayarlıyoruz olarak ayarılıyoruz.
time.sleep(0.1024) #Bu işlemler bilgisiyarımızı yorduğu için biraz dinlenme noktaları ekliyoruz.
print('Sıcaklık: {0}')
time.sleep(4.24) #Bu işlemler bilgisiyarımızı yorduğu için biraz dinlenme noktaları ekliyoruz.
#Böylece sistemi kötü olan bilgisiyarlarda bile bu programın çalışmasını sağlıyabiliriz.
#Son olarak bilgisiyar bilgisi py dosyasını açarak bilgileri teyit ediyoruz.
#import BilgisiyarBilgisi