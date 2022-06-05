import requests, hgtk, random

#이미 있는 단어 알기위해 단어목록 저장
history = []
playing = True

#키 발급은 https://krdict.korean.go.kr/openApi/openApiInfo
apikey = '92C86E68D846EBC1DA3DE4EF202675F6'

first_word_list = ['바보', '개발', '개발자', '군인', '얼굴', '조개', '향수']



def get_start_word() -> "":
    return random.choice(first_word_list)



# 지정한 두 개의 문자열 사이의 문자열을 리턴하는 함수
# string list에서 단어, 품사와 같은 요소들을 추출할때 사용됩니다
def midReturn(val, s, e):
    if s in val:
        val = val[val.find(s) + len(s):]
        if e in val: val = val[:val.find(e)]
    return val


# 지정한 두 개의 문자열 사이의 문자열 여러개를 리턴하는 함수
# string에서 XML 등의 요소를 분석할때 사용됩니다
def midReturn_all(val, s, e):
    if s in val:
        tmp = val.split(s)
        val = []
        for i in range(0, len(tmp)):
            if e in tmp[i]: val.append(tmp[i][:tmp[i].find(e)])
    else:
        val = []
    return val


def findword(query):
    url = 'https://krdict.korean.go.kr/api/search?key=' + apikey + '&part=word&pos=1&q=' + query
    response = requests.get(url)
    ans = []

    # 단어 목록을 불러오기
    words = midReturn_all(response.text, '<item>', '</item>')
    for w in words:
        # 이미 쓴 단어가 아닐때
        if not (w in history):
            # 한글자가 아니고 품사가 명사일때
            word = midReturn(w, '<word>', '</word>')
            pos = midReturn(w, '<pos>', '</pos>')
            if len(word) > 1 and pos == '명사' and not word in history and not word[len(word) - 1] in blacklist:
                ans.append(w)
    if len(ans) > 0:
        return random.choice(ans)
    else:
        return ''

def checkexists(query):
    url = 'https://krdict.korean.go.kr/api/search?key=' + apikey + '&part=word&sort=popular&num=100&pos=1&q=' + query
    response = requests.get(url)
    ans = ''

    #단어 목록을 불러오기
    words = midReturn_all(response.text,'<item>','</item>')
    for w in words:
        #이미 쓴 단어가 아닐때
        if not (w in history):
            #한글자가 아니고 품사가 명사일때
            word = midReturn(w,'<word>','</word>')
            pos = midReturn(w,'<pos>','</pos>')
            if len(word) > 1 and pos == '명사' and word == query: ans = w

    if len(ans)>0:
        return ans
    else:
        return ''