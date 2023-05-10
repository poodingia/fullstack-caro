# Demo referee để test backend và frontend
## Cách sử dụng:
1. Chạy môi trường ảo giống trong backend trong *referre*, ví dụ ở [link](https://flask.palletsprojects.com/en/2.2.x/installation/#virtual-environments)
2. Chạy câu lệnh `pip install -r requirements.txt` trong terminal để cài những thư viện cần thiết
3. Chạy flask run `flask run --debug --host=0.0.0.0 --port=3000` để bắt đầu, có thể đối sang port khác ![](res/terminal_demo.png)



* Những lần sau chỉ cần vào môi trường ảo và chạy `flask run --host=0.0.0.0`, không cần cài lại
* Server trọng tài đang có 3 API, **'/init'** để nhận yêu cầu khởi tạo, **'/'** để trả về thông tin render và **'/move'** để nhận nước đi'
* Hiện tại, tài đang trả về đúng nhưng gì đang được nhận
