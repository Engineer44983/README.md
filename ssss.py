#!/usr/bin/python3
# -*- coding: utf-8 -*-

# python 3.3.2+ ssss.py Dos Script v.1
# by Can Yalçın
# only for legal purpose
"""
نظام تعليمي لمحاكاة أنظمة اكتشاف التسلل
لأغراض التدريب والبحث الأمني المشروع
"""

import asyncio
import json
import hashlib
from datetime import datetime
from dataclasses import dataclass
from typing import Dict, List, Optional
import ipaddress

@dataclass
class SecurityEvent:
    """فئة تمثل حدث أمني"""
    timestamp: str
    source_ip: str
    destination_ip: str
    protocol: str
    alert_level: str  # LOW, MEDIUM, HIGH, CRITICAL
    description: str
    signature_id: str
    
class EducationalIDS:
    """نظام اكتشاف تسلل تعليمي"""
    
    def __init__(self):
        self.threat_signatures = self.load_signatures()
        self.whitelist_ips = self.load_whitelist()
        self.events_log: List[SecurityEvent] = []
        
    def load_signatures(self) -> Dict:
        """تحميل توقيعات التهديدات التعليمية"""
        return {
            "EDU-001": {
                "name": "Port Scan Simulation",
                "pattern": "SYN.*SYN.*SYN",
                "severity": "MEDIUM"
            },
            "EDU-002": {
                "name": "SQL Injection Pattern",
                "pattern": "(?i)(union.*select|drop.*table|1=1)",
                "severity": "HIGH"
            },
            "EDU-003": {
                "name": "XSS Attempt",
                "pattern": "(?i)(<script>|alert\\(|onload=)",
                "severity": "HIGH"
            }
        }
    
    def load_whitelist(self) -> List:
        """قائمة IPs مسموح بها (للتعليم)"""
        return [
            "192.168.1.0/24",
            "10.0.0.0/8"
        ]
    
    def is_ip_allowed(self, ip: str) -> bool:
        """التحقق من أن IP مسموح بها"""
        try:
            ip_addr = ipaddress.ip_address(ip)
            for network in self.whitelist_ips:
                if ip_addr in ipaddress.ip_network(network):
                    return True
        except:
            pass
        return False
    
    def analyze_packet(self, packet_data: Dict) -> Optional[SecurityEvent]:
        """تحليل حزمة بيانات (محاكاة)"""
        
        # تخطي IPs المسموح بها
        if self.is_ip_allowed(packet_data.get('src_ip', '')):
            return None
        
        # البحث عن أنماط مشبوهة
        payload = packet_data.get('payload', '').lower()
        
        for sig_id, signature in self.threat_signatures.items():
            import re
            if re.search(signature['pattern'], payload, re.IGNORECASE):
                event = SecurityEvent(
                    timestamp=datetime.now().isoformat(),
                    source_ip=packet_data.get('src_ip', 'UNKNOWN'),
                    destination_ip=packet_data.get('dst_ip', 'UNKNOWN'),
                    protocol=packet_data.get('protocol', 'TCP'),
                    alert_level=signature['severity'],
                    description=f"تم اكتشاف: {signature['name']}",
                    signature_id=sig_id
                )
                self.events_log.append(event)
                return event
        
        return None
    
    def generate_threat_report(self) -> Dict:
        """إنشاء تقرير عن التهديدات المكتشفة"""
        report = {
            "generated_at": datetime.now().isoformat(),
            "total_events": len(self.events_log),
            "events_by_severity": {},
            "recent_events": []
        }
        
        # تجميع الأحداث حسب مستوى الخطورة
        for event in self.events_log[-100:]:  # آخر 100 حدث
            report["events_by_severity"][event.alert_level] = \
                report["events_by_severity"].get(event.alert_level, 0) + 1
            
            report["recent_events"].append({
                "time": event.timestamp,
                "source": event.source_ip,
                "alert": event.description,
                "severity": event.alert_level
            })
        
        return report

# مثال للاستخدام
async def network_monitor_simulation():
    """محاكاة مراقبة شبكة لأغراض تعليمية"""
    
    ids = EducationalIDS()
    
    # بيانات اختبارية
    test_packets = [
        {
            "src_ip": "192.168.1.100",
            "dst_ip": "10.0.0.1",
            "protocol": "TCP",
            "payload": "Normal HTTP request"
        },
        {
            "src_ip": "203.0.113.5",
            "dst_ip": "10.0.0.2",
            "protocol": "TCP",
            "payload": "<script>alert('xss')</script>"
        },
        {
            "src_ip": "198.51.100.10",
            "dst_ip": "10.0.0.3",
            "protocol": "TCP",
            "payload": "admin' OR '1'='1"
        }
    ]
    
    print("🔍 بدء تحليل حركة المرور الشبكية (محاكاة)...")
    
    for packet in test_packets:
        event = ids.analyze_packet(packet)
        if event:
            print(f"⚠️  تنبيه أمني: {event.description}")
            print(f"   المصدر: {event.source_ip}")
            print(f"   الخطورة: {event.alert_level}")
            print("-" * 50)
    
    # توليد التقرير
    report = ids.generate_threat_report()
    print(f"\n📊 التقرير الأمني:")
    print(f"إجمالي الأحداث: {report['total_events']}")
    print("الأحداث حسب الخطورة:")
    for severity, count in report["events_by_severity"].items():
        print(f"  {severity}: {count}")
