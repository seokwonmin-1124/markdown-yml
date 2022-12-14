from datetime import datetime

def createTopic(setFileName, topic):
    with open(f"./test/{setFileName}") as f: # 여기선 파일을 로컬 경로에서 찾지만 웹상에선 inpt 값을 바로 받아와서 실행시킬 예정
        set = f.readlines()[0:5]
        set = [x.strip() for x in set]
        f.close()

        result = convertSet(set)
    
    f = open(f"./test/{result['title']}_{result['date']}.txt", "w")
    f.write(f"{result}\n{topic}")
    f.close()

    return set


def convertSet(set):
    _set = {
        "title": set[1],
        "date": set[2],
        "opt": set[3],
    }

    _set["title"] = set[1][10:-2].replace(" ", "-")
    _set["opt"] = set[3][8:-1]
    _set["date"] = checkOpt(_set)

    return _set


def checkOpt(set):
    opt = set["opt"]

    if opt == "ymd":
        return str(datetime.now())[0:10]

    elif opt == "ymdhm":
        return str(datetime.now())[0:16].replace(" ", "(") + ")"

    elif opt == "ymdhms":
        return str(datetime.now())[0:19].replace(" ", "(") + ")"

    else:
        print(opt)
        return False

topic = "글 내용"
createTopic('test.md', topic)