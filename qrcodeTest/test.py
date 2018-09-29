import qrcode
from datetime import datetime
from PIL import Image


def qrecodeWithUrl(content:str):
    image = qrcode.make(content)
    now = datetime.now()
    timeStr = datetime.strftime(now,'%Y%m%d%H%M%S%s')
    imageName = timeStr+".png"
    image.save(imageName)

qrecodeWithUrl("就在昨晚将近11点钟的时候，在中国湖南长沙，来自中国河南的重量级拳手张志磊（20-0，16KO）不负众望，3回合KO了来自美国的拳击悍将唐-海恩斯沃斯（15-3-1，13KO），成功拿下职业生涯第20场胜利，张志磊也凭借本场比赛的胜利，将自己的战绩提升至20场全胜16场KO对手，力压我国拳击名将“龙王”张君龙（19-0，19KO），成为中国重量级拳击第一人。在比赛的第三回合，张志磊发动了最后的总攻，拳头如雨点般砸在了对手的身体和头部，用解说员的话来形容就是风中摇曳的雨竹。张志磊最后把对手逼到了围绳边缘，组合拳狂轰乱炸，最后将海恩斯沃斯打得摇摇欲坠，场裁果断终止了比赛。")