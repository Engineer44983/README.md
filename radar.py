#!/usr/bin/python3
# -*- coding: utf-8 -*-

# python 3.3.2+ radar.py Dos Script v.1
# by Can Yalçın
# only for legal purpose

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
from datetime import datetime

class RadarSimulation:
    """
    محاكاة تعليمية لعرض بيانات على خريطة - لأغراض تعليمية فقط
    NOT A REAL RADAR SYSTEM
    """
    
    def __init__(self):
        # إحداثيات تقريبية للعراق
        self.iraq_bounds = {
            'lat_min': 29.0, 'lat_max': 37.5,
            'lon_min': 38.5, 'lon_max': 48.5
        }
        
        self.aircraft_data = []
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        
    def generate_random_aircraft(self, num=5):
        """إنشاء بيانات طائرات عشوائية لأغراض المحاكاة"""
        aircraft = []
        for i in range(num):
            aircraft.append({
                'id': f'AC{random.randint(1000, 9999)}',
                'lat': random.uniform(self.iraq_bounds['lat_min'], 
                                     self.iraq_bounds['lat_max']),
                'lon': random.uniform(self.iraq_bounds['lon_min'], 
                                     self.iraq_bounds['lon_max']),
                'course': random.uniform(0, 360),
                'speed': random.uniform(400, 900),  # كم/ساعة
                'history': []
            })
        return aircraft
    
    def draw_iraq_map(self):
        """رسم خريطة مبسطة للعراق"""
        # رسم حدود تقريبية
        iraq_outline = np.array([
            [37.0, 42.0], [37.0, 48.0], [29.0, 48.0],
            [29.0, 42.0], [31.0, 39.0], [37.0, 42.0]
        ])
        
        self.ax.plot(iraq_outline[:, 1], iraq_outline[:, 0], 
                    'k-', linewidth=1, alpha=0.5)
        
        # إضافة مدن رئيسية
        cities = {
            'بغداد': (33.3, 44.4),
            'البصرة': (30.5, 47.8),
            'الموصل': (36.3, 43.1),
            'أربيل': (36.2, 44.0),
            'السليمانية': (35.5, 45.4)
        }
        
        for city, (lat, lon) in cities.items():
            self.ax.plot(lon, lat, 'bo', markersize=6, alpha=0.7)
            self.ax.text(lon + 0.1, lat + 0.1, city, fontsize=9, 
                        fontfamily='DejaVu Sans', alpha=0.8)
    
    def update_aircraft_positions(self):
        """تحديث مواقع الطائرات (محاكاة)"""
        for ac in self.aircraft_data:
            # حفظ التاريخ للمسار
            ac['history'].append((ac['lat'], ac['lon']))
            if len(ac['history']) > 20:  # حفظ آخر 20 نقطة فقط
                ac['history'].pop(0)
            
            # تحريك الطائرة
            ac['lat'] += random.uniform(-0.1, 0.1)
            ac['lon'] += random.uniform(-0.1, 0.1)
            
            # التأكد من بقاء الطائرة داخل الحدود
            ac['lat'] = max(self.iraq_bounds['lat_min'], 
                           min(self.iraq_bounds['lat_max'], ac['lat']))
            ac['lon'] = max(self.iraq_bounds['lon_min'], 
                           min(self.iraq_bounds['lon_max'], ac['lon']))
    
    def draw_radar_screen(self):
        """رسم شاشة الرادار"""
        self.ax.clear()
        
        # خلفية حمراء (شاشة الرادار التقليدية)
        self.ax.set_facecolor('darkred')
        
        # رسم خريطة العراق
        self.draw_iraq_map()
        
        # رسم الطائرات ومساراتها
        for ac in self.aircraft_data:
            # رسم المسار
            if len(ac['history']) > 1:
                history = np.array(ac['history'])
                self.ax.plot(history[:, 1], history[:, 0], 
                           'g-', linewidth=1, alpha=0.5)
            
            # رسم الطائرة
            self.ax.plot(ac['lon'], ac['lat'], 'go', markersize=8)
            self.ax.text(ac['lon'] + 0.05, ac['lat'] + 0.05, 
                        ac['id'], color='white', fontsize=8)
        
        # إعدادات الرسم
        self.ax.set_xlim(self.iraq_bounds['lon_min'] - 1, 
                        self.iraq_bounds['lon_max'] + 1)
        self.ax.set_ylim(self.iraq_bounds['lat_min'] - 1, 
                        self.iraq_bounds['lat_max'] + 1)
        self.ax.set_xlabel('خط الطول')
        self.ax.set_ylabel('خط العرض')
        self.ax.set_title('محاكاة تعليمية - عرض بيانات جغرافية\n(ليس نظام رادار حقيقي)', 
                         color='white', fontsize=14)
        self.ax.grid(True, alpha=0.3, color='white')
    
    def animate(self, frame):
        """دالة التحميل للرسوم المتحركة"""
        self.update_aircraft_positions()
        self.draw_radar_screen()
        return self.ax,
    
    def run_simulation(self):
        """تشغيل المحاكاة"""
        self.aircraft_data = self.generate_random_aircraft(8)
        
        # إنشاء الرسوم المتحركة
        ani = animation.FuncAnimation(
            self.fig, self.animate, frames=100,
            interval=500, blit=False, repeat=True
        )
        
        plt.show()

# تحذير أمني مهم
print("=" * 70)
print("تحذير: هذا كود محاكاة تعليمي فقط")
print("هذا ليس نظام رادار حقيقي ولا يمكن استخدامه للكشف عن الطائرات")
print("يستخدم فقط لأغراض التعليم والتدريب على التصور الجغرافي")
print("=" * 70)
print()

if __name__ == "__main__":
    # طلب التأكيد من المستخدم
    response = input("هل تريد تشغيل المحاكاة التعليمية؟ (نعم/لا): ")
    
    if response.lower() in ['نعم', 'y', 'yes']:
        simulator = RadarSimulation()
        simulator.run_simulation()
    else:
        print("تم إلغاء التشغيل.")
