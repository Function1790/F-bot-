from discord import *
from asyncio import *
from random import *
from re import *

token="NzQ2Mjg0NzA0MzAyNjI4OTQ0.Xz-Fyg.gXaYXfb5yCpvuukXltGQoCK4dO0"

lvl=0
formular="0"
value_a=0
value_b=0
value_c=0
client=Client()
following_name=[]

def argSplit(arg, findArg):
    args=split(" ",arg)
    for i in range(len(args)):
        if args[i].find(findArg)==-1:
            final=None
        else:
            return (args[i][args[i].find(findArg)+len(findArg):])
    return ""

def setValue(var_a):
    if var_a!="":
        try:
            test=eval(var_a)
            return var_a
        except Exception:
            return None

@client.event
async def on_ready():
    global lvl
    try:
        f=open('level.txt','r',encoding='utf-8')
        lvl=int(f.readline())
    except ValueError:
        lvl=0
    except Exception:
        f=open('level.txt','w',encoding='utf-8')
        f.write("0")
    await client.change_presence(activity=Game("파이썬"))
    print("Connect")

@client.event
async def on_message(msg):
    global formular
    global value_a, value_b, value_c
    global following_name

    text=msg.content
    name=str(msg.author)
    name=name[:name.find("#")]
    if name!="F(bot)":
        if text.find(" ")!=-1:
            empty=text.find(" ")
            cmd=text[:empty]
            arg=text[empty+1:]
        else:
            cmd=text
            arg=None
        
        for i in following_name:
            if i==name:
                await msg.channel.send(text)

        if text=="함수봇":
            await msg.channel.send("무슨 일이오")
        if text=="앙" or text=="앙?":
            await msg.channel.send("앙?")
        elif text.find("갈게")!=-1 or text.find("ㅂ")!=-1:
            await msg.channel.send("안녕히가세요!")
        elif text.find("잔다")!=-1 or text.find("잘게")!=-1:
            await msg.channel.send("{0}님 제 꿈꿔요♥!".format(name))
        elif text=="!help" or text=="!도움말":
            embed=Embed(title="도움말",color=0x0F73FF)
            embed.add_field(name="!embed name:[text] value:[text]",value="임베드를 생성합니다",inline=False)
            embed.add_field(name="!rect x:[value] y:[value] txt:[text]",value="사각형을 출력합니다.",inline=False)
            embed.add_field(name="!clab cnt:[value]",value="박수를 칩니다.",inline=False)
            embed.add_field(name="!calc [식]",value="식을 계산합니다.",inline=False)
            txt1="미지수 a,b,c가 포함이 가능합니다.\n"
            txt1+="!for set:[식] -> 식을 설정합니다.\n"
            txt1+="!for a:[value] ->a의 값을 설정합니다.\n"
            txt1+="!for b:[value] ->b의 값을 설정합니다.\n"
            txt1+="!for c:[value] ->b의 값을 설정합니다.\n"
            txt1+="ex)!for set:-3b*c/2a\n"
            txt1+="ex)!for a:2 b:5 c:2"
            embed.add_field(name="!for",value=txt1,inline=False)
            embed.add_field(name="!run",value="!for을 계산합니다.",inline=False)
            embed.add_field(name="!split txt:[text] arg:[text]",value="txt를 arg로 분할합니다.",inline=False)
            embed.add_field(name="!follow b:[true/false]",value="봇이 따라할 여부를 결정합니다.",inline=False)
            await msg.channel.send(embed=embed)
        elif text.find("안녕")!=-1 or text.find("하이")!=-1 or text.find("ㅎㅇ")!=-1:
            if name=="Terry":
                await msg.channel.send("제작자다!")
            elif name=="히공" or name=="heegong":
                await msg.channel.send("히공 바보!")
            else:
                await msg.channel.send("{0}님이당!".format(name))
        elif text.find("ㅇㅈ?")!=-1 or text.find("히공 바보")!=-1 :
            await msg.channel.send("인정!!".format(name))
        elif text.find("ㅗㅜㅑ")!=-1:
            await msg.channel.send("ㅗㅜㅑ...".format(name))
        if cmd=="!run":
            try:
                forResult=""
                formularB=formular.replace("+"," + ")
                formularB=formularB.replace("-"," - ")
                formularB=formularB.replace("*"," * ")
                formularB=formularB.replace("/"," / ")
                formularB=formularB.replace("^"," ** ")
                forSplit=split(" ",formularB)
                for i in range(len(forSplit)):
                    if forSplit[i]=="a":
                        forSplit[i]="1a"
                    elif forSplit[i]=="b":
                        forSplit[i]="1b"
                    elif forSplit[i]=="c":
                        forSplit[i]="1c"
                    forResult+=forSplit[i]
                formularB=forResult
                formularB=formularB.replace("a",("*{0}".format(value_a)))
                formularB=formularB.replace("b",("*{0}".format(value_b)))
                formularB=formularB.replace("c",("*{0}".format(value_c)))
                result=eval(formularB)
                await msg.channel.send("{0} = {1}".format(formular,result))
            except Exception:
                await msg.channel.send("연산 오류!!")
        if arg!=None:
            arg+=" "
            if cmd=="!embed":
                name=argSplit(arg, "name:")
                value=argSplit(arg, "value:")
                colorValue=randint(0,6)
                if colorValue==0:
                    color=0xFF0000
                elif colorValue==1:
                    color=0x00FF00
                elif colorValue==2:
                    color=0x0000FF
                elif colorValue==3:
                    color=0xFF00FF
                elif colorValue==4:
                    color=0xFFFF00
                elif colorValue==5:
                    color=0x00FFFF
                elif colorValue==6:
                    color=0x999999
                embed=Embed(title=name,description=value,color=color)
                await msg.channel.send(embed=embed)
            elif cmd=="!rect":
                text=""
                try:
                    x=int(argSplit(arg, "x:"))
                except ValueError:
                    x=1
                try:
                    y=int(argSplit(arg, "y:"))
                except ValueError:
                    y=1
                txt=argSplit(arg, "txt:")
                if txt=="":
                    txt="■"
                if x>20 or y>20 or x<1 or y<1:
                    await msg.channel.send("x또는 y는 20이하, 1이상이여야 해요!")
                    return 0
                for j in range(y):
                    for i in range(x):
                        text+=txt
                    text+="\n"
                await msg.channel.send(text)
            elif cmd=="!clab":
                try:
                    count=int(argSplit(arg,"cnt:"))
                except:
                    count=2
                if count>300 or count<1:
                    await msg.channel.send("cnt는 300이하, 1이상이여야 해요!")
                    return 0
                text=""
                for i in range(count):
                    text+="짝"
                await msg.channel.send(text)
            elif cmd=="!calc":
                try:
                    arg=arg.replace("^","**")
                    result=eval(arg)
                except Exception:
                    result="연산 오류!"
                await msg.channel.send("{0}".format(result))
            elif cmd=="!for":
                if arg!=None:
                    sets=argSplit(arg,"set:")
                    var_a=argSplit(arg,"a:").replace("^","**")
                    var_b=argSplit(arg,"b:").replace("^","**")
                    var_c=argSplit(arg,"c:").replace("^","**")
                    if sets!="":
                        formular=sets
                        await msg.channel.send("식 = {0}".format(formular))
                    if var_a!="":
                        before_a=setValue(var_a)
                        if before_a==None:
                            await msg.channel.send("값이 이상해요!")
                        else:
                            value_a=before_a
                            await msg.channel.send("a = {0}".format(value_a))
                    if var_b!="":
                        before_b=setValue(var_b)
                        if before_b==None:
                            await msg.channel.send("값이 이상해요!")
                        else:
                            value_b=before_b
                            await msg.channel.send("b = {0}".format(value_b))
                    if var_c!="":
                        before_c=setValue(var_c)
                        if before_c==None:
                            await msg.channel.send("값이 이상해요!")
                        else:
                            value_c=before_c
                            await msg.channel.send("c = {0}".format(value_c))
            elif cmd=="!split":
                try:
                    splited=argSplit(arg,"txt:")
                    spliting=argSplit(arg,"arg:")
                    result=split(spliting,splited)
                    await msg.channel.send(result)
                except Exception:
                    await msg.channel.send("예상치 못한 에러에요!")
            elif cmd=="!follow":
                TFbool=argSplit(arg, "b:")
                target=""
                if name=="Terry":
                    target=argSplit(arg, "target:").replace("[]"," ")
                nameF=name
                if target!="":
                    nameF=target
                if target=="all":
                    following_name=[]
                    await msg.channel.send("따라하기 목록을 초기화했어요!")
                if target=="show":
                    txt=""
                    if following_name==[]:
                        txt="아무도 없어요!"
                    else:
                        for i in following_name:
                            txt+=("%s//"%(i))
                    await msg.channel.send("{0}".format(txt))
                if TFbool=="true":
                    following_name.append(nameF)
                    await msg.channel.send("{0}님을 따라할게요!".format(nameF))
                if TFbool=="false":
                    for i in range(len(following_name)):
                        if following_name[i]==nameF:
                            del(following_name[i])
                            await msg.channel.send("{0}님을 그만 따라할게요!".format(nameF))
                            return 0
                    await msg.channel.send("{0}님은 따라하기 목록에 없어요!".format(nameF))

client.run(token)