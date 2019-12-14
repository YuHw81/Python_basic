def getTotalPage(m, n):
    page = m // n
    if m % n > 0 : page += 1
    return page

print(getTotalPage(5, 10))


