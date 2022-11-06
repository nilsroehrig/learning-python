import cv2

img = cv2.imread("../materials/galaxy.jpg", 0)

print(img)
print(type(img))
print(img.shape)
print(img.ndim)

resized_image=cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
cv2.imwrite("../materials/Galaxy_resized.jpg", resized_image)
cv2.imshow("Galaxy", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()