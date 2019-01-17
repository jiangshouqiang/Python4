jsonObj = set()
with open("/Users/jiang/Documents/learn/log.log","r",encoding="utf8") as fs:
    msg_id = ""
    myLine = ""
    lastCln = ""
    column = 0
    for context in fs:
        column = column + 1
        if context.find("MsgId") > 0:
            lineMap = {}
            if lastCln is not '':
                # lineMap["MsgId"] = msg_id
                # lineMap["lastCln"] = lastCln
                print(msg_id + "\t-" + "\t-" + "\t-" + "\t-" + "\t-" + "\t-" + lastCln)

            lastCln = ""
            context = context.replace(" INFO  - ","\t").replace("] [","\t").replace("] - ","\t").replace(" - ","\t").replace("], ","]\t")
            obj_content = context.split("\t")

            i = 0
            for col in obj_content:
                if i == 0:
                    lineMap["dt"] = col

                if col.find("MsgId[") >= 0:
                    lineMap["MsgId"] = col.replace("MsgId[","").replace("]","")
                    msg_id = col.replace("MsgId[","").replace("]","")

                if col.find("perMsgId") >= 0:
                    lineMap["perMsgId"] = col.replace("perMsgId=[","").replace("]","")

                if i == 2:
                    lineMap["type"] = col

                if col.find("method") >= 0:
                    lineMap["method"] = col.replace("method=[","").replace("]","")

                if col.find("message") >= 0:
                    lineMap["message"] = col.replace("message=[","").replace("]","")

                if col.find("sql") >= 0:
                    lineMap["sql"] = col.replace("sql=[","").replace("]","")

                if col.find("exec") >= 0:
                    lineMap["exec"] = col.replace("exec ","")
                i = i + 1
        else :
            lastCln = lastCln + context + "\n"
            continue
        jsonObj.add(lineMap.get("message"))

import json
import pymysql

conn = pymysql.connect(host='192.168.11.193',user='hibabyadm',password='hibaby@)!&',database='hibaby_sit')
cursor = conn.cursor()

for x in jsonObj :
    xx = json.loads(x)
    cursor.execute('insert into hk_pay_info (apply_id,hk_merid,amount,trade_date) values(%s,%s,%s,%s)',[xx["SignData"]["OutOrderNo"],xx["SignData"]["HKMerchNo"],xx["SignData"]["Amount"],xx["SignData"]["TransDate"]])
    conn.commit()
cursor.close()



from datetime import datetime,timedelta,timezone


#
# for i in range(1000,9000):
#     now = datetime.now()
#     timeStr = datetime.strftime(now,'%Y%m%d%H%M%S%s')
#     id = timeStr[:-8]+ str(i)
#     cursor.execute('insert into pay_refund_no (pay_no,refund_no) values(%s,%s)',['P'+id,'R'+id])
#     print("running ... ")
#     conn.commit()
# cursor.close()

        # print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s"%(lineMap["MsgId"],lineMap["dt"],lineMap.get("type") if lineMap.get("type") is not None else "-",lineMap.get("perMsgId") if lineMap.get("perMsgId") is not None else "-",lineMap.get("message") if lineMap.get("message") is not None else "-",lineMap.get("method") if lineMap.get("method") is not None else "-",lineMap.get("sql") if lineMap.get("sql") is not None else "-", lineMap.get("exec") if lineMap.get("exec") is not None else "-"))