from CodernityDB3.database import Database


def main():
    db = Database('/tmp/tut1')
    db.create()
    for x in range(100):
        print(db.insert(dict(x=x)))
    for curr in db.all('id'):
        print(curr)

main()
