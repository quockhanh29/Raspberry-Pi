
print("電圧:1 , 電流:2 , 抵抗: 3 計算問題")
type = int(input())

if type == 1 :
    print("電流をを入力 A")
    I = input()
    print("抵抗をを入力 ohm")
    R = input()
    E = int(R)*int(I)
elif type == 2:
    print("電圧をを入力 V")
    E = input()
    print("抵抗をを入力 ohm")
    R = input()
    I = int(E)/int(R)
else :
    print("電圧をを入力 V")
    E = input()
    print("電流をを入力 ohm")
    I = input()
    R = int(E) / int(I)

print("電圧の値は ", E,"V")
print("電流の値は ", I, "A")
print("抵抗の値は ", R, "Ωです")
