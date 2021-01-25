import cv2 as cv


def detectImages(imgPath):

    original_img = cv.imread(imgPath)

    grayscale_img = cv.cvtColor(original_img, cv.COLOR_BGR2GRAY)

    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_alt.xml')

    detected_faces = face_cascade.detectMultiScale(grayscale_img)

    for (column, row, width, height) in detected_faces:
        cv.rectangle(
            original_img,
            (column, row),
            (column + width, row + height),
            (0, 255, 0),
            2
        )

    cv.imshow('Image', original_img)
    cv.waitKey(0)
    cv.destroyAllWindows()


imgPath = R"/image-to-path/.jpg"
detectImages(imgPath)
