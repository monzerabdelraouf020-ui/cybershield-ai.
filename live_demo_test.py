import sys
if sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

import urllib.request
import json

TEST_CASES = [
    {
        "title": "حالة 1: رسالة تصيد مصرية (فودافون كاش وجائزة وهمية)",
        "input": "مبروك كسبت 50000 جنيه من فودافون كاش! دوس ع اللينك واستلم فلوسك: http://voda-cash-win.xyz/claim"
    },
    {
        "title": "حالة 2: انتحال بنك مصر وتهديد بتجميد الحساب",
        "input": "خدمه عملاء بنك مصر: مطلوب فورا تحديث بطاقتك الائتمانية قبل الساعه 6 مساء عشان حسابك هيقف نهائيا. ادخل اللينك: http://banquemisr-online.xyz/update"
    },
    {
        "title": "حالة 3: رسالة رسمية شرعية من تطبيق انستاباي (آمنة)",
        "input": "انستاباي: رمز التأكيد السري الخاص بك لتسجيل الدخول هو 749281. تحذير: لا تشارك هذا الرمز مع أي شخص حتى موظفي البنك."
    },
    {
        "title": "حالة 4: رابط خبيث مباشر يستخدم عنوان IP بدلاً من نطاق رسمي",
        "input": "http://192.168.1.104/vodafone-cash/login.php"
    },
    {
        "title": "حالة 5: رسالة تصيد إنجليزية (انتحال PayPal وتجميد الحساب)",
        "input": "URGENT: Your PayPal account has been suspended due to unauthorized login attempts. Verify your identity now: https://paypal-security-account.top/verify"
    },
    {
        "title": "حالة 6: إشعار سحب شرعي من البنك الأهلي المصري (آمن)",
        "input": "البنك الأهلي المصري: تم سحب مبلغ 500 جنيه من ماكينة صراف آلي برقم بطاقة تنتهي بـ 4920. الرصيد المتاح 18,400 جنيه."
    }
]

def run_tests():
    print("=" * 70)
    print("🛡️  CyberShield AI — اختبار مباشر وحي للنظام عبر الـ REST API")
    print("🌐 خادم الويب: http://127.0.0.1:8000")
    print("=" * 70)

    for i, test in enumerate(TEST_CASES, 1):
        payload = json.dumps({"text": test["input"]}).encode('utf-8')
        req = urllib.request.Request(
            "http://127.0.0.1:8000/api/analyze",
            data=payload,
            headers={"Content-Type": "application/json"}
        )

        try:
            with urllib.request.urlopen(req) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                
                verdict_emoji = "🚨" if data["verdict"] == "Phishing" else ("⚠️" if data["verdict"] == "Suspicious" else "✅")
                print(f"\n[{i}/6] {test['title']}")
                print(f"📥 المدخلات: \"{test['input']}\"")
                print(f"📊 النتيجة: {verdict_emoji} {data['verdict']} ({data['risk_level']})")
                print(f"📈 نسبة الخطورة: {data['risk_percentage']}% | مستوى الثقة: {data['confidence_percentage']}%")
                print(f"🗣️  اللغة/اللهجة: {data['detected_language']} ({'مصري عامي' if data.get('is_egyptian') else 'فصحى/أخرى'})")
                print(f"⚡ زمن الاستجابة: {data['processing_time_ms']} مللي ثانية")
                
                print("🔍 أسباب التحذير التفسيرية (XAI):")
                if data["explanation_factors"]:
                    for f in data["explanation_factors"][:3]:
                        print(f"   • [{f.get('severity', 'INFO')}] {f.get('description_ar', f.get('description_en'))}")
                else:
                    print("   • لا توجد عوامل خطر (رسالة آمنة تماماً)")
                
                print("-" * 70)
        except Exception as e:
            print(f"❌ خطأ أثناء الفحص: {e}")

    # Check updated stats
    try:
        with urllib.request.urlopen("http://127.0.0.1:8000/api/stats") as resp:
            stats = json.loads(resp.read().decode('utf-8'))
            print("\n📈 إحصائيات قاعدة البيانات المسجلة الآن في SQLite:")
            print(f"   • إجمالي الفحوصات: {stats['total_scans']}")
            print(f"   • تهديدات التصيد المكتشفة: {stats['phishing_detected']}")
            print(f"   • الرسائل الآمنة: {stats['safe_verified']}")
            print(f"   • متوسط سرعة الفحص: {stats['avg_latency_ms']} ms")
    except Exception as e:
        print(f"Stats check error: {e}")

if __name__ == "__main__":
    run_tests()
