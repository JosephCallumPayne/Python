dashes = "-----------------------"
board = [[0]*7 for _ in range(6)]
labels = [[1,2,3,4,5,6,7]]
w,p,c = 0,1,42
s = []
abcd5,bcde5,cdef5,defg5,abcd4,bcde4,cdef4,defg4,abcd3,bcde3,cdef3,defg3,abcd2,bcde2,cdef2,defg2,abcd1,bcde1,cdef1,defg1,abcd0,bcde0,cdef0,defg0,ABCD1,BCDE1,CDEF1,ABCD2,BCDE2,CDEF2,ABCD3,BCDE3,CDEF3,ABCD4,BCDE4,CDEF4,ABCD5,BCDE5,CDEF5,ABCD6,BCDE6,CDEF6,ABCD7,BCDE7,CDEF7,AbCd2,BcDe2,CdEf2,DeFg2,aBcD5,bCdE5,cDeF5,dEfG5,AbCd1,BcDe1,CdEf1,DeFg1,aBcD4,bCdE4,cDeF4,dEfG4,AbCd0,BcDe0,CdEf0,DeFg0,aBcD3,bCdE3,cDeF3,dEfG3 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
print("Do you have a seed?")
print("If yes, state it, if no then press enter.")
try:
  seed = str(input())
  seed = seed[1:(len(seed)-1)]
  seed = list(map(int, seed.split(", ")))
  s = seed[:]
except:
  seed = s
while len(seed) > 0:
  i = seed[0]
  seed.remove(seed[0])
  for j in range(5, -1, -1):
    if board[j][i] == 0:
      board[j][i] = p
      c -= 1
      if i == 3:
        if j == 5:
          abcd5 += 2*p-3
          bcde5 += 2*p-3
          cdef5 += 2*p-3
          defg5 += 2*p-3
          ABCD4 += 2*p-3
          dEfG5 += 2*p-3
          AbCd2 += 2*p-3
          if abcd5 == 4*(2*p-3) or bcde5 == 4*(2*p-3) or cdef5 == 4*(2*p-3) or defg5 == 4*(2*p-3) or ABCD4 == 4*(2*p-3) or dEfG5 == 4*(2*p-3) or AbCd2 == 4*(2*p-3):
            w = p
            break
        elif j == 4:
          abcd4 += 2*p-3
          bcde4 += 2*p-3
          cdef4 += 2*p-3
          defg4 += 2*p-3
          ABCD4 += 2*p-3
          BCDE4 += 2*p-3
          dEfG4 += 2*p-3
          AbCd1 += 2*p-3
          cDeF5 += 2*p-3
          BcDe2 += 2*p-3
          if abcd4 == 4*(2*p-3) or bcde4 == 4*(2*p-3) or cdef4 == 4*(2*p-3) or defg4 == 4*(2*p-3) or ABCD4 == 4*(2*p-3) or BCDE4 == 4*(2*p-3) or dEfG4 == 4*(2*p-3) or AbCd1 == 4*(2*p-3) or cDeF5 == 4*(2*p-3) or BcDe2 == 4*(2*p-3):
            w = p
            break
        elif j == 3:
          abcd3 += 2*p-3
          bcde3 += 2*p-3
          cdef3 += 2*p-3
          defg3 += 2*p-3
          ABCD4 += 2*p-3
          BCDE4 += 2*p-3
          CDEF4 += 2*p-3
          dEfG3 += 2*p-3
          AbCd0 += 2*p-3
          cDeF4 += 2*p-3
          BcDe1 += 2*p-3
          bCdE5 += 2*p-3
          CdEf2 += 2*p-3
          if abcd3 == 4*(2*p-3) or bcde3 == 4*(2*p-3) or cdef3 == 4*(2*p-3) or defg3 == 4*(2*p-3) or ABCD4 == 4*(2*p-3) or BCDE4 == 4*(2*p-3) or CDEF4 == 4*(2*p-3) or dEfG3 == 4*(2*p-3) or AbCd0 == 4*(2*p-3) or cDeF4 == 4*(2*p-3) or BcDe1 == 4*(2*p-3) or bCdE5 == 4*(2*p-3) or CdEf2 == 4*(2*p-3):
            w = p
            break
        elif j == 2:
          abcd2 += 2*p-3
          bcde2 += 2*p-3
          cdef2 += 2*p-3
          defg2 += 2*p-3
          ABCD4 += 2*p-3
          BCDE4 += 2*p-3
          CDEF4 += 2*p-3
          cDeF3 += 2*p-3
          BcDe0 += 2*p-3
          bCdE4 += 2*p-3
          CdEf1 += 2*p-3
          aBcD5 += 2*p-3
          DeFg2 += 2*p-3
          if abcd2 == 4*(2*p-3) or bcde2 == 4*(2*p-3) or cdef2 == 4*(2*p-3) or defg2 == 4*(2*p-3) or ABCD4 == 4*(2*p-3) or BCDE4 == 4*(2*p-3) or CDEF4 == 4*(2*p-3) or cDeF3 == 4*(2*p-3) or BcDe0 == 4*(2*p-3) or bCdE4 == 4*(2*p-3) or CdEf1 == 4*(2*p-3) or aBcD5 == 4*(2*p-3) or DeFg2 == 4*(2*p-3):
            w = p
            break
        elif j == 1:
          abcd1 += 2*p-3
          bcde1 += 2*p-3
          cdef1 += 2*p-3
          defg1 += 2*p-3
          BCDE4 += 2*p-3
          CDEF4 += 2*p-3
          cDeF4 += 2*p-3
          BcDe1 += 2*p-3
          aBcD4 += 2*p-3
          DeFg1 += 2*p-3
          if abcd1 == 4*(2*p-3) or bcde1 == 4*(2*p-3) or cdef1 == 4*(2*p-3) or defg1 == 4*(2*p-3) or BCDE4 == 4*(2*p-3) or CDEF4 == 4*(2*p-3) or cDeF4 == 4*(2*p-3) or BcDe1 == 4*(2*p-3) or aBcD4 == 4*(2*p-3) or DeFg1 == 4*(2*p-3):
            w = p
            break
        elif j == 0:
          abcd0 += 2*p-3
          bcde0 += 2*p-3
          cdef0 += 2*p-3
          defg0 += 2*p-3
          CDEF4 += 2*p-3
          aBcD5 += 2*p-3
          DeFg2 += 2*p-3
          if abcd0 == 4*(2*p-3) or bcde0 == 4*(2*p-3) or cdef0 == 4*(2*p-3) or defg0 == 4*(2*p-3) or CDEF4 == 4*(2*p-3) or aBcD5 == 4*(2*p-3) or DeFg2 == 4*(2*p-3):
            w = p
            break
      elif i == 4:
        if j == 5:
          bcde5 += 2*p-3
          cdef5 += 2*p-3
          defg5 += 2*p-3
          ABCD5 += 2*p-3
          BcDe2 += 2*p-3
          if bcde5 == 4*(2*p-3) or cdef5 == 4*(2*p-3) or defg5 == 4*(2*p-3) or ABCD5 == 4*(2*p-3) or BcDe2 == 4*(2*p-3):
            w = p
            break
        elif j == 4:
          bcde4 += 2*p-3
          cdef4 += 2*p-3
          defg4 += 2*p-3
          ABCD5 += 2*p-3
          BCDE5 += 2*p-3
          dEfG5 += 2*p-3
          BcDe1 += 2*p-3
          CdEf2 += 2*p-3
          if bcde4 == 4*(2*p-3) or cdef4 == 4*(2*p-3) or defg4 == 4*(2*p-3) or ABCD5 == 4*(2*p-3) or BCDE5 == 4*(2*p-3) or dEfG5 == 4*(2*p-3) or BcDe1 == 4*(2*p-3) or CdEf2 == 4*(2*p-3):
            w = p
            break
        elif j == 3:
          bcde3 += 2*p-3
          cdef3 += 2*p-3
          defg3 += 2*p-3
          ABCD5 += 2*p-3
          BCDE5 += 2*p-3
          CDEF5 += 2*p-3
          dEfG4 += 2*p-3
          BcDe0 += 2*p-3
          CdEf1 += 2*p-3
          DeFg2 += 2*p-3
          cDeF5 += 2*p-3
          if bcde3 == 4*(2*p-3) or cdef3 == 4*(2*p-3) or defg3 == 4*(2*p-3) or ABCD5 == 4*(2*p-3) or BCDE5 == 4*(2*p-3) or CDEF5 == 4*(2*p-3) or dEfG4 == 4*(2*p-3) or BcDe0 == 4*(2*p-3) or CdEf1 == 4*(2*p-3) or DeFg2 == 4*(2*p-3) or cDeF5 == 4*(2*p-3):
            w = p
            break
        elif j == 2:
          bcde2 += 2*p-3
          cdef2 += 2*p-3
          defg2 += 2*p-3
          ABCD5 += 2*p-3
          BCDE5 += 2*p-3
          CDEF5 += 2*p-3
          dEfG3 += 2*p-3
          CdEf0 += 2*p-3
          DeFg1 += 2*p-3
          cDeF4 += 2*p-3
          bCdE5 += 2*p-3
          if bcde2 == 4*(2*p-3) or cdef2 == 4*(2*p-3) or defg2 == 4*(2*p-3) or ABCD5 == 4*(2*p-3) or BCDE5 == 4*(2*p-3) or CDEF5 == 4*(2*p-3) or dEfG3 == 4*(2*p-3) or CdEf0 == 4*(2*p-3) or DeFg1 == 4*(2*p-3) or cDeF4 == 4*(2*p-3) or bCdE5 == 4*(2*p-3):
            w = p
            break
        elif j == 1:
          bcde1 += 2*p-3
          cdef1 += 2*p-3
          defg1 += 2*p-3
          BCDE5 += 2*p-3
          CDEF5 += 2*p-3
          cDeF3 += 2*p-3
          DeFg0 += 2*p-3
          bCdE4 += 2*p-3
          if bcde1 == 4*(2*p-3) or cdef1 == 4*(2*p-3) or defg1 == 4*(2*p-3) or BCDE5 == 4*(2*p-3) or CDEF5 == 4*(2*p-3) or cDeF3 == 4*(2*p-3) or DeFg0 == 4*(2*p-3) or bCdE4 == 4*(2*p-3):
            w = p
            break
        elif j == 0:
          bcde0 += 2*p-3
          cdef0 += 2*p-3
          defg0 += 2*p-3
          CDEF5 += 2*p-3
          bCdE3 += 2*p-3
          if bcde0 == 4*(2*p-3) or cdef0 == 4*(2*p-3) or defg0 == 4*(2*p-3) or CDEF5 == 4*(2*p-3) or bCdE3 == 4*(2*p-3):
            w = p
            break
      elif i == 2:
        if j == 5:
          abcd5 += 2*p-3
          bcde5 += 2*p-3
          cdef5 += 2*p-3
          ABCD3 += 2*p-3
          cDeF5 += 2*p-3
          if abcd5 == 4*(2*p-3) or bcde5 == 4*(2*p-3) or cdef5 == 4*(2*p-3) or ABCD3 == 4*(2*p-3) or cDeF5 == 4*(2*p-3):
            w = p
            break
        elif j == 4:
          abcd4 += 2*p-3
          bcde4 += 2*p-3
          cdef4 += 2*p-3
          ABCD3 += 2*p-3
          BCDE3 += 2*p-3
          cDeF4 += 2*p-3
          AbCd2 += 2*p-3
          bCdE5 += 2*p-3
          if abcd4 == 4*(2*p-3) or bcde4 == 4*(2*p-3) or cdef4 == 4*(2*p-3) or ABCD3 == 4*(2*p-3) or BCDE3 == 4*(2*p-3) or cDeF4 == 4*(2*p-3) or AbCd2 == 4*(2*p-3) or bCdE5 == 4*(2*p-3):
            w = p
            break
        elif j == 3:
          abcd3 += 2*p-3
          bcde3 += 2*p-3
          cdef3 += 2*p-3
          ABCD3 += 2*p-3
          BCDE3 += 2*p-3
          CDEF3 += 2*p-3
          cDeF3 += 2*p-3
          bCdE4 += 2*p-3
          aBcD5 += 2*p-3
          BcDe2 += 2*p-3
          AbCd1 += 2*p-3
          if abcd3 == 4*(2*p-3) or bcde3 == 4*(2*p-3) or cdef3 == 4*(2*p-3) or ABCD3 == 4*(2*p-3) or BCDE3 == 4*(2*p-3) or CDEF3 == 4*(2*p-3) or cDeF3 == 4*(2*p-3) or bCdE4 == 4*(2*p-3) or aBcD5 == 4*(2*p-3) or BcDe2 == 4*(2*p-3) or AbCd1 == 4*(2*p-3):
            w = p
            break
        elif j == 2:
          abcd2 += 2*p-3
          bcde2 += 2*p-3
          cdef2 += 2*p-3
          ABCD3 += 2*p-3
          BCDE3 += 2*p-3
          CDEF3 += 2*p-3
          aBcD4 += 2*p-3
          bCdE3 += 2*p-3
          AbCd0 += 2*p-3
          BcDe1 += 2*p-3
          CdEf2 += 2*p-3
          if abcd2 == 4*(2*p-3) or bcde2 == 4*(2*p-3) or cdef2 == 4*(2*p-3) or ABCD3 == 4*(2*p-3) or BCDE3 == 4*(2*p-3) or CDEF3 == 4*(2*p-3) or aBcD4 == 4*(2*p-3) or bCdE3 == 4*(2*p-3) or AbCd0 == 4*(2*p-3) or BcDe1 == 4*(2*p-3) or CdEf2 == 4*(2*p-3):
            w = p
            break
        elif j == 1:
          abcd1 += 2*p-3
          bcde1 += 2*p-3
          cdef1 += 2*p-3
          BCDE3 += 2*p-3
          CDEF3 += 2*p-3
          aBcD3 += 2*p-3
          BcDe0 += 2*p-3
          CdEf1 += 2*p-3
          if abcd1 == 4*(2*p-3) or bcde1 == 4*(2*p-3) or cdef1 == 4*(2*p-3) or BCDE3 == 4*(2*p-3) or CDEF3 == 4*(2*p-3) or aBcD3 == 4*(2*p-3) or BcDe0 == 4*(2*p-3) or CdEf1 == 4*(2*p-3):
            w = p
            break
        elif j == 0:
          abcd0 += 2*p-3
          bcde0 += 2*p-3
          cdef0 += 2*p-3
          CDEF3 += 2*p-3
          CdEf0 += 2*p-3
          if abcd0 == 4*(2*p-3) or bcde0 == 4*(2*p-3) or cdef0 == 4*(2*p-3) or CDEF3 == 4*(2*p-3) or CdEf0 == 4*(2*p-3):
            w = p
            break
      elif i == 5:
        if j == 5:
          cdef5 += 2*p-3
          defg5 += 2*p-3
          ABCD6 += 2*p-3
          CdEf2 += 2*p-3
          if cdef5 == 4*(2*p-3) or defg5 == 4*(2*p-3) or ABCD6 == 4*(2*p-3) or CdEf2 == 4*(2*p-3):
            w = p
        elif j == 4:
          cdef4 += 2*p-3
          defg4 += 2*p-3
          ABCD6 += 2*p-3
          BCDE6 += 2*p-3
          DeFg2 += 2*p-3
          CdEf1 += 2*p-3
          if cdef4 == 4*(2*p-3) or defg4 == 4*(2*p-3) or ABCD6 == 4*(2*p-3) or BCDE6 == 4*(2*p-3) or DeFg2 == 4*(2*p-3) or CdEf1 == 4*(2*p-3):
            w = p
        elif j == 3:
          cdef3 += 2*p-3
          defg3 += 2*p-3
          ABCD6 += 2*p-3
          BCDE6 += 2*p-3
          CDEF6 += 2*p-3
          dEfG5 += 2*p-3
          DeFg1 += 2*p-3
          CdEf0 += 2*p-3
          if cdef3 == 4*(2*p-3) or defg3 == 4*(2*p-3) or ABCD6 == 4*(2*p-3) or BCDE6 == 4*(2*p-3) or CDEF6 == 4*(2*p-3) or dEfG5 == 4*(2*p-3) or DeFg1 == 4*(2*p-3) or CdEf0 == 4*(2*p-3):
            w = p
        elif j == 2:
          cdef2 += 2*p-3
          defg2 += 2*p-3
          ABCD6 += 2*p-3
          BCDE6 += 2*p-3
          CDEF6 += 2*p-3
          dEfG4 += 2*p-3
          cDeF5 += 2*p-3
          DeFg0 += 2*p-3
          if cdef2 == 4*(2*p-3) or defg2 == 4*(2*p-3) or ABCD6 == 4*(2*p-3) or BCDE6  == 4*(2*p-3) or CDEF6 == 4*(2*p-3) or dEfG4 == 4*(2*p-3) or cDeF5 == 4*(2*p-3) or DeFg0 == 4*(2*p-3):
            w = p
        elif j == 1:
          cdef1 += 2*p-3
          defg1 += 2*p-3
          BCDE6 += 2*p-3
          CDEF6 += 2*p-3
          dEfG3 += 2*p-3
          cDeF4 += 2*p-3
          if cdef1 == 4*(2*p-3) or defg1 == 4*(2*p-3) or BCDE6 == 4*(2*p-3) or CDEF6 == 4*(2*p-3) or dEfG3 == 4*(2*p-3) or cDeF4 == 4*(2*p-3):
            w = p
        elif j == 0:
          cdef0 += 2*p-3
          defg0 += 2*p-3
          CDEF6 += 2*p-3
          cDeF3 += 2*p-3
          if cdef0 == 4*(2*p-3) or defg0 == 4*(2*p-3) or CDEF6 == 4*(2*p-3) or cDeF3 == 4*(2*p-3):
            w = p
      elif i == 1:
        if j == 5:
          abcd5 += 2*p-3
          bcde5 += 2*p-3
          ABCD2 += 2*p-3
          bCdE5 += 2*p-3
          if abcd5 == 4*(2*p-3) or bcde5 == 4*(2*p-3) or ABCD2 == 4*(2*p-3) or bCdE5 == 4*(2*p-3):
            w = p
        elif j == 4:
          abcd4 += 2*p-3
          bcde4 += 2*p-3
          ABCD2 += 2*p-3
          BCDE2 += 2*p-3
          bCdE4 += 2*p-3
          cDeF5 += 2*p-3
          if abcd4 == 4*(2*p-3) or bcde4 == 4*(2*p-3) or ABCD2 == 4*(2*p-3) or BCDE2 == 4*(2*p-3) or bCdE4 == 4*(2*p-3) or cDeF5 == 4*(2*p-3):
            w = p
        elif j == 3:
          abcd3 += 2*p-3
          bcde3 += 2*p-3
          ABCD2 += 2*p-3
          BCDE2 += 2*p-3
          CDEF2 += 2*p-3
          bCdE3 += 2*p-3
          cDeF4 += 2*p-3
          AbCd2 += 2*p-3
          if abcd3 == 4*(2*p-3) or bcde3 == 4*(2*p-3) or ABCD2 == 4*(2*p-3) or BCDE2 == 4*(2*p-3) or CDEF2 == 4*(2*p-3) or bCdE3 == 4*(2*p-3) or cDeF4 == 4*(2*p-3) or AbCd2 == 4*(2*p-3):
            w = p
        elif j == 2:
          abcd2 += 2*p-3
          bcde2 += 2*p-3
          ABCD2 += 2*p-3
          BCDE2 += 2*p-3
          CDEF2 += 2*p-3
          cDeF3 += 2*p-3
          AbCd1 += 2*p-3
          BcDe2 += 2*p-3
          if abcd2 == 4*(2*p-3) or bcde2 == 4*(2*p-3) or ABCD2 == 4*(2*p-3) or BCDE2 == 4*(2*p-3) or CDEF2 == 4*(2*p-3) or cDeF3 == 4*(2*p-3) or AbCd1 == 4*(2*p-3) or BcDe2 == 4*(2*p-3):
            w = p
        elif j == 1:
          abcd1 += 2*p-3
          bcde1 += 2*p-3
          BCDE2 += 2*p-3
          CDEF2 += 2*p-3
          AbCd0 += 2*p-3
          BcDe1 += 2*p-3
          if abcd1 == 4*(2*p-3) or bcde1 == 4*(2*p-3) or BCDE2 == 4*(2*p-3) or CDEF2 == 4*(2*p-3) or AbCd0 == 4*(2*p-3) or BcDe1 == 4*(2*p-3):
            w = p
        elif j == 0:
          abcd0 += 2*p-3
          bcde0 += 2*p-3
          CDEF2 += 2*p-3
          BcDe0 += 2*p-3
          if abcd0 == 4*(2*p-3) or bcde0 == 4*(2*p-3) or CDEF2 == 4*(2*p-3) or BcDe0 == 4*(2*p-3):
            w = p
      elif i == 6:
        if j == 5:
          defg5 += 2*p-3
          ABCD7 += 2*p-3
          DeFg2 += 2*p-3
          if defg5 == 4*(2*p-3) or ABCD7 == 4*(2*p-3) or DeFg2 == 4*(2*p-3):
            w = p
        elif j == 4:
          defg4 += 2*p-3
          ABCD7 += 2*p-3
          BCDE7 += 2*p-3
          DeFg1 += 2*p-3
          if defg4 == 4*(2*p-3) or ABCD7 == 4*(2*p-3) or BCDE7 == 4*(2*p-3) or DeFg1 == 4*(2*p-3):
            w = p
        elif j == 3:
          defg3 += 2*p-3
          ABCD7 += 2*p-3
          BCDE7 += 2*p-3
          CDEF7 += 2*p-3
          DeFg0 += 2*p-3
          if defg4 == 4*(2*p-3) or ABCD7 == 4*(2*p-3) or BCDE7 == 4*(2*p-3) or CDEF7 == 4*(2*p-3) or DeFg0 == 4*(2*p-3):
            w = p
        elif j == 2:
          defg2 += 2*p-3
          ABCD7 += 2*p-3
          BCDE7 += 2*p-3
          CDEF7 += 2*p-3
          dEfG5 += 2*p-3
          if defg2 == 4*(2*p-3) or ABCD7 == 4*(2*p-3) or BCDE7 == 4*(2*p-3) or CDEF7 == 4*(2*p-3) or dEfG5 == 4*(2*p-3):
            w = p
        elif j == 1:
          defg1 += 2*p-3
          BCDE7 += 2*p-3
          CDEF7 += 2*p-3
          dEfG4 += 2*p-3
          if defg1 == 4*(2*p-3) or BCDE7 == 4*(2*p-3) or CDEF7 == 4*(2*p-3) or dEfG4 == 4*(2*p-3):
            w = p
        elif j == 0:
          defg0 += 2*p-3
          CDEF7 += 2*p-3
          dEfG3 += 2*p-3
          if defg0 == 4*(2*p-3) or CDEF7 == 4*(2*p-3) or dEfG3 == 4*(2*p-3):
            w = p
      elif i == 0:
        if j == 5:
          abcd5 += 2*p-3
          ABCD1 += 2*p-3
          aBcD5 += 2*p-3
          if abcd5 == 4*(2*p-3) or ABCD1 == 4*(2*p-3) or aBcD5 == 4*(2*p-3):
            w = p
        elif j == 4:
          abcd4 += 2*p-3
          ABCD1 += 2*p-3
          BCDE1 += 2*p-3
          aBcD4 += 2*p-3
          if abcd5 == 4*(2*p-3) or ABCD1 == 4*(2*p-3) or BCDE1 == 4*(2*p-3) or aBcD4 == 4*(2*p-3):
            w = p
        elif j == 3:
          abcd3 += 2*p-3
          ABCD1 += 2*p-3
          BCDE1 += 2*p-3
          CDEF1 += 2*p-3
          aBcD3 += 2*p-3
          if abcd5 == 4*(2*p-3) or ABCD1 == 4*(2*p-3) or BCDE1 == 4*(2*p-3) or CDEF1 == 4*(2*p-3) or aBcD3 == 4*(2*p-3):
            w = p
        elif j == 2:
          abcd2 += 2*p-3
          ABCD1 += 2*p-3
          BCDE1 += 2*p-3
          CDEF1 += 2*p-3
          AbCd2 += 2*p-3
          if abcd5 == 4*(2*p-3) or ABCD1 == 4*(2*p-3) or BCDE1 == 4*(2*p-3) or CDEF1 == 4*(2*p-3) or AbCd2 == 4*(2*p-3):
            w = p
        elif j == 1:
          abcd1 += 2*p-3
          BCDE1 += 2*p-3
          CDEF1 += 2*p-3
          AbCd1 += 2*p-3
          if abcd5 == 4*(2*p-3) or BCDE1 == 4*(2*p-3) or CDEF1 == 4*(2*p-3) or AbCd1 == 4*(2*p-3):
            w = p
        elif j == 0:
          abcd0 += 2*p-3
          CDEF1 += 2*p-3
          AbCd0 += 2*p-3
          if abcd5 == 4*(2*p-3) or CDEF1 == 4*(2*p-3) or AbCd0 == 4*(2*p-3):
            w = p
      break
    if j == 0:
        p = p%2+1
  p = p%2+1
seed = s
print(dashes)
print(board)
print(dashes)
print(labels)
while c > 0 and w == 0:
  i = -1
  print("Player {}'s turn.".format(p))
  print("Select a column from 1-7.")
  while i > 6 or i < 0:
    try:
      i = int(input())-1
      seed.append(i)
      print("seed = "+str(seed))
    except:
      continue
  for j in range(5, -1, -1):
    if board[j][i] == 0:
      board[j][i] = p
      c -= 1
      if i == 3:
        if j == 5:
          abcd5 += 2*p-3
          bcde5 += 2*p-3
          cdef5 += 2*p-3
          defg5 += 2*p-3
          ABCD4 += 2*p-3
          dEfG5 += 2*p-3
          AbCd2 += 2*p-3
          if abcd5 == 4*(2*p-3) or bcde5 == 4*(2*p-3) or cdef5 == 4*(2*p-3) or defg5 == 4*(2*p-3) or ABCD4 == 4*(2*p-3) or dEfG5 == 4*(2*p-3) or AbCd2 == 4*(2*p-3):
            w = p
            break
        elif j == 4:
          abcd4 += 2*p-3
          bcde4 += 2*p-3
          cdef4 += 2*p-3
          defg4 += 2*p-3
          ABCD4 += 2*p-3
          BCDE4 += 2*p-3
          dEfG4 += 2*p-3
          AbCd1 += 2*p-3
          cDeF5 += 2*p-3
          BcDe2 += 2*p-3
          if abcd4 == 4*(2*p-3) or bcde4 == 4*(2*p-3) or cdef4 == 4*(2*p-3) or defg4 == 4*(2*p-3) or ABCD4 == 4*(2*p-3) or BCDE4 == 4*(2*p-3) or dEfG4 == 4*(2*p-3) or AbCd1 == 4*(2*p-3) or cDeF5 == 4*(2*p-3) or BcDe2 == 4*(2*p-3):
            w = p
            break
        elif j == 3:
          abcd3 += 2*p-3
          bcde3 += 2*p-3
          cdef3 += 2*p-3
          defg3 += 2*p-3
          ABCD4 += 2*p-3
          BCDE4 += 2*p-3
          CDEF4 += 2*p-3
          dEfG3 += 2*p-3
          AbCd0 += 2*p-3
          cDeF4 += 2*p-3
          BcDe1 += 2*p-3
          bCdE5 += 2*p-3
          CdEf2 += 2*p-3
          if abcd3 == 4*(2*p-3) or bcde3 == 4*(2*p-3) or cdef3 == 4*(2*p-3) or defg3 == 4*(2*p-3) or ABCD4 == 4*(2*p-3) or BCDE4 == 4*(2*p-3) or CDEF4 == 4*(2*p-3) or dEfG3 == 4*(2*p-3) or AbCd0 == 4*(2*p-3) or cDeF4 == 4*(2*p-3) or BcDe1 == 4*(2*p-3) or bCdE5 == 4*(2*p-3) or CdEf2 == 4*(2*p-3):
            w = p
            break
        elif j == 2:
          abcd2 += 2*p-3
          bcde2 += 2*p-3
          cdef2 += 2*p-3
          defg2 += 2*p-3
          ABCD4 += 2*p-3
          BCDE4 += 2*p-3
          CDEF4 += 2*p-3
          cDeF3 += 2*p-3
          BcDe0 += 2*p-3
          bCdE4 += 2*p-3
          CdEf1 += 2*p-3
          aBcD5 += 2*p-3
          DeFg2 += 2*p-3
          if abcd2 == 4*(2*p-3) or bcde2 == 4*(2*p-3) or cdef2 == 4*(2*p-3) or defg2 == 4*(2*p-3) or ABCD4 == 4*(2*p-3) or BCDE4 == 4*(2*p-3) or CDEF4 == 4*(2*p-3) or cDeF3 == 4*(2*p-3) or BcDe0 == 4*(2*p-3) or bCdE4 == 4*(2*p-3) or CdEf1 == 4*(2*p-3) or aBcD5 == 4*(2*p-3) or DeFg2 == 4*(2*p-3):
            w = p
            break
        elif j == 1:
          abcd1 += 2*p-3
          bcde1 += 2*p-3
          cdef1 += 2*p-3
          defg1 += 2*p-3
          BCDE4 += 2*p-3
          CDEF4 += 2*p-3
          cDeF4 += 2*p-3
          BcDe1 += 2*p-3
          aBcD4 += 2*p-3
          DeFg1 += 2*p-3
          if abcd1 == 4*(2*p-3) or bcde1 == 4*(2*p-3) or cdef1 == 4*(2*p-3) or defg1 == 4*(2*p-3) or BCDE4 == 4*(2*p-3) or CDEF4 == 4*(2*p-3) or cDeF4 == 4*(2*p-3) or BcDe1 == 4*(2*p-3) or aBcD4 == 4*(2*p-3) or DeFg1 == 4*(2*p-3):
            w = p
            break
        elif j == 0:
          abcd0 += 2*p-3
          bcde0 += 2*p-3
          cdef0 += 2*p-3
          defg0 += 2*p-3
          CDEF4 += 2*p-3
          aBcD5 += 2*p-3
          DeFg2 += 2*p-3
          if abcd0 == 4*(2*p-3) or bcde0 == 4*(2*p-3) or cdef0 == 4*(2*p-3) or defg0 == 4*(2*p-3) or CDEF4 == 4*(2*p-3) or aBcD5 == 4*(2*p-3) or DeFg2 == 4*(2*p-3):
            w = p
            break
      elif i == 4:
        if j == 5:
          bcde5 += 2*p-3
          cdef5 += 2*p-3
          defg5 += 2*p-3
          ABCD5 += 2*p-3
          BcDe2 += 2*p-3
          if bcde5 == 4*(2*p-3) or cdef5 == 4*(2*p-3) or defg5 == 4*(2*p-3) or ABCD5 == 4*(2*p-3) or BcDe2 == 4*(2*p-3):
            w = p
            break
        elif j == 4:
          bcde4 += 2*p-3
          cdef4 += 2*p-3
          defg4 += 2*p-3
          ABCD5 += 2*p-3
          BCDE5 += 2*p-3
          dEfG5 += 2*p-3
          BcDe1 += 2*p-3
          CdEf2 += 2*p-3
          if bcde4 == 4*(2*p-3) or cdef4 == 4*(2*p-3) or defg4 == 4*(2*p-3) or ABCD5 == 4*(2*p-3) or BCDE5 == 4*(2*p-3) or dEfG5 == 4*(2*p-3) or BcDe1 == 4*(2*p-3) or CdEf2 == 4*(2*p-3):
            w = p
            break
        elif j == 3:
          bcde3 += 2*p-3
          cdef3 += 2*p-3
          defg3 += 2*p-3
          ABCD5 += 2*p-3
          BCDE5 += 2*p-3
          CDEF5 += 2*p-3
          dEfG4 += 2*p-3
          BcDe0 += 2*p-3
          CdEf1 += 2*p-3
          DeFg2 += 2*p-3
          cDeF5 += 2*p-3
          if bcde3 == 4*(2*p-3) or cdef3 == 4*(2*p-3) or defg3 == 4*(2*p-3) or ABCD5 == 4*(2*p-3) or BCDE5 == 4*(2*p-3) or CDEF5 == 4*(2*p-3) or dEfG4 == 4*(2*p-3) or BcDe0 == 4*(2*p-3) or CdEf1 == 4*(2*p-3) or DeFg2 == 4*(2*p-3) or cDeF5 == 4*(2*p-3):
            w = p
            break
        elif j == 2:
          bcde2 += 2*p-3
          cdef2 += 2*p-3
          defg2 += 2*p-3
          ABCD5 += 2*p-3
          BCDE5 += 2*p-3
          CDEF5 += 2*p-3
          dEfG3 += 2*p-3
          CdEf0 += 2*p-3
          DeFg1 += 2*p-3
          cDeF4 += 2*p-3
          bCdE5 += 2*p-3
          if bcde2 == 4*(2*p-3) or cdef2 == 4*(2*p-3) or defg2 == 4*(2*p-3) or ABCD5 == 4*(2*p-3) or BCDE5 == 4*(2*p-3) or CDEF5 == 4*(2*p-3) or dEfG3 == 4*(2*p-3) or CdEf0 == 4*(2*p-3) or DeFg1 == 4*(2*p-3) or cDeF4 == 4*(2*p-3) or bCdE5 == 4*(2*p-3):
            w = p
            break
        elif j == 1:
          bcde1 += 2*p-3
          cdef1 += 2*p-3
          defg1 += 2*p-3
          BCDE5 += 2*p-3
          CDEF5 += 2*p-3
          cDeF3 += 2*p-3
          DeFg0 += 2*p-3
          bCdE4 += 2*p-3
          if bcde1 == 4*(2*p-3) or cdef1 == 4*(2*p-3) or defg1 == 4*(2*p-3) or BCDE5 == 4*(2*p-3) or CDEF5 == 4*(2*p-3) or cDeF3 == 4*(2*p-3) or DeFg0 == 4*(2*p-3) or bCdE4 == 4*(2*p-3):
            w = p
            break
        elif j == 0:
          bcde0 += 2*p-3
          cdef0 += 2*p-3
          defg0 += 2*p-3
          CDEF5 += 2*p-3
          bCdE3 += 2*p-3
          if bcde0 == 4*(2*p-3) or cdef0 == 4*(2*p-3) or defg0 == 4*(2*p-3) or CDEF5 == 4*(2*p-3) or bCdE3 == 4*(2*p-3):
            w = p
            break
      elif i == 2:
        if j == 5:
          abcd5 += 2*p-3
          bcde5 += 2*p-3
          cdef5 += 2*p-3
          ABCD3 += 2*p-3
          cDeF5 += 2*p-3
          if abcd5 == 4*(2*p-3) or bcde5 == 4*(2*p-3) or cdef5 == 4*(2*p-3) or ABCD3 == 4*(2*p-3) or cDeF5 == 4*(2*p-3):
            w = p
            break
        elif j == 4:
          abcd4 += 2*p-3
          bcde4 += 2*p-3
          cdef4 += 2*p-3
          ABCD3 += 2*p-3
          BCDE3 += 2*p-3
          cDeF4 += 2*p-3
          AbCd2 += 2*p-3
          bCdE5 += 2*p-3
          if abcd4 == 4*(2*p-3) or bcde4 == 4*(2*p-3) or cdef4 == 4*(2*p-3) or ABCD3 == 4*(2*p-3) or BCDE3 == 4*(2*p-3) or cDeF4 == 4*(2*p-3) or AbCd2 == 4*(2*p-3) or bCdE5 == 4*(2*p-3):
            w = p
            break
        elif j == 3:
          abcd3 += 2*p-3
          bcde3 += 2*p-3
          cdef3 += 2*p-3
          ABCD3 += 2*p-3
          BCDE3 += 2*p-3
          CDEF3 += 2*p-3
          cDeF3 += 2*p-3
          bCdE4 += 2*p-3
          aBcD5 += 2*p-3
          BcDe2 += 2*p-3
          AbCd1 += 2*p-3
          if abcd3 == 4*(2*p-3) or bcde3 == 4*(2*p-3) or cdef3 == 4*(2*p-3) or ABCD3 == 4*(2*p-3) or BCDE3 == 4*(2*p-3) or CDEF3 == 4*(2*p-3) or cDeF3 == 4*(2*p-3) or bCdE4 == 4*(2*p-3) or aBcD5 == 4*(2*p-3) or BcDe2 == 4*(2*p-3) or AbCd1 == 4*(2*p-3):
            w = p
            break
        elif j == 2:
          abcd2 += 2*p-3
          bcde2 += 2*p-3
          cdef2 += 2*p-3
          ABCD3 += 2*p-3
          BCDE3 += 2*p-3
          CDEF3 += 2*p-3
          aBcD4 += 2*p-3
          bCdE3 += 2*p-3
          AbCd0 += 2*p-3
          BcDe1 += 2*p-3
          CdEf2 += 2*p-3
          if abcd2 == 4*(2*p-3) or bcde2 == 4*(2*p-3) or cdef2 == 4*(2*p-3) or ABCD3 == 4*(2*p-3) or BCDE3 == 4*(2*p-3) or CDEF3 == 4*(2*p-3) or aBcD4 == 4*(2*p-3) or bCdE3 == 4*(2*p-3) or AbCd0 == 4*(2*p-3) or BcDe1 == 4*(2*p-3) or CdEf2 == 4*(2*p-3):
            w = p
            break
        elif j == 1:
          abcd1 += 2*p-3
          bcde1 += 2*p-3
          cdef1 += 2*p-3
          BCDE3 += 2*p-3
          CDEF3 += 2*p-3
          aBcD3 += 2*p-3
          BcDe0 += 2*p-3
          CdEf1 += 2*p-3
          if abcd1 == 4*(2*p-3) or bcde1 == 4*(2*p-3) or cdef1 == 4*(2*p-3) or BCDE3 == 4*(2*p-3) or CDEF3 == 4*(2*p-3) or aBcD3 == 4*(2*p-3) or BcDe0 == 4*(2*p-3) or CdEf1 == 4*(2*p-3):
            w = p
            break
        elif j == 0:
          abcd0 += 2*p-3
          bcde0 += 2*p-3
          cdef0 += 2*p-3
          CDEF3 += 2*p-3
          CdEf0 += 2*p-3
          if abcd0 == 4*(2*p-3) or bcde0 == 4*(2*p-3) or cdef0 == 4*(2*p-3) or CDEF3 == 4*(2*p-3) or CdEf0 == 4*(2*p-3):
            w = p
            break
      elif i == 5:
        if j == 5:
          cdef5 += 2*p-3
          defg5 += 2*p-3
          ABCD6 += 2*p-3
          CdEf2 += 2*p-3
          if cdef5 == 4*(2*p-3) or defg5 == 4*(2*p-3) or ABCD6 == 4*(2*p-3) or CdEf2 == 4*(2*p-3):
            w = p
        elif j == 4:
          cdef4 += 2*p-3
          defg4 += 2*p-3
          ABCD6 += 2*p-3
          BCDE6 += 2*p-3
          DeFg2 += 2*p-3
          CdEf1 += 2*p-3
          if cdef4 == 4*(2*p-3) or defg4 == 4*(2*p-3) or ABCD6 == 4*(2*p-3) or BCDE6 == 4*(2*p-3) or DeFg2 == 4*(2*p-3) or CdEf1 == 4*(2*p-3):
            w = p
        elif j == 3:
          cdef3 += 2*p-3
          defg3 += 2*p-3
          ABCD6 += 2*p-3
          BCDE6 += 2*p-3
          CDEF6 += 2*p-3
          dEfG5 += 2*p-3
          DeFg1 += 2*p-3
          CdEf0 += 2*p-3
          if cdef3 == 4*(2*p-3) or defg3 == 4*(2*p-3) or ABCD6 == 4*(2*p-3) or BCDE6 == 4*(2*p-3) or CDEF6 == 4*(2*p-3) or dEfG5 == 4*(2*p-3) or DeFg1 == 4*(2*p-3) or CdEf0 == 4*(2*p-3):
            w = p
        elif j == 2:
          cdef2 += 2*p-3
          defg2 += 2*p-3
          ABCD6 += 2*p-3
          BCDE6 += 2*p-3
          CDEF6 += 2*p-3
          dEfG4 += 2*p-3
          cDeF5 += 2*p-3
          DeFg0 += 2*p-3
          if cdef2 == 4*(2*p-3) or defg2 == 4*(2*p-3) or ABCD6 == 4*(2*p-3) or BCDE6  == 4*(2*p-3) or CDEF6 == 4*(2*p-3) or dEfG4 == 4*(2*p-3) or cDeF5 == 4*(2*p-3) or DeFg0 == 4*(2*p-3):
            w = p
        elif j == 1:
          cdef1 += 2*p-3
          defg1 += 2*p-3
          BCDE6 += 2*p-3
          CDEF6 += 2*p-3
          dEfG3 += 2*p-3
          cDeF4 += 2*p-3
          if cdef1 == 4*(2*p-3) or defg1 == 4*(2*p-3) or BCDE6 == 4*(2*p-3) or CDEF6 == 4*(2*p-3) or dEfG3 == 4*(2*p-3) or cDeF4 == 4*(2*p-3):
            w = p
        elif j == 0:
          cdef0 += 2*p-3
          defg0 += 2*p-3
          CDEF6 += 2*p-3
          cDeF3 += 2*p-3
          if cdef0 == 4*(2*p-3) or defg0 == 4*(2*p-3) or CDEF6 == 4*(2*p-3) or cDeF3 == 4*(2*p-3):
            w = p
      elif i == 1:
        if j == 5:
          abcd5 += 2*p-3
          bcde5 += 2*p-3
          ABCD2 += 2*p-3
          bCdE5 += 2*p-3
          if abcd5 == 4*(2*p-3) or bcde5 == 4*(2*p-3) or ABCD2 == 4*(2*p-3) or bCdE5 == 4*(2*p-3):
            w = p
        elif j == 4:
          abcd4 += 2*p-3
          bcde4 += 2*p-3
          ABCD2 += 2*p-3
          BCDE2 += 2*p-3
          bCdE4 += 2*p-3
          cDeF5 += 2*p-3
          if abcd4 == 4*(2*p-3) or bcde4 == 4*(2*p-3) or ABCD2 == 4*(2*p-3) or BCDE2 == 4*(2*p-3) or bCdE4 == 4*(2*p-3) or cDeF5 == 4*(2*p-3):
            w = p
        elif j == 3:
          abcd3 += 2*p-3
          bcde3 += 2*p-3
          ABCD2 += 2*p-3
          BCDE2 += 2*p-3
          CDEF2 += 2*p-3
          bCdE3 += 2*p-3
          cDeF4 += 2*p-3
          AbCd2 += 2*p-3
          if abcd3 == 4*(2*p-3) or bcde3 == 4*(2*p-3) or ABCD2 == 4*(2*p-3) or BCDE2 == 4*(2*p-3) or CDEF2 == 4*(2*p-3) or bCdE3 == 4*(2*p-3) or cDeF4 == 4*(2*p-3) or AbCd2 == 4*(2*p-3):
            w = p
        elif j == 2:
          abcd2 += 2*p-3
          bcde2 += 2*p-3
          ABCD2 += 2*p-3
          BCDE2 += 2*p-3
          CDEF2 += 2*p-3
          cDeF3 += 2*p-3
          AbCd1 += 2*p-3
          BcDe2 += 2*p-3
          if abcd2 == 4*(2*p-3) or bcde2 == 4*(2*p-3) or ABCD2 == 4*(2*p-3) or BCDE2 == 4*(2*p-3) or CDEF2 == 4*(2*p-3) or cDeF3 == 4*(2*p-3) or AbCd1 == 4*(2*p-3) or BcDe2 == 4*(2*p-3):
            w = p
        elif j == 1:
          abcd1 += 2*p-3
          bcde1 += 2*p-3
          BCDE2 += 2*p-3
          CDEF2 += 2*p-3
          AbCd0 += 2*p-3
          BcDe1 += 2*p-3
          if abcd1 == 4*(2*p-3) or bcde1 == 4*(2*p-3) or BCDE2 == 4*(2*p-3) or CDEF2 == 4*(2*p-3) or AbCd0 == 4*(2*p-3) or BcDe1 == 4*(2*p-3):
            w = p
        elif j == 0:
          abcd0 += 2*p-3
          bcde0 += 2*p-3
          CDEF2 += 2*p-3
          BcDe0 += 2*p-3
          if abcd0 == 4*(2*p-3) or bcde0 == 4*(2*p-3) or CDEF2 == 4*(2*p-3) or BcDe0 == 4*(2*p-3):
            w = p
      elif i == 6:
        if j == 5:
          defg5 += 2*p-3
          ABCD7 += 2*p-3
          DeFg2 += 2*p-3
          if defg5 == 4*(2*p-3) or ABCD7 == 4*(2*p-3) or DeFg2 == 4*(2*p-3):
            w = p
        elif j == 4:
          defg4 += 2*p-3
          ABCD7 += 2*p-3
          BCDE7 += 2*p-3
          DeFg1 += 2*p-3
          if defg4 == 4*(2*p-3) or ABCD7 == 4*(2*p-3) or BCDE7 == 4*(2*p-3) or DeFg1 == 4*(2*p-3):
            w = p
        elif j == 3:
          defg3 += 2*p-3
          ABCD7 += 2*p-3
          BCDE7 += 2*p-3
          CDEF7 += 2*p-3
          DeFg0 += 2*p-3
          if defg4 == 4*(2*p-3) or ABCD7 == 4*(2*p-3) or BCDE7 == 4*(2*p-3) or CDEF7 == 4*(2*p-3) or DeFg0 == 4*(2*p-3):
            w = p
        elif j == 2:
          defg2 += 2*p-3
          ABCD7 += 2*p-3
          BCDE7 += 2*p-3
          CDEF7 += 2*p-3
          dEfG5 += 2*p-3
          if defg2 == 4*(2*p-3) or ABCD7 == 4*(2*p-3) or BCDE7 == 4*(2*p-3) or CDEF7 == 4*(2*p-3) or dEfG5 == 4*(2*p-3):
            w = p
        elif j == 1:
          defg1 += 2*p-3
          BCDE7 += 2*p-3
          CDEF7 += 2*p-3
          dEfG4 += 2*p-3
          if defg1 == 4*(2*p-3) or BCDE7 == 4*(2*p-3) or CDEF7 == 4*(2*p-3) or dEfG4 == 4*(2*p-3):
            w = p
        elif j == 0:
          defg0 += 2*p-3
          CDEF7 += 2*p-3
          dEfG3 += 2*p-3
          if defg0 == 4*(2*p-3) or CDEF7 == 4*(2*p-3) or dEfG3 == 4*(2*p-3):
            w = p
      elif i == 0:
        if j == 5:
          abcd5 += 2*p-3
          ABCD1 += 2*p-3
          aBcD5 += 2*p-3
          if abcd5 == 4*(2*p-3) or ABCD1 == 4*(2*p-3) or aBcD5 == 4*(2*p-3):
            w = p
        elif j == 4:
          abcd4 += 2*p-3
          ABCD1 += 2*p-3
          BCDE1 += 2*p-3
          aBcD4 += 2*p-3
          if abcd5 == 4*(2*p-3) or ABCD1 == 4*(2*p-3) or BCDE1 == 4*(2*p-3) or aBcD4 == 4*(2*p-3):
            w = p
        elif j == 3:
          abcd3 += 2*p-3
          ABCD1 += 2*p-3
          BCDE1 += 2*p-3
          CDEF1 += 2*p-3
          aBcD3 += 2*p-3
          if abcd5 == 4*(2*p-3) or ABCD1 == 4*(2*p-3) or BCDE1 == 4*(2*p-3) or CDEF1 == 4*(2*p-3) or aBcD3 == 4*(2*p-3):
            w = p
        elif j == 2:
          abcd2 += 2*p-3
          ABCD1 += 2*p-3
          BCDE1 += 2*p-3
          CDEF1 += 2*p-3
          AbCd2 += 2*p-3
          if abcd5 == 4*(2*p-3) or ABCD1 == 4*(2*p-3) or BCDE1 == 4*(2*p-3) or CDEF1 == 4*(2*p-3) or AbCd2 == 4*(2*p-3):
            w = p
        elif j == 1:
          abcd1 += 2*p-3
          BCDE1 += 2*p-3
          CDEF1 += 2*p-3
          AbCd1 += 2*p-3
          if abcd5 == 4*(2*p-3) or BCDE1 == 4*(2*p-3) or CDEF1 == 4*(2*p-3) or AbCd1 == 4*(2*p-3):
            w = p
        elif j == 0:
          abcd0 += 2*p-3
          CDEF1 += 2*p-3
          AbCd0 += 2*p-3
          if abcd5 == 4*(2*p-3) or CDEF1 == 4*(2*p-3) or AbCd0 == 4*(2*p-3):
            w = p
      break
    if j == 0:
        print("Column full.")
        p = p%2+1
  print(dashes)
  print(board)
  print(dashes)
  print(labels)
  p = p%2+1
print("Player {} wins.".format(w))
