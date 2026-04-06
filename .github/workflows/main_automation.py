import google.generativeai as genai
from trend_scraper import run as run_scraper
from novel_factory import create_word_file, get_style

# 1. ตั้งค่า AI (เอา Key ของคุณมาวางตรงนี้)
genai.configure(api_key="YAIzaSyADwc2NTqUd0wT187z2EVImJmZpmJ_T8IU")
model = genai.GenerativeModel('gemini-pro')

def start_production():
    # ก้าวที่ 1: สั่งตัวเจาะข้อมูลไปหาชื่อนิยายมา (ใช้โค้ดเดิม)
    print("🚀 กำลังเจาะข้อมูลเทรนด์ล่าสุด...")
    titles = run_scraper() 
    
    # ก้าวที่ 2: ดึงสำนวน DNA ของคุณมา
    my_style = get_style()
    
    # ก้าวที่ 3: สั่ง AI เขียนทีละเรื่อง!
    for title in titles[:3]: # ทดสอบแค่ 3 เรื่องก่อน
        print(f"✍️ AI กำลังร่างเรื่อง: {title}")
        
        prompt = f"เขียนตอนที่ 1 ของนิยายชื่อ '{title}' โดยใช้สำนวนแบบนี้: {my_style}"
        response = model.generate_content(prompt)
        
        # ก้าวที่ 4: ส่งเนื้อหาไปทำไฟล์ Word (ใช้โค้ดใหม่)
        create_word_file(title, response.text)

if __name__ == "__main__":
    start_production()