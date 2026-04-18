def kesishma(list1, list2):
    return list(set(list1) & set(list2))

def birlashma(list1, list2):
    return list(set(list1) | set(list2))

def farq(list1, list2):
    return list(set(list1) - set(list2))

def asosiy_funktsiya():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    print("List 1: ", list1)
    print("List 2: ", list2)
    print("Kesishma: ", kesishma(list1, list2))
    print("Birlashma: ", birlashma(list1, list2))
    print("Farq: ", farq(list1, list2))
    print("List 1 dan List 2 ga farq: ", farq(list1, list2))
    print("List 2 dan List 1 ga farq: ", farq(list2, list1))

asosiy_funktsiya()

def sinov():
    list1 = ["a", "b", "c"]
    list2 = ["c", "d", "e"]
    print("List 1: ", list1)
    print("List 2: ", list2)
    print("Kesishma: ", kesishma(list1, list2))
    print("Birlashma: ", birlashma(list1, list2))
    print("Farq: ", farq(list1, list2))
    print("List 1 dan List 2 ga farq: ", farq(list1, list2))
    print("List 2 dan List 1 ga farq: ", farq(list2, list1))

sinov()

def qoshimcha_sinov():
    list1 = [1.2, 2.3, 3.4]
    list2 = [3.4, 4.5, 5.6]
    print("List 1: ", list1)
    print("List 2: ", list2)
    print("Kesishma: ", kesishma(list1, list2))
    print("Birlashma: ", birlashma(list1, list2))
    print("Farq: ", farq(list1, list2))
    print("List 1 dan List 2 ga farq: ", farq(list1, list2))
    print("List 2 dan List 1 ga farq: ", farq(list2, list1))

qoshimcha_sinov()

def oxirgi_sinov():
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]
    print("List 1: ", list1)
    print("List 2: ", list2)
    print("Kesishma: ", kesishma(list1, list2))
    print("Birlashma: ", birlashma(list1, list2))
    print("Farq: ", farq(list1, list2))
    print("List 1 dan List 2 ga farq: ", farq(list1, list2))
    print("List 2 dan List 1 ga farq: ", farq(list2, list1))

oxirgi_sinov()