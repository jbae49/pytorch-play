from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

img = Image.open("training_images/img_1.jpg")
img_arr = np.array(img)


def parse_localization(loc_path):
    boxes = []
    file_names = [os.path.join(loc_path, f) for f in os.listdir(loc_path)]
    for f in file_names:
        img = "img_" + str(f.split("_")[-1].split(".")[0]) + ".jpg"
        img = os.path.join(img_path, img)
        file = open(f, encoding="utf-8-sig").read()
        data = file.strip().split("\n")
        for line in data:
            part = line.split(",")
            label = part[-1]
            if label == "###" or len(label) == 0:
                pass
            else:
                if len(part) == 9:
                    coords = list(map(int, part[:8]))
                    x, y, w, h = (
                        coords[0],
                        coords[1],
                        coords[2] - coords[0],
                        coords[-1] - coords[1],
                    )
                    # print((x, y, w, h))
                cropped_img = np.array(Image.open(img))[y : y + h, x : x + w]
                cropped_img = Image.fromarray(cropped_img)
                if "/" in label:
                    label = label.replace("/", "{slash}")
                    print(label)
                img_name = label + ".jpg"

                cropped_img.save(os.path.join("cropped_images", img_name))
                # plt.imshow(cropped_img)
                # plt.show()
                # print((coords, label))

    return boxes


loc_path = "localization"
img_path = "training_images"
boxes = parse_localization(loc_path)
