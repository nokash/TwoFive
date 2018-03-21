from db_connect import connection
from flask import request


def Content():
    
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
                            ]}


    return TOPIC_DICT


if __name__ == "__main__":
    x = Content()

    print(x["Basics"])

    for each in x["Basics"]:
        print(each[1])
