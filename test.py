print("*getRoomVacant"[:-1])

tmp = []
tmp.append("jiang")
tmp.append("shou")
for t in tmp:
    print("t = ",t)

print(".h-CR00114tac".find("CR00114"))

for str in ".autoLeft ".split("."):
    print(str.strip())
print(".h-tac".startswith('.'))

print(".h-tac".startswith('.'))

test1 = ["jiang","shou","qiang"]
print("count = ",test1.count("qiang"))

print("formService.queryFormRecordHistoryInfoList"=="formService.queryFormRecordHistoryInfoList")

def except_test(n):
    try:
        print(10/n)
    except Exception as e:
        print(e)

line = {'dt': '2018-11-07 17:36:37:111', 'type': 'service-resp', 'perMsgId': 'C.ENT01201811071736375971', 'message': 'OrgInfoRespDto(orgId=bad58237c0864f4a8816071d1a269718, orgName=悠月荟月子会所, limitNum=100, appId=wx73c9a38cb7d9f135, businessMode=1, branchFlag=0, topOrgId=0, provinceId=00, cityId=01, telephone=020-31063146, address=广州市番禺区市桥街东涌路129号, introduction=03, expireDate=Thu Dec 31 00:00:00 CST 2020, expireTime=Thu Jan 01 01:00:00 CST 1970, createTime=Thu Jan 01 12:33:22 CST 1970)', 'MsgId': 'S.BASE01201811071736371894'}
print(line if line.get("method") is not None else "-")