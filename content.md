# 作品介绍
## 一、作品代码
```python
import random  #产生随机模块random
age=int(random.randint(1,30))
GameOver=0
for a in range(999):
    for i in range(3):
        ages = int(input('猜猜这个数多大？'))
        if age == ages:
            print('恭喜你，答对了')
            break
            pass
        elif ages > age :
            print('对不起，猜大了哦')
            continue
        elif ages < age :
            print('对不起，猜小了喔')
            continue
        else:
            print('信息识别错误')
    if age == ages:
        break
    else:
      for b in range(999):
         change=input('您已经答错3次了，请问您是否愿意继续？')
         if change=='Y' or change=='y':
                print('请您继续')
                break
         elif change=='N' or change=='n':
             GameOver=1
             break
         else:
            print('输入信息错误，，请重新输入')
            continue
    if GameOver==1:
          print('游戏结束')
          break
```

## 二、作品阐述
这是一个比较简单的程序，运行之后是一个小的猜数游戏，该程序在你猜之前会内定一个数字，然后你进行猜测，系统会提示你猜大了或者猜小了，有无限个机会，直到你猜对了为止，是不是很有意思！
