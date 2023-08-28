panNumber = 7890125634
panNumber = str(panNumber)
flags = []
for ctr in range (0,10):
    flags.append(False)
for char in num:
    flags [  int(char) ] = True
for flag in flags:
    if flags [ flag ] ==False:
        print('Not a PanDigital')
        break
else:
    print("PanDigital")
