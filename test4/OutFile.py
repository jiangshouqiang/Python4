#Python write context to a file
import os
def main():
    filename = input("Choose filename:")
    if not filename:
        filename = "defult"
    count = 0
    content = ""
    if os.path.exists(filename+".lst"):
        fh_tmp = open(filename+".lst","rU")
        count = len(fh_tmp.readlines())
        fh_tmp.close()
    while True:
        select = input("[A]dd [Q]uit [a]:")
        if not select:
            continue
        if "Q" == select or "q" == select:
            break
        if "a" == select or "A" == select:
            count += 1
            contents = input("Add item:")
            content += str(count)+":"+contents+"\n"
        if "s" == select or "S" == select:
            fh = open(filename+".lst","a",encoding="utf8")
            fh.write(content)
            fh.close()
main()