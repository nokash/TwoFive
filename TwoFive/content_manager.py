from db_connect import connection
from flask import request


def Content():

    TOPIC_DICT = {"Articles":[

                                ["ggfg","/ggfg/", "31"],
                                ["hvgvjjbhj","/hvgvjjbhj/", "38"],
                                ["sasdsadsaddsa","/sasdsadsaddsa/", "43"],
                                ["Conspiracy","/conspiracy/", "52"],
                                ["uyyyuu hhjbiui njjjj nmnmn ","/uyyyuu-hhjbiui-njjjj-nmnmn-/", "54"],
                                ["Arch","/arch/", "56"],
                                ["ttee","/ttee/", "62"],
                                ["ttetet","/ttetet/", "63"],
                                ["gyvbfhnijgfvbuhjmfvbh","/gyvbfhnijgfvbuhjmfvbh/", "64"],
                                ["tuugugg","/tuugugg/", "65"],
                                ["ydugydgydsyuydsyds","/ydugydgydsyuydsyds/", "67"]
                                ]}


    return TOPIC_DICT


if __name__ == "__main__":
    x = Content()

    print(x["Basics"])

    for each in x["Basics"]:
        print(each[1])
