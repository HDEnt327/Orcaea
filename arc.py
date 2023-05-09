from PIL import Image
import pytesseract
import json
import positions
import tracemalloc

class arc:

    name = ''
    score = 0
    diff = ''
    ptt = 0.0
    songid = ''
    const = 0.0
    img = None
    
    def __init__(self, img: Image):
        self.img = img
        self.img = self.img.convert("L")
        self.songid = self.getSong(self.img)
        self.name = self.getName(self.songid)
        self.score = self.findScore(self.img)
        self.diff = self.findDiff(self.img)
        self.const = self.getConst(self.songid, self.diff)
        self.ptt = self.calcPtt(self.score, self.const)

    def findName(self, img: Image):
        pos = positions.getNamePosition(img)
        cropped_n = img.crop((0, img.height/pos[1], img.width, img.height/pos[3]))
        cropped_n.save("name_out.png")
        name = pytesseract.image_to_string(cropped_n)
        name = name.strip('\n')
        return name
    
    def findScore(self, img: Image):
        pos = positions.getScorePosition(img)
        cropped_s = img.crop((img.width/pos[0], int(img.height/pos[1]), img.width/pos[2], int(img.height/pos[3])))
        cropped_s.save("score_out.png")
        score = pytesseract.image_to_string(cropped_s)
        score_n = ''.join([i for i in score if i.isdigit()])
        score_n = int(score_n)
        return score_n

    def findDiff(self, img: Image):
        pos = positions.getDiffPosition(img)
        cropped_d = img.crop((0, img.height/pos[1], img.width/pos[2], img.height/pos[3]))
        cropped_d.save("diff_out.png")
        diff = pytesseract.image_to_string(cropped_d)
        diff = ''.join([i for i in diff if not i.isdigit()])
        diff = diff.strip('\n')
        diff = diff.strip(' ')
        return diff
    
    def getSong(self, img: Image):
        name = arc.findName(self, img)
        counter = 0
        max = 0
        songid = ''
        with open('songs.json', 'r+') as s:
            songs = json.load(s)
            for song in songs['songs']:
                for i in range (len(name)):
                    if name[i:i+1] == song['title_localized']['en'][i:i+1]:
                        counter = counter + 1
                    else:
                        break
                if counter > max:
                    max = counter
                    songid = song['id']
                counter = 0
        return songid

    def getConst(self, songid: str, diff: str):
        with open('const.json', 'r+') as c:
            constlist = json.load(c)
            if diff == 'Past':
                index = 0
            if diff == 'Present':
                index = 1
            if diff == 'Future':
                index = 2
            if diff == 'Beyond':
                index = 3
            return constlist[songid][index]['constant']
        
    def getName(self, songid: str):
        with open('songs.json', 'r+') as s:
            songs = json.load(s)
            for song in songs['songs']:
                if song['id'] == songid:
                    return song['title_localized']['en']
        
    def calcPtt(self, score: int, const: float):
        if score >= 10000000:
            return const + 2
        if score >= 9800000:
            return const + 1 + (score - 9800000) / 200000
        else:
            return const + (score - 9500000) / 300000

