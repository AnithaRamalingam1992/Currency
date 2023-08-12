Money = int(input("Enter the amount: "))
if Money>200:
  print("Eat everything")
elif Money<200 and Money>=150:
  print("Meals,Snacks,Juice or Snacks and Juice or Meals")
elif Money<150 and Money>=100:
  print("Meals,Snacks,Juice or Meals or Snacks and Juice")
elif Money<100 and Money>=50:
  print("Snacks and Juice")
elif Money<50 and Money>=20:
  print("Juice")
else:
  print("Water")
