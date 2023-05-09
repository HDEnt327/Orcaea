from PIL import Image
import json
import sys


def getScreenRatio(img: Image):
    return 1.0 * img.width / img.height

def getPositions(img: Image):
    ratio = getScreenRatio(img)
    min = sys.maxsize
    pos = None
    with open('screens.json', 'r+') as p:
        positions = json.load(p)
        for position in positions['screens']:
            diff = position['ratio'] - ratio
            if abs(diff) < min:
                min = diff
                pos = position
    return pos
        

# Returns an array of positions
def getNamePosition(img: Image):
    return getPositions(img)['NamePos']


def getScorePosition(img: Image):
    return getPositions(img)['ScorePos']
  
        
def getDiffPosition(img: Image):
    return getPositions(img)['DiffPos']
        
