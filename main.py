a = [1,3,4,4,4,5]

a.sort()  # Important


db = {}
for i in range(0,max(a) + 1):
    prev = None
    for x in a:
        current = x
        if prev is None:
            prev = current
            continue
        else:
            diff = current - prev
            if diff == i:
                # Check current count for this diff
                current_count = db.get(i)
                if current_count is None:
                    db.update({i: 1})
                else:
                    db.update({i: current_count + 1})
        prev = current

zero_edge = db.get(0)
if zero_edge is not None:
    db.update({0: zero_edge + 1})

m = max(db, key=db.get)
return m
