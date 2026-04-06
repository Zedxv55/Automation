from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # 1. เปิดแบบ headless=False เพื่อให้เราเห็นหน้าจอ และ "ช่วยกด" ถ้าติด Verify
        browser = p.chromium.launch(headless=False) 
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        )
        page = context.new_page()
        
        print("กำลังเชื่อมต่อกับหน้าหลัก readAwrite...")
        url = "https://www.readawrite.com/"
        
        # ไปที่หน้าเว็บ
        page.goto(url)
        
        # 2. ให้เวลาคุณ 15 วินาที ในการกด "ยืนยันว่าเป็นมนุษย์" (ถ้ามีขึ้นมา)
        print("ตรวจสอบหน้าจอ Browser: ถ้ามีปุ่ม Verify ให้รีบกดนะครับ...")
        page.wait_for_timeout(15000) 
        
        # เลื่อนหน้าจอเพื่อให้ข้อมูลโหลด
        page.mouse.wheel(0, 1500)
        page.wait_for_timeout(3000)
        
        print("\n--- รายชื่อนิยายยอดนิยมบนหน้าหลัก ---")
        
        # เจาะจงคลาส .thumbnail-title ซึ่งเป็นมาตรฐานของเว็บนี้
        novels = page.query_selector_all(".thumbnail-title")
        
        count = 0
        for novel in novels:
            title = novel.inner_text().strip()
            if title and len(title) > 2:
                print(f"{count+1}. {title}")
                count += 1
                if count >= 20: break

        if count == 0:
            print("ยังไม่พบข้อมูล... เว็บอาจจะใช้โครงสร้างอื่นในหน้าหลัก ลองสแกนหาทุกลิงก์แทน...")
            # แผนสำรอง: กวาดทุกลิงก์ที่น่าจะเป็นชื่อนิยาย
            links = page.query_selector_all("a")
            for link in links:
                t = link.inner_text().strip()
                if len(t) > 10 and count < 15: # ชื่อนิยายมักจะยาว
                    print(f"สำรอง {count+1}. {t}")
                    count += 1

        print(f"\nดึงข้อมูลสำเร็จทั้งหมด {count} รายการ")
        browser.close()
        # ... โค้ดเดิมของคุณด้านบน ...
        novels_found = [] # สร้างตะกร้าเก็บชื่อนิยาย
        links = page.query_selector_all("a")
        for link in links:
            t = link.inner_text().strip()
            if len(t) > 10 and count < 15:
                print(f"สำรอง {count+1}. {t}")
                novels_found.append(t) # เก็บชื่อใส่ตะกร้าไว้
                count += 1
        
        browser.close()
        return novels_found # ส่งตะกร้าชื่อนิยายออกไปนอกไฟล์

if __name__ == "__main__":
    run()
    