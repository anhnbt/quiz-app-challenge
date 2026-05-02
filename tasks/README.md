# 🚀 Quiz System - Product Backlog

## 🎯 Tầm nhìn Sản phẩm (Product Vision)
Xây dựng một nền tảng thi trắc nghiệm trực tuyến toàn diện, cho phép giáo viên tạo lập ngân hàng câu hỏi đa dạng và tổ chức các kỳ thi thời gian thực (Real-time Online Exam). Đồng thời giúp học viên luyện tập, đánh giá năng lực và theo dõi tiến độ học tập một cách trực quan, minh bạch.

---

## 🏗️ Danh sách Epic

1.  **IAM (Identity & Access Management)**: Quản lý đa đối tượng (Admin, Giáo viên, Học viên).
2.  **Question Bank & Taxonomy**: Hệ thống quản lý ngân hàng câu hỏi và danh mục phân loại.
3.  **Exam Engine & Real-time Proctoring**: Công cụ tạo đề thi, tổ chức thi trực tuyến và giám sát thời gian thực.
4.  **Analytics & Result History**: Hệ thống chấm điểm tự động, lịch sử thi và báo cáo phân tích.

---

## 📋 Chi tiết Product Backlog

### 🔐 Epic 1: Quản lý Tài khoản (IAM)
*Quản lý danh tính và phân quyền người dùng (Admin, Giáo viên, Học viên).*

| ID | User Story | Priority | Trạng thái | Acceptance Criteria (AC) |
| :--- | :--- | :---: | :---: | :--- |
| **US01** | **Xem DS học viên (Admin)** | P2 | 📝 To Do | - Hiển thị: Email, Tên, Ngày tạo, Lượt truy cập.<br>- Phân trang 20 items/trang.<br>- Sắp xếp: Mới nhất lên đầu. |
| **US02** | **Tìm kiếm học viên (Admin)** | P2 | 📝 To Do | - Tìm theo: Tên hiển thị, Email. |
| **US03** | **Xem DS giáo viên (Admin)** | P2 | 📝 To Do | - Tương tự US01 nhưng dành cho đối tượng Giáo viên. |
| **US04** | **Tìm kiếm giáo viên (Admin)** | P2 | 📝 To Do | - Tìm theo: Tên hiển thị, Email. |
| **US05** | **Duyệt tài khoản giáo viên** | P1 | 📝 To Do | - Button "Duyệt" trong DS Giáo viên.<br>- Tự động gửi email thông báo (kèm thông tin đăng nhập) sau khi duyệt. |
| **US06** | **Xóa tài khoản (Admin)** | P1 | 📝 To Do | - Yêu cầu xác nhận trước khi xóa.<br>- Đăng xuất ngay lập tức (force logout) nếu user đang login.<br>- Gửi email thông báo lý do bị xóa. |
| **US07** | **Đăng ký làm giáo viên** | P1 | 📝 To Do | - Form: Tên, Email, Mật khẩu, Nhập lại mật khẩu.<br>- Trạng thái: Chờ duyệt (Pending).<br>- Chuyển hướng về Trang chủ sau khi submit. |
| **US08** | **Đăng nhập giáo viên** | P0 | 📝 To Do | - Input: Email, Password.<br>- Điều kiện: Tài khoản đã được Admin duyệt. |
| **US09** | **Cập nhật Profile** | P2 | 📝 To Do | - Cập nhật: Tên hiển thị, Avatar.<br>- Khóa trường Email (không cho đổi). |
| **US10** | **Đăng ký học viên** | P0 | 📝 To Do | - Form: Email, Mật khẩu.<br>- Chuyển hướng sang trang Login sau khi thành công. |
| **US11** | **Đăng nhập học viên** | P0 | 📝 To Do | - Input: Email, Password.<br>- Chuyển hướng về Dashboard/Trang chủ. |
| **US12** | **Đổi mật khẩu** | P1 | 📝 To Do | - Xác thực mật khẩu cũ.<br>- Yêu cầu Login lại sau khi đổi thành công. |
| **US13** | **Quên mật khẩu** | P1 | 📝 To Do | - Xác thực qua mã OTP gửi tới Email.<br>- Thiết lập mật khẩu mới. |
| **US14** | **Đăng xuất** | P0 | 📝 To Do | - Xóa session và chuyển hướng về Trang chủ. |

### 📚 Epic 2: Ngân hàng Câu hỏi & Danh mục (Question Bank)
*Quản lý dữ liệu lõi của hệ thống.*

| ID | User Story | Priority | Trạng thái | Acceptance Criteria (AC) |
| :--- | :--- | :---: | :---: | :--- |
| **US15** | **Tạo danh mục (Admin/GV)** | P1 | 📝 To Do | - Tên (Unique), Mô tả.<br>- Auto uppercase chữ cái đầu của Tên. |
| **US17** | **Xem DS danh mục** | P1 | 📝 To Do | - Hiển thị: Tên, Số câu hỏi, Người tạo.<br>- Sắp xếp AlphaB, phân trang 20/trang. |
| **US18** | **Xóa danh mục** | P2 | 📝 To Do | - Chỉ xóa được danh mục chưa có câu hỏi.<br>- Giáo viên chỉ xóa được danh mục mình tạo. |
| **US23** | **Tạo câu hỏi mới (GV)** | P0 | 📝 To Do | - Form: Tiêu đề, Loại (1 đáp án, nhiều đáp án, Đúng/Sai), Độ khó, Đáp án, Danh mục.<br>- Validation: Phải chọn ít nhất 1 đáp án đúng. |
| **US24** | **Cập nhật câu hỏi** | P1 | 📝 To Do | - Khóa chỉnh sửa nếu câu hỏi đã nằm trong một bài thi. |
| **US26** | **Xem DS câu hỏi** | P1 | 📝 To Do | - Hiển thị đáp án đúng để GV đối chiếu.<br>- Phân trang 5 items/trang. |
| **US28** | **Tìm kiếm/Lọc câu hỏi** | P1 | 📝 To Do | - Lọc theo: Độ khó, Loại câu hỏi, Danh mục. |
| **US52** | **Import câu hỏi từ Excel** | P1 | 📝 To Do | - Hỗ trợ file .xlsx/.csv theo template.<br>- Tự động map các cột: Tiêu đề, Đáp án, Đúng/Sai, Độ khó. |

### 🎯 Epic 3: Bài thi & Thi trực tuyến (Exam Engine)
*Xử lý quy trình thi và tính năng Real-time.*

| ID | User Story | Priority | Trạng thái | Acceptance Criteria (AC) |
| :--- | :--- | :---: | :---: | :--- |
| **US29** | **Thiết lập bài thi** | P0 | 📝 To Do | - Tên (Unique), Số lượng câu, Loại đề, Thời gian làm bài, Điểm đạt. |
| **US53** | **Cấu hình Trộn đề (Shuffle)** | P1 | 📝 To Do | - Option: Trộn thứ tự câu hỏi.<br>- Option: Trộn thứ tự các đáp án trong mỗi câu. |
| **US54** | **Phát hiện gian lận (Tab Switch)** | P2 | 📝 To Do | - Ghi nhận số lần học viên rời khỏi tab bài thi.<br>- Tự động nộp bài hoặc cảnh báo nếu vượt quá số lần cho phép. |
| **US32** | **Xem lịch sử làm bài (GV)** | P1 | 📝 To Do | - Thống kê: Danh sách học viên, Thời gian nộp, Điểm, Số câu đúng/sai. |
| **US55** | **Báo cáo phân tích câu hỏi** | P2 | 📝 To Do | - GV xem được tỉ lệ chọn từng đáp án của học viên.<br>- Hệ thống đánh dấu các câu hỏi có tỉ lệ sai > 70%. |
| **US33** | **Dashboard học viên** | P0 | 📝 To Do | - Hiển thị bài thi theo danh mục.<br>- Mục "Hot nhất": Dựa trên số lượt tham gia. |
| **US36** | **Thực hiện bài thi** | P0 | 📝 To Do | - Giao diện: Countdown timer, Nav câu hỏi, Nút Nộp bài. |
| **US37** | **Kết quả tức thì** | P0 | 📝 To Do | - Hiển thị Điểm, Đúng/Sai ngay sau khi nộp. |
| **US38** | **Lịch sử thi cá nhân** | P1 | 📝 To Do | - Danh sách bài đã làm (Mới nhất lên đầu). |
| **US40** | **Tạo phòng thi Online** | P1 | 📝 To Do | - Cài đặt số người tối đa.<br>- Sinh mã tham dự: Link, 6 số, QR Code. |
| **US41** | **Quản lý phòng chờ** | P1 | 📝 To Do | - GV điều khiển nút "Bắt đầu".<br>- Hiển thị Avatar những người đang chờ. |
| **US43** | **Tham gia thi Online** | P1 | 📝 To Do | - Nhập mã Code/Quét QR để vào phòng chờ. |
| **US45** | **Bảng xếp hạng (Leaderboard)** | P1 | 📝 To Do | - Real-time leaderboard sau khi bài thi Online kết thúc. |
| **US50** | **Thông báo thời gian thực** | P2 | 📝 To Do | - Thông báo GV khi có học viên ra/vào phòng thi. |

---
*Cập nhật lần cuối: 2026-05-02*
*Bởi: Senior Product Owner Agent*
