# import textq
# from PIL import Image
#
# im = Image.open("/home/ab/mrtest/negexamples/001.jpg")
# q = textq.TextQuerier(im, textq.engines.PaddleOCREngine())
# q.run()

# # https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.1/doc/doc_en/whl_en.md#21-use-by-code
# # import time
# # from PIL import Image, ImageDraw
# # from paddleocr import PaddleOCR
# # ocr = PaddleOCR(use_angle_cls=False, lang='en')  # need to run only once to download and load model into memory
# # time_initial = time.time()
# # img_path = 'res/test.jpg'
# # result = ocr.ocr(img_path, cls=False, rec=True)
# # for line in result:
# #     print(line)
# # print(time.time() - time_initial)
# #
# # im = Image.open(img_path)
# # draw = ImageDraw.Draw(im)
# # for line in result:
# #     draw.polygon([tuple(x) for x in line])
# # im.show()

import textq
c = textq.correctors.WordNinjaCorrector()
corrected = c.correct("helloiwouldlike to vgive you the highest pp i can give")
print(corrected)