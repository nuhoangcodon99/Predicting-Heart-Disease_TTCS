# TTCS
## 1. age -  age
## 2. sex - (1 = male; 0 = female) 
## 3. cp - chest pain type - tức ngực 
    * 0: Typical angina: đau ngực liên quan đến giảm cung cấp máu cho tim
    * 1: Atypical angina: đau ngực không liên quan đến tim
    * 2: Non-anginal pain: điển hình là co thắt thực quản (không liên quan đến tim)
    * 3: Asymptomatic: đau ngực không có dấu hiệu của bệnh
## 4. trestbps - resting blood pressure (tính bằng mm Hg khi nhập viện) - huyết áp
    * bất cứ điều gì trên 130-140 thường gây lo ngại
## 5. chol - serum cholestoral in mg/dl - lượng cholestoral trong máu
    * serum = LDL + HDL + .2 * triglycerides
    * trên 200 là đáng lo ngại
## 6. fbs - (fasting blood sugar > 120 mg/dl)  - lượng đường trong máu
    * '>126' mg/dL báo hiệu bệnh tiểu đường
    * 1: có
    * 0: không
## 7. restecg - resting electrocardiographic results - kết quả điện tâm đồ
    * 0: Không có gì đáng lưu ý
    * 1: Sóng ST-T bất thường
        - có thể từ các triệu chứng nhẹ đến các vấn đề nghiêm trọng
        - tín hiệu nhịp tim không bình thường
    * 2: Phì đại thất trái có thể hoặc chắc chắn
        - Buồng bơm máu chính của tim mở rộng
## 8. thalach - maximum heart rate achieved - nhịp tim
    * nhịp tim tối đa đạt được
## 9. exang - exercise induced angina (1 = yes; 0 = no) - đau thắt ngực khi tập thể dục
    * 1: có
    * 0: không
## 10. oldpeak - ST chênh xuống do gắng sức so với nghỉ ngơi - tình trạng stress
    * nhìn vào sự căng thẳng của tim trong khi tập thể dục
    * trái tim không khỏe mạnh sẽ căng thẳng hơn
## 11. slope - the slope of the peak exercise ST segment - 
    * 0: Upsloping: nhịp tim tốt hơn khi tập thể dục (không phổ biến)
    * 1: Flatsloping: thay đổi tối thiểu (trái tim khỏe mạnh điển hình)
    * 2: Downslopins: dấu hiệu tim không khỏe
## 12. ca - number of major vessels (0-3) colored by flourosopy - số lượng các mạch chính
    * số mạch chính (0-3)
    * mạch màu có nghĩa là bác sĩ có thể nhìn thấy máu chảy qua
    * càng nhiều máu di chuyển càng tốt (không có cục máu đông)
## 13. thal - thalium stress result - stress thalium
    * Dấu hiệu của sóng
## 14. target - have disease or not (1=yes, 0=no) (= the predicted attribute)
    * 1: có
    * 0: không

# Để chạy chương trình:
    - run file app.py
    - nhập đầy đủ thông số và chọn model muốn dự đoán
    - Tích chọn "Tôi đảm bảo những gì kê khai"
    - Chọn Chuẩn đoán
    - giao diện chuẩn đoán hiện ra
# Một số ví dụ:
| age | sex | cp  | trestbps | chol | fbs | restecg | thalach | exang | oldpeak | slope | ca  | thal | target |
| --- | --- | --- | -------- | ---- | --- | ------- | ------- | ----- | ------- | ----- | --- | ---- | ------ |
| 52  | 1   | 0   | 125      | 212  | 0   | 1       | 168     | 0     | 1       | 2     | 2   | 3    | 0      |
| 53  | 1   | 0   | 140      | 203  | 1   | 0       | 155     | 1     | 3.1     | 0     | 0   | 3    | 0      |
| 44  | 1   | 2   | 130      | 233  | 0   | 1       | 179     | 1     | 0.4     | 2     | 0   | 2    | 1      |
