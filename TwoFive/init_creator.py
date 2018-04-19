from content_manager import Content

TOPIC_DICT = Content()

FUNC_TEMPLATE = '''

@app.route(TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][1], methods = ["GET", "POST"])
def CURRENTTITLE():
    url = TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][1]
    id = TOPIC_DICT["CURRENTTOPIC"][CURRENTINDEX][2]
    Post = postlist(id)
    flash(id)
    flash(Post)
    return render_template("CURRENTHTML",TOPIC_DICT=TOPIC_DICT, Post=Post)

 '''


for each_topic in TOPIC_DICT:
    #print(each_topic)

    index_counter = 0
    for eachele in TOPIC_DICT[each_topic]:
        try:
            CURRENTHTML = (eachele[1]+'.html').replace("/","")
            CURRENTTOPIC = each_topic
            CURRENTTITLE = eachele[0].replace(" ","").replace("-","_").replace(")","").replace("(","").replace(".","").replace("!","").replace(":","-").replace("'","")
            CURRENTINDEX = str(index_counter)
            NEXTINDEX = str(index_counter + 1)
            index_counter += 1

            print( FUNC_TEMPLATE.replace("CURRENTTOPIC",CURRENTTOPIC).replace("CURRENTINDEX",CURRENTINDEX).replace("CURRENTTITLE",CURRENTTITLE).replace("CURRENTHTML",CURRENTHTML).replace("NEXTINDEX",NEXTINDEX) )

        except Exception as e:
            print(str(e))



            template_save = open(savePath,"w")
            template_save.write(saveData)
            template_save.close()
        except Exception as ex:
            print(str(ex))
