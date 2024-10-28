import cv2

# 동영상 파일 열기
cap = cv2.VideoCapture("lion.mp4")
edge_bool = False
gray_bool = False
rotate_bool= False
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # 그레이스케일 변환
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Canny edge detection 적용
    edges = cv2.Canny(image=gray_img, threshold1=100, threshold2=200)

    if edge_bool:
        image = edges
    else:
        image = frame
        if gray_bool:
            image=gray_img
        else:
            image=frame
    height, width = frame.shape[:2]
    center = (width / 2, height / 2)
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=90, scale=1)
    rotated_img = cv2.warpAffine(src=frame, M=rotate_matrix, dsize=(width, height))
    if rotate_bool:
        image= rotated_img
        
    
    cv2.imshow("Video", image)
    key = cv2.waitKey(10)
    if key == ord("q"):break
    elif key == ord("b"):
        edge_bool = not edge_bool
    elif key == ord("g"):
        gray_bool= not gray_bool
    elif key == ord("r"):
        rotate_bool= not rotate_bool



# 외부 자원은 반환
cap.release()
cv2.destroyAllWindows()



# 작업 완료 후 해제
cap.release()
# out.release()
cv2.destroyAllWindows()