def except_test(n):
    try:
        print(10/n)
    except Exception as e:
        print(e)

except_test(0)