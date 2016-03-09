import sys
def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h","--help"}:
        print("usage : {0} file1 [file2 [...fileN]]".format(
            sys.argv[0]
        ))
        sys.exit()
    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        for line in open("MetaType.py",encoding="utf8"):
            line = line.rstrip()
            if line:
                user = process_line(line,usernames)
                users[(user.surname.lower(),user.forename.lower(),user.id)]=user
    print_users(users)