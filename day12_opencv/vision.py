import cv2

# 이미지 읽기
img = cv2.imread('a.webp')

# 그레이스케일 변환
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Canny edge detection 적용
edges = cv2.Canny(image=gray_img, threshold1=100, threshold2=200)
# 경계가 감지된 이미지 표시
cv2.imshow('Edge Detected Image', edges)
cv2.imshow('Image', img) # 화면 열고
cv2.waitKey(0)
cv2.destroyAllWindows()

# 이미지 저장
# cv2.imwrite('output.jpg', img)
