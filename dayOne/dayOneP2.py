with open("input.txt", "r") as  data:
  point = 50
  zero = 0
  
  for row in data:
    dir = 1 if row[0] == "R" else -1
    amount = int(row[1:])
    
    zero += amount // 100
    
    r = amount % 100
    
    if r > 0:
      new = point + dir * r
      
      if (dir > 0 and new >= 100) or (dir < 0 and new < 1 and point > 0):
        zero += 1
      
      point = (new + 100) % 100
    print(zero)