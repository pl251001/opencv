Import cv2
Import random

num = int(input("number of scantrons: "))
img = cv2.imread()
pt = []
horiDif = 
vertDif = 

for x in range(num):
    scan = img.copy()
    options = [0, 1, 2, 3, 4] 
    answers = random.choices(options, weights=(225, 225, 225, 225, 100), k=30) 
    count = 0
    for y in answers:
        choice = [pt[0] + (horiDif*y), pt[1] + (vertDif*count)]
        count = count + 1
        cv2.circle(scan, choice, radius=10, (0,0,0), thickness = 5)
    cv2.imshow(f"scantron {x+1}", scan)
    cv2.waitKey(5)
