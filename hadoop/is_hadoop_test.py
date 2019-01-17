with open("/Users/jiang/Downloads/S-BASE.log","r",encoding="utf8") as fs:
    msg_id = ""
    myLine = ""
    lastCln = ""
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
        print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s"%(lineMap["MsgId"],lineMap["dt"],lineMap.get("type") if lineMap.get("type") is not None else "-",lineMap.get("perMsgId") if lineMap.get("perMsgId") is not None else "-",lineMap.get("message") if lineMap.get("message") is not None else "-",lineMap.get("method") if lineMap.get("method") is not None else "-",lineMap.get("sql") if lineMap.get("sql") is not None else "-", lineMap.get("exec") if lineMap.get("exec") is not None else "-"))