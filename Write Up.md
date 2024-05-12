## Giải này mình join hơi muộn nên chỉ kịp làm được 1 bài misc 

Đề: ![enter image description here](a)

Nhìn vào hình mình thấy có những pixel sắp xếp lộn xộn nên thử lấy mã màu của từng pixel ra xem như thế nào( vì mã RGB là decimal nên mình đã convert sang hex để so sánh với file signature)

Code:  [Xem ở đây](a)

![image](https://github.com/NguyenCongHaiNam/Write-Up-KCSC-CTF-2024/assets/116544941/e510440b-0da2-4d07-b128-07f6e91c6219)

![image](https://github.com/NguyenCongHaiNam/Write-Up-KCSC-CTF-2024/assets/116544941/2f75cf86-da3f-4fee-ab0e-b0ec009aaf3b)

Đúng như mình dự đoán, đây là một video, ném lên Cyberchef rồi tải về thôi

![image](https://github.com/NguyenCongHaiNam/Write-Up-KCSC-CTF-2024/assets/116544941/6b906ec7-e34d-4c2e-986a-7286452c32e2)

Xem qua video này một lượt không thấy có gì thú vị ngoài cái tiêu đề là hint của author

![image](https://github.com/NguyenCongHaiNam/Write-Up-KCSC-CTF-2024/assets/116544941/246dcfb7-6266-4772-914c-04f7ca0b1c05)

Tìm trên gg một vòng thì toàn những thông tin vô ích thì mình đã hỏi GPT xem thì đã tìm được thông tin khá thú vị

![image](https://github.com/NguyenCongHaiNam/Write-Up-KCSC-CTF-2024/assets/116544941/f9f453f4-b679-40a8-87cc-2539d8e73da3)

Nếu để ý kĩ thì ta thấy video pixel kia có sự thay đổi màu rất ít và không có yếu tố `chỉ với hai trạng thái` trừ cái bóng đèn trên đỉnh tháp ( lười chụp quá nên mọi người tự extract video để xem nhé, nó là cái bóng đèn nháy vàng trên đỉnh tháp ). Vậy là đã khá rõ ý đồ của author, và đây là cách mình giải quyết bài này.

(mình lười chụp ảnh lắm rồi nên mọi người chịu khó tưởng tượng nhé :((( )
Đầu tiên, mình ném file .webm này lên một web bất kì cho phép chỉnh sửa định dạng file này rồi zoom to ra để trích xuất màu có vẻ là vàng ở trên bóng đèn, nhưng vấn đề xảy ra khi độ phân giải của video bị kém đi khi zoom lên nên màu không chính xác. Nhưng mà nhận thấy màu G=226 không thay đổi nên mình đã lấy toàn bộ RGB của frame đầu ra rồi tìm thử thì đã thấy mã màu của bóng đèn kia.

![image](https://github.com/NguyenCongHaiNam/Write-Up-KCSC-CTF-2024/assets/116544941/8b2807a8-dc0c-46ca-89b3-475a4b5983b5)

4 pixel màu vàng ở giữa một đống màu khác thì có vẻ là chuẩn rồi, mình nhớ vị trí của những pixel này rồi thử extract màu của pixel này trong 10 frame đầu thì 

![image](https://github.com/NguyenCongHaiNam/Write-Up-KCSC-CTF-2024/assets/116544941/9e0452a0-6ff9-4399-92c5-96c3d63178ca)

**PWN**, tới đây thì đã rõ, bây giờ chỉ cần đọc từng frame rồi đánh đấu màu vàng là 0 còn trắng là 1 thì ta được flag...

![image](https://github.com/NguyenCongHaiNam/Write-Up-KCSC-CTF-2024/assets/116544941/dd8cbf29-eac0-47dd-a318-a34855698fd7)
![image](https://github.com/NguyenCongHaiNam/Write-Up-KCSC-CTF-2024/assets/116544941/39aa3c42-14e9-4a52-bb0d-f3487147b62d)
![image](https://github.com/NguyenCongHaiNam/Write-Up-KCSC-CTF-2024/assets/116544941/7ba263e4-a2ae-4c02-b0c4-a5fcda79d2c4)

PS: ở đây mình bị sai một bit mà không rõ vì sao :((( Tiếc là khi mình giải xong thì vừa hết giờ :( mn thấy hay thì cho mình xin một star để lấy cái huy hiệu của github nhé. Thank guys!




