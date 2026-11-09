# 🚀 دليل رفع وتشغيل CyberShield AI على قوقل (Google Deployment Guide)

تم تجهيز أداة **CyberShield AI** بثلاث طرق احترافية للرفع والتشغيل على منصات قوقل (Google) مباشرة دون أي عناء:

---

## 🥇 الطريقة الأولى: التشغيل السحابي المجاني عبر Google Colab (الأسهل والأنسب للبحث العلمي)

ملف الدفتر التفاعلي جاهز ومبني بالكامل:
📁 **[`CyberShield_AI_Google_Colab.ipynb`](file:///C:/Users/mohamad.abdelraouf/.gemini/antigravity/scratch/cybershield-ai/CyberShield_AI_Google_Colab.ipynb)**

### خطوات التشغيل:
1. افتح موقع **[Google Colab](https://colab.research.google.com/)**.
2. اختر **Upload (رفع)**، وحدد الملف `CyberShield_AI_Google_Colab.ipynb` من جهازك:
   `C:\Users\mohamad.abdelraouf\.gemini\antigravity\scratch\cybershield-ai\CyberShield_AI_Google_Colab.ipynb`
3. من القائمة العلوية اضغط على **Runtime ➔ Run all** (أو اضغط `Ctrl + F9`).
4. **ماذا سيحدث داخل قوقل كولاب؟**
   - تثبيت مكتبات الذكاء الاصطناعي ومعالجة اللغات الطبيعية.
   - تدريب نماذج اللهجة المصرية والعربية والإنجليزية والروابط فورياً.
   - تشغيل **مفحص تفاعلي داخل الكولاب** لاختبار الرسائل مباشرة باللغة العربية.
   - إطلاق خادم الويب الكامل وتوليد **رابط عام مجاني (Public URL)** لفتح لوحة التحكم على الإنترنت لأي شخص!

---

## 🥈 الطريقة الثانية: الرفع كإضافة رسمية لمتصفح قوقل كروم (Google Chrome Extension)

تم بناء إضافة متصفح قوقل كروم كاملة ومتوافقة مع المعيار الأحدث (Manifest V3):
📁 مجلد الإضافة: **[`chrome_extension/`](file:///C:/Users/mohamad.abdelraouf/.gemini/antigravity/scratch/cybershield-ai/chrome_extension)**

### خطوات التثبيت والتشغيل في متصفح قوقل كروم:
1. افتح متصفح **Google Chrome** واكتب في شريط العنوان: `chrome://extensions`
2. فعّل خيار **وضع المطور (Developer mode)** في الزاوية العلوية اليمنى.
3. اضغط على زر **تحميل إضافة تم فك حزمتها (Load unpacked)**.
4. حدد المجلد:
   `C:\Users\mohamad.abdelraouf\.gemini\antigravity\scratch\cybershield-ai\chrome_extension`
5. مبروك! ستظهر أيقونة **🛡️ CyberShield AI** في شريط أدوات كروم. يمكنك الآن:
   - فحص رابط أي صفحة تزورها بضغطة زر.
   - تظليل أي نص رسالة مشبوهة والنقر بالزر الأيمن للفحص الفوري (`فحص النص عبر CyberShield AI`).

---

## 🥉 الطريقة الثالثة: النشر السحابي الكامل عبر Google Cloud Run (سيرفر حقيقي دائم)

تم إعداد حاوية Docker ومواصفات النشر السحابي التلقائي:
- 📁 **[`Dockerfile`](file:///C:/Users/mohamad.abdelraouf/.gemini/antigravity/scratch/cybershield-ai/Dockerfile)**
- 📁 **[`deploy_google_cloud.bat`](file:///C:/Users/mohamad.abdelraouf/.gemini/antigravity/scratch/cybershield-ai/deploy_google_cloud.bat)**

### خطوات الرفع بنقرة واحدة:
1. تأكد من تثبيت [Google Cloud SDK](https://cloud.google.com/sdk).
2. افتح موجه الأوامر داخل مجلد المشروع ونفذ:
   ```cmd
   deploy_google_cloud.bat
   ```
3. سيقوم السكربت برفع الحاوية إلى **Google Cloud Run** في بضع دقائق، وسيعطيك رابط ويب دائم ومجاني بصيغة:
   `https://cybershield-ai-xxxx-uc.a.run.app`
