def ai_number_guesser() :
 print("Number Guesser")
 print("Lets play a number guesser game.I will predict the number you guess ")
 low =int(input("What should be the lowset number I can guess?  "))
 high =int(input("What should be the highest number I can guess?  "))
 attempts=0
 while low<=high :
  guess=(low+high)//2
  attempts+=1
  print(f"My guess is {guess} ")
  feedback=input("Press (h) for higher, (l) for lower and (c) for correct  ").lower()
  if feedback=='c':
    print(f" yay I have gussed your number {guess} in {attempts} attempts ")
    break
  elif feedback=='h':
    low=guess+1
    print("I will guess higher number this time")
  elif feedback=='l':
    high=guess-1
    print("I will guess lower next time")
  else:
    print("Please press 'h' for higher, 'l' for lower and 'c' for correct. ")
 if low>high:
   print("Did something went wrong")
ai_number_guesser()

   
 
   



    