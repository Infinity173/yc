import random  #产生随机模块random
decidedage=int(random.randint(1,30))
GameOver=0
for a in range(999):
    for i in range(3):
        ages = int(input('猜猜数是多大？'))
        if decidedage == ages:
            print('恭喜你，答对了')
            break
            pass
        elif ages > decidedage :
            print('猜大了哦')
            continue
        elif ages < decidedage :
            print('猜小了喔')
            continue
        else:
            print('信息识别错误')
    if decidedage == ages:
        break
    else:
      for b in range(999):
         change=input('请问您是否愿意继续？')
         if change=='Y' or change=='y':
                print('请您继续')
                break
         elif change=='N' or change=='n':
             GameOver=1
             break
         else:
            print('输入信息错误，请重新输入：')
            continue
    if GameOver==1:
          print('游戏结束')
          break
        
