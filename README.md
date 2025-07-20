# สอง API ด้วย Docker Compose

## วิธีใช้งาน

1. แตก zip แล้วเข้าโฟลเดอร์โปรเจกต์นี้
2. เปิด terminal แล้วรัน:
```bash
docker-compose up --build
```

3. เปิดเว็บเบราว์เซอร์ที่ `http://localhost:8080`

ถ้าทุกอย่างถูกต้อง จะเห็นข้อความประมาณนี้:

```
API1 -> API2 ตอบกลับว่า: สวัสดีจาก API2!
```

## โครงสร้างโปรเจกต์

```
.
├── api1/
│   ├── main.py
│   └── Dockerfile
├── api2/
│   ├── main.py
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## คำอธิบาย

- API1 รับคำขอจากผู้ใช้ แล้วเรียก API2
- API2 ตอบกลับว่า "สวัสดีจาก API2"
- ทั้งสอง API มีการ print log ตอนทำงาน
- ทั้งหมดรันด้วย docker-compose
