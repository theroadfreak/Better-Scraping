cssPath = "html body form#aspnetForm div#ns-wrapper div#ns-content.content div.full-content.catPage div.container div.row div.inner-content-box.inner div div#angularApp.ng-scope div.ng-scope div#mainContainer.catPage.ng-scope div.row div.col-lg-9.col-md-9.col-sm-8.col-fix-main"

cssPathAsList = cssPath.split(' ')
code = ""

for item in cssPathAsList:
    taraba = item.find("#")
    tocka = item.find(".")
    # print(taraba, "   ", item)
    if taraba != -1:
        element = item[0:taraba]
        item = item.replace(item[0:taraba+1], "")

        tocka = item.find(".")
        if tocka != -1:
            code += "pageSoup = pageSoup.find('{}',['id':'{}']) \n".format(
                element, item[0:tocka])
        else:
            code += "pageSoup = pageSoup.find('{}',['id':'{}']) \n".format(
                element, item[0:len(item)])
    elif tocka != -1:
        element = item[0:tocka]
        item = item.replace(item[0:tocka+1], "")

        classes = ""
        while(True):
            tocka = item.find(".")
            if tocka != -1:
                classes += "{} ".format(item[0:tocka])
                item = item.replace(item[0:tocka+1], "")

            else:
                code += "pageSoup = pageSoup.find('{}',['class':'{}{}']) \n".format(
                    element, classes, item)
                break
    else:
        code += "pageSoup = pageSoup.{}\n".format(item)

print(code)
