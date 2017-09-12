# coding ：utf-8

weather_dict = {}
history_dict = {}
with open('C:/Users/Administrator/Py101-004/Chap1/resource/weather_info.txt' , 'r', encoding= 'utf-8') as file :
    for info in file.readlines():
        key = info.split(',')[0]
        #print(city)
        value = info.split(',')[1].strip('\n')
        weather_dict[key] = value
#print(weather_dict)

while True:
    user_input = input('请输入指令或您要查询的城市名：')
    if user_input in weather_dict.keys():
        value = weather_dict[user_input]
        history_dict[user_input]= value
        print ("%s的天气为:%s" %(user_input, value))
        #print("{}的天气为：{}" .formate(user_input,value))
    elif user_input == "help" or user_input == "h":
        print(
        """
        输入城市名，查询该城市的天气；
        输入 help, 获取帮助文档；
        输入 history, 获取查询历史；
        输入 quit, 退出天气查询系统。
        """
        )
    elif user_input == "history":
        for his in history_dict.keys():
            print (his, history_dict[his])
    elif user_input=="quit" or user_input== "q":
        for his in history_dict:
            print (his, history_dict[his])
        break
    else:
        print("没有该城市的信息")
