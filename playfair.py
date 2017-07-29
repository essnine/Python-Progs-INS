def main():
  inpstr = input("Enter key: ")
  inpstr2 = reverse(inpstr)
  arr = matrixGen(inpstr2)
  #print(arr)
  printmatrix(arr)
  code = input("Enter message: ")
  encode(code)


def matrixGen(key):
  arr = ["a ","b ","c ","d ","e ","f ","g ","h ","i ","j ","k ","l ","m ","n ","o ","p ","q ","r ","s ","t ","u ","v ","w ","x ","y ","z ","0 ","1 ","2 ","3 ","4 ","5 ","6 ","7 ","8 ","9 "]
  print(key)
  for i in range(0,len(key)):
    for j in range(0,len(arr)):
      if str(key[i]+" ") == str(arr[j]):
        #print(key[i])
        arr.pop(j)
        arr.insert(0, key[i]+" ")
  return(arr)

def printmatrix(arr):
  print("",arr[0:6],"\n",arr[6:12],"\n",arr[12:18],"\n",arr[18:24],"\n",arr[24:30],"\n",arr[30:36])
  arr2 = (arr[0:6],arr[6:12],arr[12:18],arr[18:24],arr[24:30],arr[30:36])
  #print(arr2)
  return(arr2)

def encode(inp):
  mess = []
  #adds input to array
  for e in inp:
    msg.append(e)

  #removes spaces

  for unused in range(len(mess)):
      if " " in mess:
        mess.remove(" ")

  #adding x after repeated 1st letter
  i = 0
  for e in range (len(mess)/2):
    if mess[i] ==  mess[i+1]:
      mess.insert(i+1, "x")
    i = i+2

  if len(mess)%2 == 1:
    mess.append("x")

  #grouping to sets of 2

  i = 0
  new = []
  for x in range(1,len(mess)/2+1):
    new.append(mess[i:i+2])
    i=i+2
  print(new)
  return(new)



def reverse(text):
    if len(text) <= 1:
        return text

    return(reverse(text[1:]) + text[0])

if __name__ == '__main__':
  main()