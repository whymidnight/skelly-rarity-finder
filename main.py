import imageio
import cv2
import numpy as np

def main():
    gif = imageio.mimread("./skelly.gif")
    imgs = [cv2.resize(img, (56,56), interpolation = cv2.INTER_AREA) for img in gif]
    imgs = [cv2.cvtColor(imgs[0], cv2.COLOR_BGR2RGB)]

    for skelly in imgs:
        img = cv2.imread('./rarity.jpeg')
        res = cv2.matchTemplate(img, skelly, cv2.TM_CCOEFF_NORMED)
        _, _, _, max_location = cv2.minMaxLoc(res)
        top_left = max_location
        height, width, channels = skelly.shape
        bottom_right = (top_left[0]+width, top_left[1]+height+40)

        cv2.rectangle(img, top_left, bottom_right, (255, 0, 255), 12)

        cv2.imwrite(f'result.png', img)
        print(f'wrote result.png')

if __name__ == "__main__":
    main()
