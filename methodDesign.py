previousSlides = []

def gatherPrevious(amount, direction):
    amount = int(amount)
    while amount != 0:
        previousSlides.append(slide(selection, direction, amount, img))
        print "appended ", amount
        amount  -1
