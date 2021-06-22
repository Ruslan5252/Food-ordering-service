names = ["Руслан","Саша","Вася","Петя"]
search_for = "Вася"
def linear_search(where,what):
    for v in enumerate(where):
        if v[1] == what:
            return v[0]
    return None
print("Искомый элемент ",search_for,"Найден под индексом",linear_search(names,search_for))