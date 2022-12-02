hossz = 15

def disz(minta, db):
    print(minta * db)


def hello():
    szoveg = "hello"
    disz("-", hossz)
    print(f"{szoveg:^{hossz}}")
    disz("-", hossz)