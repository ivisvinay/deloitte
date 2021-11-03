import cv2
orb = cv2.ORB_create()
img1 = cv2.imread("lena_left.jpg")
img2 = cv2.imread("lena_right.jpg")
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)
firstTen = matches[:10]
similar = 0
for i in firstTen:
    similar = similar + i.distance
    similar = similar/10
print("similar = ", similar)

output = cv2.drawMatches(img1, kp1, img2, kp2, matches[: 10], img2, flags=2)
cv2.imwrite("output.jpg", output)
cv2.imshow("matches", output)
cv2.waitKey(0)