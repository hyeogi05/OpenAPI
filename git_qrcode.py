import qrcode

# GitHub 주소
url = "https://github.com/hyeogi05/OpenAPI"

# QR 코드 생성
qr = qrcode.QRCode(
    version=1,  # 1~40: 숫자가 클수록 복잡한 데이터 가능
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # 오류 정정률: L, M, Q, H
    box_size=10,  # QR코드 내부 박스 크기
    border=4,  # 테두리 여백
)
qr.add_data(url)
qr.make(fit=True)

# 이미지 생성 및 저장
img = qr.make_image(fill_color="black", back_color="white")
img.save("github_qr.png")

print("QR 코드가 github_qr.png로 저장되었습니다.")