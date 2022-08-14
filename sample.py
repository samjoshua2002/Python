import flet 
from flet import Page, Text , AppBar, colors,FloatingActionButton,icons,Column

def main(page:Page):
    page.title="Sanjay Team"
    page.horizontal_alignment="center"
    page.vertical_alignment="center"
    def onclick(e):
        changetext.value=int(changetext.value) + 1
        #print(changetext.value)
        page.update()


    f1=FloatingActionButton(text=" ",icon=icons.ADD,bgcolor=colors.BLUE,on_click=onclick)
    
    page.appbar= AppBar (
        title=Text("Counting The Touches ",size=30, color=colors.WHITE),
        bgcolor=colors.BLUE)
    page.floating_action_button=f1
    showText=Text("You have pushed the button this many times:",size=30, color=colors.BLUE)
    changetext=Text(value="0",size=40)
    page.add(Column([showText,changetext,],horizontal_alignment="center" ) )
    

flet.app(target=main) 