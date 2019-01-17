import os,xlwt

home_dir="/Users/jiang/Documents/work/web/"
projects=('hibaby',)

version = version=input("请输入版本号（如CR00114）:")
# 实体
class JsxObject(object):
    def __init__(self,note,fileName,mrange,projectName):
        self.note = note
        self.fileName = fileName
        self.mrange = mrange
        self.projectName = projectName

jsxObjects = []
jsxs = []

for project in projects:
    files = os.popen("find " + home_dir+project + " -name *jsx | xargs grep " + version).readlines()
    jsxObject = JsxObject("","",[],"")
    for file in files:
        tmp = file.split(":")
        fileName = tmp[0].strip()
        note = tmp[1].strip()
        if jsxs.count(fileName) > 0:
            continue
        jsxs.append(fileName)
        jsxObject.note = note
        jsxObject.fileName = fileName
        jsxObject.projectName = project
        jsxObjects.append(jsxObject)
        jsxObject = JsxObject("","",[],"")

for jsx in jsxObjects:
    importName = jsx.fileName.split('/')[-1].replace('.jsx','')
    files = os.popen("find " + home_dir+project + " -name *jsx | xargs grep 'import " + importName +"'").readlines()
    mrange = []
    for file in files:
        fileName = file.split(":")[0].strip()
        if mrange.count(fileName) > 0:
            continue
        mrange.append(fileName)
    jsx.mrange = mrange

    # print(jsx.note,jsx.fileName,jsx.projectName)


# 实体
class JsMethodObject(object):
    def __init__(self,note,fileName,methodName,mrange,projectName):
        self.note = note
        self.fileName = fileName
        self.mrange = mrange
        self.projectName = projectName
        self.methodName = methodName

jsMethodObjects = []
for project in projects:
    files = os.popen("grep -r " + version + " " + home_dir+project+"/src/utils").readlines()
    jsMethodObject = JsMethodObject("","","",[],"")
    for file in files:
        tmp = file.split(":")
        fileName = tmp[0].strip()
        note = tmp[1].strip().replace("\n","")

        jsMethodObject.note = note
        jsMethodObject.fileName = fileName
        jsMethodObject.projectName = project
        with open(fileName) as f:
            contents = f.readlines()
            isFlag = False
            for content in contents:
                if isFlag:
                    if content.count('(') > -1:
                        methodName = content.strip().split("(")[0]
                        importName = fileName.strip().split("/")[-1].replace(".js","")
                        if importName == "util" :
                            jsMethodObject.methodName = importName+"."+methodName
                        if importName == "comm" :
                            jsMethodObject.methodName = "new Comm(this.props)."+methodName
                        jsMethodObjects.append(jsMethodObject)
                        isFlag = False
                        jsMethodObject = JsMethodObject("","","",[],"")
                        break
                if content.strip().replace("\n","")==note:
                    isFlag = True

class Mrange(object):
    def __init__(self,fileName,num):
        self.fileName = fileName
        self.num = num


for js in jsMethodObjects:
    # print(js.note,js.fileName,js.methodName,js.projectName)
    methodName = js.methodName
    files = os.popen("grep -r '" + methodName + "(' " + home_dir+js.projectName)
    mrange = Mrange("",[])
    tmpFiles = []

    mranges = []
    for file in files:
        tmp = file.split(":")
        tmpFile = tmp[0].strip()
        tmpContent = tmp[1].strip()
        isFlag = False
        if tmpFiles.count(tmpFile) > 0:
            mrange = mranges[tmpFiles.index(tmpFile)]
            num = mrange.num
            isFlag = True
        else:
            tmpFiles.append(tmpFile)
            num = []
            mrange.fileName = tmpFile

        with open(tmpFile) as f:
            contents = f.readlines()
            i = 0
            for content in contents:
                i = i + 1
                if content.find(tmpContent) > -1:
                    if num.count(i) > 0:
                        continue
                    num.append(i)
                    mrange.num = num
                    if isFlag is not True:
                        mranges.append(mrange)
                    mrange = Mrange("",0)
                    isFlag = False
                    break
    js.mrange = mranges

# for js in jsMethodObjects:
#     print(js.note,js.fileName,js.methodName,js.projectName)
#     for mrange in js.mrange:
#         print(mrange.fileName,mrange.num)


# 实体
class CssMethodObject(object):
    def __init__(self,note,className,mrange,projectName,searchName):
        self.note = note
        self.mrange = mrange
        self.projectName = projectName
        self.className = className
        self.searchName = searchName

cssMethodObjects = []
for project in projects:
    with open(home_dir+project+"/src/index.less") as f:
        contents = f.readlines()
        cssMethodObject = CssMethodObject("","",[],"","")
        isFlag = False
        for content in contents:
            content = content.strip()
            if content.find(version) > -1:
                cssMethodObject.note = content.replace("\n","")
                isFlag = True
            elif isFlag :
                isOk = False
                if content.startswith('.') and content.startswith(".am-") is False:
                    isOk = True
                elif content.startswith("[data-role="):
                    isOk = True
                if isOk:
                    cssMethodObject.searchName = content.split(".")[1].strip().split(" ")[0].replace("[","").replace("]","")
                    cssMethodObject.className = content.replace("\n","")
                    cssMethodObject.projectName = project
                    cssMethodObjects.append(cssMethodObject)
                    cssMethodObject = CssMethodObject("","",[],"","")
                    isOk = False
                isFlag = False

for css in cssMethodObjects:
    tmpSearchs = []
    searchName = css.searchName
    mranges =[]
    fileNames = []
    if searchName.find("data-role") > 0:
        tmpSearchs.append(searchName.replace("'",'"'))
    else:
        tmpSearchs.append(searchName+"\\\'}")
        tmpSearchs.append(searchName+"\"")
        tmpSearchs.append(searchName+" ")
    # files = os.popen("")
    for tmp in tmpSearchs:
        if tmp.find("'") > -1:
            grepStr = "grep -r \"" + tmp + "\" " + home_dir+project
        else:
            grepStr = "grep -r '" + tmp + "' " + home_dir+project
        files = os.popen(grepStr).readlines()
        for file in files:
            num = []
            tmp = file.replace(":","|",1).split("|")
            if len(tmp) < 2:
                continue
            tmpContent =tmp[1].strip()
            fileName = file.split(":")[0].strip()
            if fileNames.count(fileName) > 0:
                continue
            fileNames.append(fileName)
            if mranges.count(fileName) > 0 or fileName.endswith("src/index.less"):
                continue
            if fileName.endswith(".js") or fileName.endswith(".jsx") or fileName.endswith(".less"):
                with open(fileName) as f:
                    mrange = Mrange("",[])
                    mrange.fileName=fileName
                    contents = f.readlines()
                    i = 0
                    isFlag = False
                    for content in contents:
                        i = i + 1
                        if content.find(tmpContent) > -1:
                            if num.count(i) > 0:
                                continue
                            mrange.num.append(i)
                            if isFlag is not True:
                                mranges.append(mrange)
                            isFlag = True
    css.mrange=mranges

# for css in cssMethodObjects:
#     print(css.searchName,"=====")
#     for mrange in css.mrange:
#         print(mrange.fileName,mrange.num)

# 接口
class CommonObject(object):
    def __init__(self,note,commonName,mrange,projectName,searchName):
        self.note = note
        self.mrange = mrange
        self.projectName = projectName
        self.commonName = commonName
        self.searchName = searchName

commonObjects = []
for project in projects:
    with open(home_dir+project+"/src/models/common.js") as f:
        contents = f.readlines()
        isFlag = False
        commonObject = CommonObject("","",[],"","")
        for content in contents:
            content = content.strip().replace("\n","")
            if content.find(version) > -1:
                isFlag = True
                commonObject.note = content.replace("\n","")
            elif isFlag :
                isOk = False
                if content.startswith('*'):
                    isOk = True
                if isOk:
                    commonObject.searchName = "'common/"+content.split("(")[0].replace("*","")+"'"
                    commonObject.commonName = content.split("(")[0]
                    commonObject.projectName = project
                    commonObjects.append(commonObject)
                    commonObject = CommonObject("","",[],"","")
                    isOk = False
                isFlag = False

for common in commonObjects:
    searchName = common.searchName
    mranges = []
    fileNames = []
    files = os.popen("grep -r \"" + searchName + "\" " + home_dir+project)
    for file in files:
        num = []
        tmp = file.replace(":","|",1).split("|")
        if len(tmp) < 2:
            continue
        fileName = tmp[0].strip()
        tmpContent =tmp[1].strip()
        if fileNames.count(fileName) > 0 :
            continue
        if fileName.endswith(".js") or fileName.endswith(".jsx") or fileName.endswith(".less"):
            fileNames.append(fileName)
            with open(fileName) as f:
                    mrange = Mrange("",[])
                    mrange.fileName=fileName
                    contents = f.readlines()
                    i = 0
                    isFlag = False
                    for content in contents:
                        i = i + 1
                        if content.find(tmpContent) > -1:
                            if num.count(i) > 0:
                                continue
                            mrange.num.append(i)
                            if isFlag is not True:
                                mranges.append(mrange)
                            isFlag = True
    common.mrange = mranges

#jsxObjects，jsMethodObjects，cssMethodObjects，commonObjects
book = xlwt.Workbook(encoding='utf-8')
sheet1 = book.add_sheet("JSX修改评估")
titles=['项目名称','被修改JSX文件','影响jsx文件','更新说明']

for i in range(0,len(titles)):
    sheet1.write(0,i,titles[i])

col = 1
for jsx in jsxObjects :
    # print(method.methodName,method.note)
    for mrange in jsx.mrange:
        sheet1.write(col,0,jsx.projectName)
        sheet1.write(col,1,jsx.fileName.replace(home_dir+css.projectName,""))
        sheet1.write(col,2,mrange.replace(home_dir+css.projectName,""))
        sheet1.write(col,3,jsx.note)

        col = col + 1
for j in range(0,i):
    sheet1.col(j).width=150*60

sheet2 = book.add_sheet("JS修改评估")
titles=['项目名称','被修改JS文件','JS函数名称','受影响文件','行数','更新说明']
for i in range(0,len(titles)):
    sheet2.write(0,i,titles[i])
col = 1
for js in jsMethodObjects:
    for mrange in js.mrange:
        sheet2.write(col,0,js.projectName)
        sheet2.write(col,1,js.fileName.replace(home_dir+css.projectName,""))
        sheet2.write(col,2,js.methodName)
        sheet2.write(col,3,mrange.fileName.replace(home_dir+css.projectName,""))
        numStr = ""
        for num in mrange.num:
            numStr = numStr + str(num) + "，"
        sheet2.write(col,4,numStr[:-1])
        sheet2.write(col,5,js.note)
        col = col + 1

for j in range(0,i):
    sheet2.col(j).width=150*60

sheet3 = book.add_sheet("CSS修改评估")
titles=['项目名称','被修改CSS文件','class名','受影响文件','行数','更新说明']
for i in range(0,len(titles)):
    sheet3.write(0,i,titles[i])
col = 1
for css in cssMethodObjects:
    for mrange in css.mrange:
        sheet3.write(col,0,css.projectName)
        sheet3.write(col,1,"/src/index.less")
        sheet3.write(col,2,css.className.replace("{","").strip())
        sheet3.write(col,3,mrange.fileName.replace(home_dir+css.projectName,""))
        numStr = ""
        for num in mrange.num:
            numStr = numStr + str(num) + "，"
        sheet3.write(col,4,numStr[:-1])
        sheet3.write(col,5,css.note)
        col = col + 1

for j in range(0,i):
    sheet3.col(j).width=150*60

sheet4 = book.add_sheet("接口修改评估")
titles=['项目名称','common文件','接口名','受影响文件','行数','更新说明']
for i in range(0,len(titles)):
    sheet4.write(0,i,titles[i])
col = 1
for common in commonObjects:
    for mrange in common.mrange:
        sheet4.write(col,0,common.projectName)
        sheet4.write(col,1,"/src/models/common.js")
        sheet4.write(col,2,common.commonName)
        sheet4.write(col,3,mrange.fileName.replace(home_dir+css.projectName,""))
        numStr = ""
        for num in mrange.num:
            numStr = numStr + str(num) + "，"
        sheet4.write(col,4,numStr[:-1])
        sheet4.write(col,5,common.note)
        col = col + 1

for j in range(0,i):
    sheet4.col(j).width=150*60

book.save(version+"需求评估.xls")
print("执行完毕")