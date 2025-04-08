from flask import Flask, render_template  # استيراد Flask ودالة render_template

app = Flask(__name__)  # إنشاء تطبيق Flask

# الصفحة الرئيسية - تعرض عنوان وصورة
@app.route("/")  # المسار الأساسي للموقع (الرئيسية)
def home():
    return render_template("index.html")  # عرض قالب الصفحة الرئيسية

# صفحة "من نحن" - تعرض نصاً بسيطاً
@app.route("/about")  # المسار /about 
def about():
    return render_template("about.html")  # عرض قالب صفحة من نحن

# صفحة "تواصل معنا" - تعرض نموذجاً للتعبئة
@app.route("/contact")  # المسار /contact 
def contact():
  return render_template("contact.html")  # عرض قالب صفحة تواصل معنا

# التأكد من تشغيل التطبيق عند تنفيذ الملف مباشرة
if __name__ == "__main__":  
    app.run(debug=True)