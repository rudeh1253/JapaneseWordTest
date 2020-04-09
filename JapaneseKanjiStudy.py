import random
from time import sleep

class Note:  # 단어장 생성 및 불러오기
    def __init__(self, tt):
        self.filet = tt + '.txt'
        self.wordList = []

    def writeList(self, kanji, hiragana, sinifie):  # (self, 한자, 히라가나, 뜻)
        self.wordList.append([kanji, hiragana, sinifie])

    def saveListToNote(self): # wordList의 요소들을 텍스트파일에 저장
        f = open(self.filet, "a", -1, "utf-8")
        for i in self.wordList:
            data = "%s %s %s\n" % (i[0], i[1], i[2])
            f.write(data)
        f.close()
        self.wordList.clear()

    def readNote(self): # 텍스트파일 읽기
        f = open(self.filet, "r", -1, "utf-8")
        line = f.read()
        print(line)
        print()
        f.close()

    def readNoteAndInsertList(self):
        self.wordList.clear()
        f = open(self.filet, "r", -1, "utf-8")
        while True:
            line = f.readline()
            if not line:
                break
            self.wordList.append(line.split())
        f.close()

    def testReady(self):
        self.wordList.clear()
        f = open(self.filet, "r", -1, "utf-8")
        index = 0 # random.shuffle(self.wordList)가 뒤에 오므로 test 이후 정답과 비교를 위해 2차원 리스트에서 내부의 리스트에 인덱스 넘버를 요소로 추가
        while True:
            temp = f.readline()
            if not temp :
                break
            temp = temp.split()
            temp.append(index)
            self.wordList.append(temp)
            index += 1
        random.shuffle(self.wordList)
        f.close()

    def explain(self):
        print("1번을 선택할 경우 wordNote.txt에 관계 없이 프로그램 내부에서 wordList를 작성합니다.\n"
              "작성된 wordList는 2번을 선택하여 wordNote.txt에 저장할 수 있습니다(덮어씌우는 게 아니고 추가)\n")
        print("wordNote.txt를 수정할 경우 다음과 같은 규칙을 따라야 합니다.\n"
              "1. 한 줄은 <한자> <히라가나> <뜻>으로 구성되며 각각 공백(space bar)로 구분됩니다.\n"
              "2. 하나의 단어를 작성하면 엔터를 눌러 줄바꿈을 해야 합니다.\n")
        print("테스트를 하기 전에 wordList에 작성된 것을 저장해야 합니다.\n"
              "그렇지 않으면 wordList에 작성된 것이 소멸됩니다.\n"
              "6번을 선택하여 작성된 wordList를 조회할 수 있습니다.\n")
        print("한자 읽기 테스트는 한자를 보고 히라가나와 뜻을 입력하는 것이고,\n"
              "한자 쓰기 테스트는 히라가나를 보고 한자와 뜻을 입력하는 것입니다.\n"
              "히라가나 또는 뜻이 정답과 완벽히 일치하지 않을 경우 오답으로 처리되기 때문에\n"
              "테스트가 끝난 후 답과 정답을 비교하여 뜻이 맞다고 생각되시면 그거 감안해서 틀랜 개수 계산하세요.\n"
              "동봉된 단어장 문서를 출력하여 외운 다음에 응시하세요.\n")
        print("8번 파일 변경은 단어장 변경입니다.\n")
        print("만든이 : PGD\n")

def test(obj, k, l, m, txt):
    obj.testReady()
    compare = Note(txt)
    compare.readNoteAndInsertList()
    count = 0  # count : 틀린 개수
    for i in obj.wordList:  # test 시작
        print(i[k])
        answer_hirakanji = input("%s : " %m)
        if answer_hirakanji == '0': break
        answer_sinifie = input("뜻 : ")

        if answer_hirakanji != i[l]:
            count += 1
            i.append("incorrect") # 틀린 부분의 리스트 요소에 추가
            i[l] = answer_hirakanji
            if answer_sinifie != i[2]:
                i[2] = answer_sinifie
        elif answer_sinifie != i[2]:
            count += 1
            i.append("incorrect") # 틀린 부분의 리스트 요소에 추가
            i[2] = answer_sinifie
    print("틀린 개수 : %d\n" %count)

    for i in obj.wordList:
        if "incorrect" in i:
            print("입력 : %s %s %s" %(i[0], i[1], i[2]))
            print("정답 : %s %s %s\n" %(compare.wordList[i[3]][0], compare.wordList[i[3]][1], compare.wordList[i[3]][2]))

    obj.wordList.clear()
    del compare

txt = "wordNote"
obj = Note(txt)
finish = False
print("단어장 시작")
sleep(1)

while not finish:  # 루프 시작
    print("1. wordList 작성\n"
          "2. wordList 세이브\n"
          "3. 저장된 텍스트파일 불러서 읽기\n"
          "4. 한자읽기 test\n"
          "5. 한자표기 test\n"
          "6. 작성된 wordList 조회\n"
          "7. 파일 변경\n"
          "8. 끝내기\n"
          "0. 설명")
    select = input()

    if select == '1':
        kanji = input("한자 입력 : ")
        hiragana = input("히라가나 입력 : ")
        sinifie = input("뜻 입력 : ")
        print()
        obj.writeList(kanji, hiragana, sinifie)
    elif select == '2':
        obj.saveListToNote()
    elif select == '3':
        obj.readNote()
    elif select == '4':
        print("::한자 읽기 test 시작::\n"
              "도중에 종료하고 싶다면 한자 or 히라가나 기입란에 숫자 '0'을 입력하십시오")
        test(obj, 0, 1, "히라가나",txt)
    elif select == '5':
        print("::한자 쓰기 test 시작::\n"
              "도중에 종료하고 싶다면 한자 or 히라가나 기입란에 숫자 '0'을 입력하십시오")
        test(obj, 1, 0, "한자", txt)
    elif select == '6':
        for i in obj.wordList:
            for j in i:
                print(j, end=' ')
            print()
    elif select == '7':
        txt = input("파일 이름 : ")
        obj = Note(txt)
    elif select == '8':
        finish = True
    elif select == '0':
        obj.explain()
    else:
        print("보기에 제시된 숫자만 입력하여 선택하세요.\n")
        sleep(1)

print("See You Later~")
sleep(3)
