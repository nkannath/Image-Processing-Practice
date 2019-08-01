def searchPattern(roi):
    global x1, x2, y1 ,y2, xAdjust, yAdjust
    newX1 = x1 - xAdjust
    newY1 = y1 - yAdjust
    newX2 = x2 + xAdjust
    newY2 = y2 + yAdjust
    searchArea = image[newY1:newY2, newX1:newX2]
    rows = searchArea.shape[0]
    cols = searchArea.shape[1]
    searchBox = image[y1:y2, x1:x2]
    horSlideDist = (cols/2)/5
    verSlideDist = (row/2)/5

scanSlides = []

def getAmount():
    amount = int(raw_input("Enter how many slides are to occur: "))
    return amount

def determineDirection():
    direction = str(raw_input("Enter direction to slide: "))
    return direction

def collectPrevious(amount, direction):
    amount = getAmount()
    direction = determineDirection()
    if direction == 'right':
        slideDirection = slideRight(i)
    elif direction == 'positive':
        slideDirection = slidePositive(i)
    elif direction == 'negative':
        slideDirection = slideNegative(i)
    i = 1
    while i <= amount:
        scanSlides.append(slideDirection)
        i += 1

histos = []

roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]

templateHist = cv2.calcHist([roi], [0,1], None, [180,256], [0,180,0,256])

def templateCompare(histo1):
    histo = cv2.calcHist([histo1], [0,1], None, [180,256], [0,180,0,256])
    histo2 = templateHist
    correlation = cv2.compareHist(templateHist, histo, cv2.HISTCMP_INTERSECT)
    return correlation

def scan(roi):
    global x1, x2, y1, y2, xAdjust, yAdjust image
    searchArea = image[newY1:newY2, newX1:newX2]
    cols = searchArea.shape[1]
    rows = searchArea.shape[0]
    q1 = searchArea[0:rows/2, cols/2:cols]
    q2 = searchArea[0:rows/2, 0:cols/2]
    q3 = searchArea[rows/2:rows, 0:cols/2]
    q4 = searchArea[rows/2:rows, cols/2:cols]
    start = q2


    histos.append(templateCompare(q2))      # 0
    collectionScan(5, q2, 'right')          # 1-6
    collectionScan(5, q3, 'right')          # 7-12
    collectionScan(5, q2, 'slideNegative')  # 13-17
    collectionScan(5, q3, 'slidePositive')  # 18-22

    def collectionScan(amount, direction):
        i = 1
        while i <= amount:
            if direction == 'right':
                histos.append(templateCompare(slideRight(i)))
                scanSlides.append(slideRight(i))
            elif direction == 'positive':
                histos.append(templateCompare(slidePositive(i)))
                scanSlides.append(slidePositive(i))
            elif direction == 'negative':
                histos.append(templateCompare(slideNegative(i)))
                scanSlides.append(slideNegative(i))
            i += 1


    # NOT SURE HOW TO HANDLE START

    def slidePositive(amount, start):
        moveRight = amount * horSlideDist
        moveUp = amount * verSlideDist
        slidePositive = image[y1-moveUp:y2-moveUp, x1+moveRight:x2+moveRight]

    def slideNegative(amount, start):
        moveLeft = amount * horSlideDist
        moveDown = amount * verSlideDist
        slideNegative = image[y1+moveDown:y2+moveDown, x1-moveLeft:x2-moveLeft]

    def slideRight(amount, start):
        movement = amount*horSlideDist
        slideRight = image[y1:y2, x1+movement:x2:movement]
