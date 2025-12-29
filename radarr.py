#!/usr/bin/python3
# -*- coding: utf-8 -*-

# python 3.3.2+ radarr.py Dos Script v.1
# by Can Yalçın
# only for legal purpose
"""
برنامج تعليمي لاستخدام RTL-SDR لأغراض التعليم والتجريب
تحذير: هذا ليس نظام رادار حقيقي ولا يمكن استخدامه للكشف عن الدرون
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import warnings
warnings.filterwarnings('ignore')

print("=" * 70)
print("برنامج تعليمي لتجريب مفاهيم استقبال RF باستخدام RTL-SDR")
print("تحذير: هذا ليس نظام رادار ولا يمكنه الكشف عن الدرون")
print("يستخدم فقط لأغراض التعليم والبحث المشروع")
print("=" * 70)

class RTL_SDR_Simulator:
    """مُحاكي تعليمي لأساسيات استقبال SDR"""
    
    def __init__(self):
        self.frequency = 433e6  # تردد ISM شائع (ليس لرادار)
        self.sample_rate = 2.4e6
        self.gain = 40
        
    def simulate_signal(self):
        """محاكاة إشارة RF بسيطة لأغراض التعليم"""
        # هذه مجرد إشارة تجريبية وليست حقيقية
        t = np.linspace(0, 0.01, 1000)
        
        # محاكاة إشارة أساسية
        signal = np.sin(2 * np.pi * 1000 * t)
        
        # إضافة بعض الضوضاء
        noise = 0.1 * np.random.randn(len(t))
        
        return t, signal + noise
    
    def plot_spectrum(self):
        """رسم طيف ترددي تعليمي"""
        t, signal = self.simulate_signal()
        
        # تحويل فورييه
        fft_result = np.fft.fft(signal)
        freqs = np.fft.fftfreq(len(t), t[1]-t[0])
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
        
        # الإشارة الزمنية
        ax1.plot(t, signal)
        ax1.set_title('إشارة RF محاكاة (تعليمية)')
        ax1.set_xlabel('الزمن (ثانية)')
        ax1.set_ylabel('السعة')
        ax1.grid(True)
        
        # الطيف الترددي
        ax2.plot(freqs[:len(freqs)//2], 
                np.abs(fft_result[:len(fft_result)//2]))
        ax2.set_title('الطيف الترددي (تعليمي)')
        ax2.set_xlabel('التردد (Hz)')
        ax2.set_ylabel('المقدار')
        ax2.grid(True)
        
        plt.tight_layout()
        plt.show()

class EducationalDroneDetector:
    """مُحاكي تعليمي لمفاهيم اكتشاف الإشارات"""
    
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.detections = []
        
    def simulate_detection(self):
        """محاكاة اكتشاف إشارة لأغراض التعليم"""
        # بيانات عشوائية للعرض فقط
        x = np.random.uniform(-10, 10)
        y = np.random.uniform(-10, 10)
        strength = np.random.uniform(0.1, 1.0)
        
        return x, y, strength
    
    def update_plot(self, frame):
        """تحديث الرسم المتحرك"""
        self.ax.clear()
        
        # محاكاة اكتشاف جديد
        if np.random.random() > 0.7:  # 30% فرصة لاكتشاف جديد
            x, y, strength = self.simulate_detection()
            self.detections.append({
                'x': x, 'y': y, 
                'strength': strength,
                'age': 0
            })
        
        # تحديث وتقدير الأعمار
        for det in self.detections:
            det['age'] += 1
            
        # إزالة الاكتشافات القديمة
        self.detections = [d for d in self.detections if d['age'] < 20]
        
        # رسم الاكتشافات
        for det in self.detections:
            color_intensity = det['strength']
            alpha = max(0.1, 1.0 - det['age']/20)
            
            self.ax.scatter(det['x'], det['y'], 
                          s=det['strength']*200,
                          c='green', alpha=alpha,
                          edgecolors='white')
        
        # إعدادات الرسم
        self.ax.set_xlim(-12, 12)
        self.ax.set_ylim(-12, 12)
        self.ax.set_facecolor('black')
        self.ax.set_title('محاكاة تعليمية - ليس نظام كشف حقيقي\nلأغراض التعليم فقط', 
                         color='white', fontsize=14)
        self.ax.grid(True, alpha=0.2, color='white')
        self.ax.set_xlabel('المسافة الأفقية (تعليمي)')
        self.ax.set_ylabel('المسافة العمودية (تعليمي)')
        
        return self.ax,
    
    def run_educational_simulation(self):
        """تشغيل المحاكاة التعليمية"""
        print("\nجاري تشغيل المحاكاة التعليمية...")
        print("هذا برنامج تعليمي فقط!")
        print("لا يستخدم RTL-SDR حقيقي ولا يمكنه اكتشاف الدرون")
        
        ani = FuncAnimation(self.fig, self.update_plot, 
                          frames=100, interval=500, 
                          blit=False, repeat=True)
        
        plt.show()

# برنامج تعليمي حقيقي لاستخدام RTL-SDR (بدون كشف درون)
def rtl_sdr_educational_example():
    """
    مثال تعليمي لأخذ عينات من RTL-SDR
    يتطلب: pip install pyrtlsdr
    """
    print("\n" + "="*60)
    print("مثال تعليمي لاستخدام RTL-SDR:")
    print("="*60)
    
    code_example = '''
# مثال تعليمي - لا تستخدم للكشف عن الدرون
from rtlsdr import RtlSdr
import numpy as np

# إعداد SDR (لأغراض التعليم فقط)
sdr = RtlSdr()

# إعدادات تعليمية (ليست لإشارات درون)
sdr.sample_rate = 2.4e6
sdr.center_freq = 100e6  # تردد FM راديوي
sdr.gain = 'auto'

try:
    # أخذ عينات لأغراض التعليم
    samples = sdr.read_samples(256*1024)
    
    # تحليل بسيط للعرض التعليمي
    power = np.mean(np.abs(samples)**2)
    print(f"مستوى الطاقة المقاس: {power:.6f}")
    
    # يمكن إضافة تحليل طيفي هنا لأغراض التعليم
    # ولكن ليس للكشف عن أي أجهزة محددة
    
except Exception as e:
    print(f"خطأ في القراءة: {e}")
finally:
    sdr.close()
    '''
    
    print(code_example)
    print("\nملاحظة: هذا الكود لأغراض التعليم فقط")
    print("مطلوب: pip install pyrtlsdr")
    print("يتطلب جهاز RTL-SDR حقيقي")

# القوانين واللوائح
def print_regulations():
    print("\n" + "="*60)
    print("القوانين واللوائح المهمة:")
    print("="*60)
    print("""
    1. قوانين الطيران الفيدرالية (FAA/FCC في الولايات المتحدة)
    2. لوائح الاتحاد الدولي للاتصالات (ITU)
    3. قوانين الخصوصية والتنصت
    4. قوانين الأمن الوطني
    
    الاستخدام غير المصرح به لأنظمة الكشف عن الدرون:
    - غير قانوني في معظم البلدان
    - قد يعاقب عليه بالسجن أو الغرامات الكبيرة
    - يعتبر انتهاكاً للخصوصية
    """)

# التوصيات المهنية
def professional_recommendations():
    print("\n" + "="*60)
    print("توصيات للتعلم المشروع:")
    print("="*60)
    print("""
    1. تعلم معالجة الإشارات الرقمية (DSP):
       - تحليل فورييه
       - المرشحات الرقمية
       - اكتشاف الإشارات
       
    2. دراسة SDR لأغراض التعليم:
       - GNU Radio (مجاني ومفتوح المصدر)
       - مشاريع RTL-SDR التعليمية
       - برمجيات هواة الراديو
       
    3. الحصول على التراخيص المناسبة:
       - رخصة هواة الراديو
       - تصاريح بحثية
       - تراخيص تطوير
       
    4. مصادر تعليمية آمنة:
       - Coursera: Digital Signal Processing
       - librosa: معالجة الصوت في Python
       - scipy.signal: معالجة الإشارات
    """)

# تشغيل البرنامج التعليمي
if __name__ == "__main__":
    print("\nاختر خياراً:")
    print("1. عرض المحاكاة التعليمية")
    print("2. عرض مثال RTL-SDR التعليمي")
    print("3. عرض القوانين واللوائح")
    print("4. التوصيات المهنية")
    
    choice = input("\nادخل اختيارك (1-4): ")
    
    if choice == "1":
        detector = EducationalDroneDetector()
        detector.run_educational_simulation()
    elif choice == "2":
        rtl_sdr_educational_example()
    elif choice == "3":
        print_regulations()
    elif choice == "4":
        professional_recommendations()
    else:
        print("خيار غير صالح")
