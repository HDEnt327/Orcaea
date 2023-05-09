from PIL import Image
import positions
import arc

img = Image.open('screentests/iPad5.PNG')
img = img.convert("L")
ratio = positions.getScreenRatio(img)
name = arc.findName(img)
score = arc.findScore(img)
diff = arc.findDiff(img)

print(ratio)
print(name)
print(score)
print(diff)
print(positions.getNamePosition(img)[1])