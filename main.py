import cv2
import os
from dotenv import load_dotenv
import app
from icecream import ic


class Error(Exception):
    """Base error Class"""

    pass


class ImageNotFound(Error):
    """Raised when the image to be processed is not found"""

    pass


if __name__ == "__main__":
    try:
        load_dotenv()
        ORIGINAL_PIC = os.getenv("ORIGINAL_PIC")
        STARS_ONLY_PIC = os.getenv("STARS_ONLY_PIC")
        METEORS_AND_RIVER_PIC = os.getenv("METEORS_AND_RIVER_PIC")

        if ORIGINAL_PIC is None:
            raise ImageNotFound
        picture = cv2.imread(ORIGINAL_PIC, -1)
        if picture is None:
            raise ImageNotFound

        starCount = app.countStars(picture, STARS_ONLY_PIC)

        meteorCount, overWater = app.countMeteorsAndWaterMeteors(
            cv2.imread(ORIGINAL_PIC, -1), METEORS_AND_RIVER_PIC
        )

        print(
            """ 
            +------------------------------+-------+
            | Number of Stars              |  %i  |
            | Number of Meteors            |  %i  |
            | Meteors falling on the Water |  %i  |
            | Hidden Phrase                |  %s  |
            +------------------------------+-------+
        """
            % (starCount, meteorCount, overWater, "n/a")
        )

    except ImageNotFound:
        print(
            "Image wasn't found,\nmake sure the image is at: ",
            os.getenv("ORIGINAL_PIC"),
        )
        print("or check .env file")
    except Exception as e:
        print("an error occurred, message ana.atala@unemat.br")
        print(e)
