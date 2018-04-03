from db_connect import connection
from flask import request


def Content():
<<<<<<< HEAD

    TOPIC_DICT = {"Articles":[

                                ["ggfg","/ggfg/", "31"],
                                ["ggfg","/ggfg/", "32"],
                                ["ggfg","/ggfg/", "33"],
                                ["ggfg","/ggfg/", "34"],
                                ["ggfg","/ggfg/", "35"],
                                ["ggfg","/ggfg/", "36"],
                                ["ggfg","/ggfg/", "37"],
                                ["hvgvjjbhj","/hvgvjjbhj/", "38"],
                                ["hvgvjjbhj","/hvgvjjbhj/", "39"],
                                ["hvgvjjbhj","/hvgvjjbhj/", "40"],
                                ["hvgvjjbhj","/hvgvjjbhj/", "41"],
                                ["hvgvjjbhj","/hvgvjjbhj/", "42"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/", "43"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/", "44"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/", "45"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/", "46"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/", "47"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/", "48"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/", "49"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/", "50"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/", "51"],
                                ["Conspiracy","/conspiracy/", "52"],
                                ["Conspiracy","/conspiracy/", "53"],
                                ["uyyyuu hhjbiui njjjj nmnmn ","/uyyyuu-hhjbiui-njjjj-nmnmn-/", "54"],
                                ["uyyyuu hhjbiui njjjj nmnmn ","/uyyyuu-hhjbiui-njjjj-nmnmn-/", "55"],
                                ["Arch","/arch/", "56"]
=======
    
    TOPIC_DICT = {"Articles":[
                                ["ggfg","/ggfg/"],
                                ["ggfg","/ggfg/"],
                                ["ggfg","/ggfg/"],
                                ["ggfg","/ggfg/"],
                                ["ggfg","/ggfg/"],
                                ["ggfg","/ggfg/"],
                                ["ggfg","/ggfg/"],
                                ["hvgvjjbhj","/hvgvjjbhj/"],
                                ["hvgvjjbhj","/hvgvjjbhj/"],
                                ["hvgvjjbhj","/hvgvjjbhj/"],
                                ["hvgvjjbhj","/hvgvjjbhj/"],
                                ["hvgvjjbhj","/hvgvjjbhj/"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/"],
                                ["Conspiracy","/conspiracy/"],
                                ["Conspiracy","/conspiracy/"],
                                ["uyyyuu hhjbiui njjjj nmnmn ","/uyyyuu-hhjbiui-njjjj-nmnmn-/"],
                                ["uyyyuu hhjbiui njjjj nmnmn ","/uyyyuu-hhjbiui-njjjj-nmnmn-/"],
                                ["Arch","/arch/"]
>>>>>>> 41f9199593e797a1bf1ffe0da30159d7fb849d10
                            ]}


    return TOPIC_DICT


if __name__ == "__main__":
    x = Content()

    print(x["Basics"])

    for each in x["Basics"]:
        print(each[1])
