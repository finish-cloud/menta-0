name = ["たんじろう", "ぎゆう", "ねずこ", "むざん"]

name.append("ぜんいつ")


def test(hikisuu):
    if hikisuu in name:
        print(hikisuu + "は含まれます")


test("いのすけ")
test("ぎゆう")
