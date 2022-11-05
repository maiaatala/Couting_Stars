import cv2
import os
from dotenv import load_dotenv
import app

load_dotenv()

# OPENCV:  BLUE GREEN RED
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)
RED = (0, 0, 255, 255)


class Error(Exception):
    """Base error Class"""

    pass


class ImageNotFound(Error):
    """Raised when the image to be processed is not found"""

    pass


if __name__ == "__main__":
    try:
        ORIGINAL_PIC = os.getenv("ORIGINAL_PIC")
        STARS_ONLY_PIC = os.getenv("STARS_ONLY_PIC")
        METEORS_ONLY_PIC = os.getenv("METEORS_ONLY_PIC")
        DOTS_ONLY_PIC = os.getenv("DOTS_ONLY_PIC")
        LOW_ALPHA_ONLY_PIC = os.getenv("LOW_ALPHA_ONLY_PIC")

        if ORIGINAL_PIC is None:
            raise ImageNotFound
        picture = cv2.imread(ORIGINAL_PIC, -1)
        if picture is None:
            raise ImageNotFound

        starCount = app.countStars(picture, STARS_ONLY_PIC)
        meteorCount, horizontalMeteors = app.countMeteors(
            cv2.imread(ORIGINAL_PIC, -1), METEORS_ONLY_PIC
        )
        app.dotsOnly(cv2.imread(ORIGINAL_PIC, -1), DOTS_ONLY_PIC)
        app.zeroAplhaOnly(cv2.imread(ORIGINAL_PIC, -1), LOW_ALPHA_ONLY_PIC)

        # print(starCount, meteorCount, horizontalMeteor)
        print(f"Number of Stars in the Sky: {starCount}")
        print(f"Number of Meteors in the Sky: {meteorCount}")
        print(
            f"Number of Meteros that will probably fall in the water: {meteorCount-horizontalMeteors}"
        )
        # didn't work
        # print("Hiddent Text: ", app.readingTest(cv2.imread(DOTS_ONLY_PIC)))
        # print("Hiddent Text: ", app.readingTest(cv2.imread(LOW_ALPHA_ONLY_PIC)))

    except ImageNotFound:
        print(
            "Image wasn't found,\nmake sure the image is at: ",
            os.getenv("ORIGINAL_PIC"),
        )
        print("or check .env file")
    except Exception as e:
        print("an error occurred, message ana.atala@unemat.br")
        print(e)
