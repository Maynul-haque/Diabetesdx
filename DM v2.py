symptoms= int(input("if symptom present, enter 1; otherwise 0: "))
fbs =float(input('enter FBS here: '))
rbs =float(input('enter RBS here: '))
thabf = float(input('enter 2HABF here: '))

if symptoms==1 and (fbs>=7 or rbs>=11.1 or thabf>=11.1):
    print('you have Diabetes!')
elif symptoms==0 and fbs>=7 and (rbs>=11.1 or thabf>=11.1):
    print('you have Diabetes!')
elif symptoms==0 and fbs>=7 and (thabf>=11.1 or rbs>=11.1):
    print('you have Diabetes!')
elif symptoms==0 and rbs>=11.1 and (thabf>=11.1 or fbs>=7):
    print('you have Diabetes!')
elif symptoms==0 and 6.1>=fbs<=6.9 and rbs
else:
  print('No Diabetes: ')
