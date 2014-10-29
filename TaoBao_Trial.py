import time, os, sys
from uiautomator import device as d

def select_product(product_x, product_y):
    # #########################
    # You to change here to select which branch to try
    #here i select Tech
    #d.click(kind_x, kind_y)  #Problem here
    #time.sleep(5)
    ###select  product
    print product_x
    print product_y
    time.sleep(5)
    d.click(product_x, product_y)
    time.sleep(10)

    d.click(575, 1828)
    time.sleep(5)

    d.click(560, 820)
    time.sleep(8)

    d.click(560, 1855)
    time.sleep(8)
    ##finish for once

    d.press("back")
    time.sleep(1)
    d.press("back")
    time.sleep(1)
    d.press("back")
    print("Done")


def launch_tb():  # cling position method
    d.screen.on()
    time.sleep(1)
    os.system("adb shell am force-stop com.taobao.taobao")
    time.sleep(1)
    d.press("home")
    d.swipe(120, 1110, 900, 1110)

    d(text="shopping").click()
    time.sleep(1)
    # launch TB
    d.click(225, 1300)
    time.sleep(8)

    #click Trial
    d.click(950, 900)
    time.sleep(8)
    #click Te She Dao Gou
    d.click(300, 300)
    time.sleep(8)
    #click Free to try
    d.click(930, 1105)
    time.sleep(10)


def launch_tb_activity():  # using activity method
    d.screen.on()
    time.sleep(1)
    os.system("adb shell am force-stop com.taobao.taobao")
    time.sleep(1)
    os.system("adb shell am start -n com.taobao.taobao/com.taobao.tao.welcome.Welcome")
    time.sleep(10)
    # click Trial
    d.click(950, 900)
    time.sleep(8)
    #click Te She Dao Gou
    d.click(300, 300)
    time.sleep(8)
    #click Free to try
    d.click(930, 1105)
    #d.click()
    time.sleep(10)
    print ("finish launch")
    #after this expression it stay on


def tb_coin():
    #completed this function
    launch_tb_activity()
    time.sleep(10)
    d.click(700, 860)
    time.sleep(9)
    print("TaoBao Coin")
    exit_tb()


def apply_one(kind_x, kind_y):
    # apply for 4 production
    dis_x = 540
    dis_y= 850
    base_x = 270
    base_y = 644
    d.click(kind_x, kind_y)
    time.sleep(5)
    select_product(base_x, base_y)
    select_product(base_x + dis_x, base_y)
    select_product(base_x, base_y + dis_y)
    select_product(base_x + dis_x, base_y + dis_y)
    #add drag down action
    d.drag(270,1494,270,750,steps=200)
    select_product(base_x, base_y)
    select_product(base_x + dis_x, base_y)
    select_product(base_x, base_y + dis_y)
    select_product(base_x + dis_x, base_y + dis_y)


def exit_tb():
    time.sleep(1)
    os.system("adb shell am force-stop com.taobao.taobao")
    time.sleep(1)

def test():
    launch_tb_activity()
    Facial_x = 338
    Facial_y = 270
    # apply_one(Facial_x,Facial_y)

    Cloth_x = 551
    Cloth_y = 270
    #apply_one(Cloth_x,Cloth_y)

    Tech_x = 820
    Tech_y = 270
    #apply_one(Tech_x,Tech_y)

    time.sleep(5)
    d.swipe(900, 270, 10, 270)
    time.sleep(8)

    Eletronic_x = 108
    Eletronic_y = 270
    apply_one(Eletronic_x, Eletronic_y)

    House_x = 270
    House_y = 270
    apply_one(House_x, House_y)

    time.sleep(2)
    d.press("home")
    print("Done")


def usage():
    print("Usage: python TaoBao_Trail.py [arg1,arg2,arg3,arg4.....]")
    print("arg=digital,facial,electron,house,cloth,others")
    exit()


def tech():
    launch_tb_activity()
    print("tech")
    x = 820
    y = 270
    apply_one(x, y)
    exit_tb()

def cloth():
    launch_tb_activity()
    print("cloth")
    x = 551
    y = 270
    apply_one(x, y)
    exit_tb()

def facial():
    launch_tb_activity()
    print("facial")
    x = 338
    y = 270
    apply_one(x, y)
    exit_tb()

def electron():
    launch_tb_activity()
    print("electron")
    x = 108
    y = 270
    d.swipe(900, 270, 10, 270)
    time.sleep(2)
    apply_one(x, y)
    exit_tb()

def house():
    d.swipe(900, 270, 10, 270)
    time.sleep(2)
    launch_tb_activity()
    print("house")
    x = 270
    y = 270
    apply_one(x, y)
    exit_tb()

def others():
    d.swipe(900, 270, 10, 270)
    time.sleep(2)
    launch_tb_activity()
    print("others")
    x = 820
    y = 270
    apply_one(x, y)
    exit_tb()


def start():
    if len(sys.argv) == 1:
        usage()

    for arg in sys.argv[1:]:
        if arg == "tech":
            tech()
        if arg == "cloth":
            cloth()
        if arg == "facial":
            facial()
        if arg == "electron":
            electron()
        if arg == "house":
            house()
        if arg == "others":
            others()


if __name__ == "__main__":
    print("Start working for MI3")
    start()
    tb_coin()
        

