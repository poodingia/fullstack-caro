# Hướng dẫn sử dụng
<h4>Cấu trúc</h4>
<ul>
<li>index.html: File HTML hiển thị tất cả thông tin từ JSON</li>
<li>style.css: Style file index.html</li>
<li>script.js: Script fetch file JSON và render lại giao diện HTML từ thông tin trong JSON</li>
</ul>

<h4>Hướng dẫn</h4>
<ol>
<li>Mở file index.html để hiển thị giao diện</li>
<li>Đặt link file JSON làm tham số truyền vào hàm fetch() trong hàm getJSON() trong file script.js</li>
<img src="public/resources/jsonguide.png"></img>
<li>Sử dụng terminal, cd đến thư mục "my-app" và chạy npm start </li>
<li>Ứng dụng mặc định chạy trên cổng 3006, có thể chỉnh trong "package.json" và đổi 3306 thành port bạn mong muốn</li>
<img src="public/resources/port.png"></img>
<li>Script sẽ fetch JSON từ API cung cấp bới Backen và re-render trang web mỗi 1 giây</li>
</ol>

<h4>Các thành phần của giao diện</h4>
<img src="public/resources/guide.png"></img>

