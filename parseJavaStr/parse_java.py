import os,xlwt

home_dir="/Users/jiang/Documents/work/yuezi/"
servicePojects=('hibaby-base-service','hibaby-business-service','hibaby-report-service',)
appProjects=('hibaby-enterprise-app','hibaby-schedule-app','hibaby-consumer-mapp','hibaby-enterprise-web',)
projectMap={'hibaby-enterprise-app':"APP端",'hibaby-schedule-app':"schedule端",'hibaby-consumer-mapp':"微信端",'hibaby-enterprise-web':"PC端",'hibaby-base-service':"base-service端",'hibaby-business-service':"business-service端",'hibaby-report-service':"report-service"}

version=input("请输入版本号（如CR00113）:")

# 实体
class MethodObject(object):
    def __init__(self,note,methodName,mrange,projectName):
        self.note = note
        self.methodName = methodName
        self.mrange = mrange
        self.projectName = projectName

methodObjects=[]

# 获取note+method
for project in servicePojects :
    files = os.popen("find " + home_dir+project + " -name *ServiceImpl.java").readlines()
    for file in files:
        with open(file.replace("\n",""),'r') as f:
            contents = f.readlines()
            fs = f.name.split("/")
            tmp = fs[len(fs)-1].replace("Impl.java","")
            classObject = tmp[0].lower()+tmp[1:]
            isFlag = False
            method = MethodObject("","",[],"")
            for content in contents:
                if content.find(version) > -1:
                    method.note=content.strip()
                    isFlag = True
                if content.find("public") > -1 and isFlag:
                    temp=content.split("(")[0].split(" ")
                    method.methodName=classObject+"."+temp[len(temp)-1]
                    method.projectName=project
                    methodObjects.append(method)
                    method = MethodObject("","",[],"")
                    isFlag = False

class MrangeObject(object):
    def __init__(self,methodName,contellerName,url,projectName,httpMethod):
        self.methodName = methodName
        self.contellerName = contellerName
        self.url = url
        self.projectName = projectName
        self.httpMethod = httpMethod

appMethods=[]
for method in methodObjects:
    mrangeObjects = []
    for project in appProjects:
        files = os.popen("find " + home_dir+project + " -name *ServiceImpl.java").readlines()
        for file in files:
            mrangeObject = MrangeObject("","","","","")
            with open(file.split(":")[0].replace("\n",""),'r') as f:
                contents = f.readlines()
                tempMethodName=""
                content = ""
                isEnd = False
                for line in contents:
                    if line.find("//") > -1 or line.find('/*') > -1 or line.find("/")>-1 or line.find('*')>-1:
                        continue
                    if (line.find(";")>-1 or line.find("}") > -1) or line.find("(") > -1:
                        content=content+line.replace("\n","").strip()
                        isEnd=True
                    else:
                        content = content+line.replace("\n","").strip()
                        continue

                    # if "formService.queryFormRecordHistoryInfoList" == method.methodName.strip():
                    #     print(content)
                    # print(content)
                    if content.find("public") > -1:
                        temp=content.split("(")[0].split(" ")
                        tempMethodName=temp[len(temp)-1]
                    if content.find(method.methodName+"(") > -1:
                        if appMethods.count(tempMethodName+project) > 0:
                            content=""
                            continue
                        appMethods.append(tempMethodName+project)
                        mrangeObject.methodName=tempMethodName
                        mrangeObject.projectName=project
                        mrangeObjects.append(mrangeObject)
                        mrangeObject = MrangeObject("","","","","")
                        # print(method.methodName,"=",content)

                    content=""

    method.mrange=mrangeObjects

# 获取接口详情CR
for method in methodObjects :
    # print(method.methodName,method.note)
    for mrange in method.mrange:
        # print(mrange.projectName)
        files = os.popen("find " + home_dir+mrange.projectName + " -name *Controller.java|xargs grep " + mrange.methodName).readlines()
        for file in files:
            with open(file.split(":")[0],'r') as f:
                contents = f.readlines()
                contellerName = ""
                mapper = ""
                url = ""
                httpMehtod = ""
                for content in contents:
                    if content.find("@RequestMapping(") > -1:
                        if mapper == "":
                            mapper = content.replace('@RequestMapping("',"").replace('")',"")
                    if content.find("@ApiOperation(value =") > -1:
                        tmps = content.split('",')
                        contellerName = tmps[0].replace('@ApiOperation(value = "',"")
                        if len(tmps) > 1:
                            httpMehtod = tmps[1].replace('httpMethod = "','').replace('"',"").replace(")","")
                        else:
                            httpMehtod = "GET"
                    if content.find("@RequestMapping(path = ") > -1:
                        url = content.split(',')[0].replace('@RequestMapping(path = "',"").replace('"',"").replace(")","")
                    if content.find("public") > -1 and content.find(mrange.methodName) > -1:
                        mrange.contellerName=contellerName
                        mrange.url=mapper.strip().replace("\n","")+url.strip()
                        mrange.httpMethod=httpMehtod.strip()


book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet("需求评估")
titles=['项目名称','方法名称','引用项目名称','接口名称','请求类型','链接','更新说明']

for i in range(0,len(titles)):
    sheet.write(0,i,titles[i])

col = 1
for method in methodObjects :
    # print(method.methodName,method.note)
    for mrange in method.mrange:
        sheet.write(col,0,method.projectName)
        sheet.write(col,1,method.methodName)
        sheet.write(col,2,mrange.projectName)
        sheet.write(col,3,mrange.contellerName+"("+mrange.methodName+")")
        sheet.write(col,4,mrange.httpMethod)
        sheet.write(col,5,mrange.url)
        sheet.write(col,6,method.note)
        col = col + 1
for j in range(0,i):
    sheet.col(j).width=150*60
book.save(version+"需求评估.xls")
print("执行完毕")