# 🤝 Hướng dẫn Đóng góp (Team 3-5 người)

Chào mừng bạn gia nhập team! Để dự án chạy trơn tru, chúng ta sẽ tuân theo quy trình sau:

## 1. Quy trình làm việc (Git Flow đơn giản)
- **Main branch**: Luôn ở trạng thái có thể deploy được. Không code trực tiếp vào đây.
- **Develop branch** (nếu có): Nhánh tích hợp các tính năng trước khi lên Main.
- **Feature branches**: Mỗi user story sẽ làm trên 1 nhánh riêng. Đặt tên theo mẫu: `feat/us-01-register`.

## 2. Các bước thực hiện một Task
1. Chọn một Issue trong tab **Issues** (ưu tiên P0).
2. Tự assign cho bản thân và chuyển trạng thái sang `In Progress` trên Project Board.
3. Tạo nhánh từ `main`: `git checkout -b feat/ten-tinh-nang`.
4. Code và commit theo chuẩn **Conventional Commits**:
   - `feat: thêm chức năng đăng ký`
   - `fix: sửa lỗi validation mật khẩu`
5. Push nhánh lên và tạo **Pull Request (PR)**.
6. Tag ít nhất 1 thành viên khác để **Review Code**.
7. Sau khi được Approve, tiến hành Merge vào `main`.

## 3. Tiêu chuẩn Code
- Sử dụng ESLint/Prettier để format code.
- Đặt tên biến/hàm bằng tiếng Anh, rõ nghĩa.
- Viết comment cho các logic phức tạp.

## 4. Liên lạc
- Sử dụng Slack/Discord/Zalo để trao đổi nhanh.
- Các vấn đề quan trọng nên được thảo luận trực tiếp trên Comment của Issue.
