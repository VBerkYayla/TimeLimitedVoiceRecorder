import sounddevice as sd
from scipy.io.wavfile import write
import datetime

# Kullanıcıdan süreyi al
try:
    duration = int(input("Kayıt süresini (saniye) giriniz: "))
except ValueError:
    print("Hatalı giriş! Lütfen sayı giriniz.")
    exit()

# Örnekleme frekansı
freq = 44100

# Dosya adını tarih-saat ile oluştur
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"recording_{timestamp}.wav"

try:
    print("🎙 Kayıt başlıyor...")
    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
    sd.wait()  # Kayıt tamamlanana kadar bekler
    write(filename, freq, recording)
    print(f"✅ Kayıt tamamlandı! '{filename}' olarak kaydedildi.")
except Exception as e:
    print(f"❌ Kayıt sırasında bir hata oluştu: {e}")
