import flet as ft 
from datetime import datetime



def main(page: ft.Page):
    page.title = "My first_application on Flet"
    page.theme_mode = ft.ThemeMode.DARK
    
    greeting_txt = ft.Text("Hello, Flet!", size=30, color=ft.Colors.WHITE)
    
    name_input = ft.TextField(label="Enter your name")
    history = ft.Text("History")
    history_list = []
    current_time = datetime.now().hour
    
    
    def change_theme(_):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            greeting_txt.color == ft.Colors.WHITE
            greeting_txt.color = ft.Colors.BLACK
            
        else:
            page.theme_mode = ft.ThemeMode.DARK
            greeting_txt.color = ft.Colors.WHITE
        page.update()
     
        
    def greeting_time():
        
        current_hour = datetime.now().hour
        if 6 <= current_hour < 12:
            return "Доброе утро"
        elif 12 <= current_hour < 18:
            return "Добрый день"
        elif 18 <= current_hour < 24:
            return "Добрый вечер"
        elif 0 <= current_hour < 6:
            return "Доброй ночи"
        return "Привет"    
    
        
    def on_button_click(_):
        name = name_input.value.strip()
        if name:
           
            
            greeting_txt.value = f"Hello! {greeting_time()},{name}"
            update_button.text
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history_list.append(f"{timestamp} {name}")
            history.value = "History\n" + "\n".join(history_list)
            
        else:
            greeting_txt.value = "please Honey, enter your name!"
            
            
            print(greeting_txt.value)
        page.update()
        
    def clear_history(_):
        history_list.clear()
        history.value = "History has been cleared"
        page.update()
        
    theme_button = ft.ElevatedButton(text="Change theme", on_click=change_theme, icon=ft.Icons.TOGGLE_ON)    
    name_input = ft.TextField(label="Enter your name", autofocus=True)
    update_button = ft.ElevatedButton("Update", on_click=on_button_click)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    
    # page.add(theme_button, greeting_txt, name_input, update_button, history, clear_button)

    page.add(ft.Row([theme_button, clear_button], alignment=ft.MainAxisAlignment.SPACE_AROUND),
             ft.Row([greeting_txt], alignment=ft.MainAxisAlignment.CENTER),
             ft.Row([name_input, update_button], alignment=ft.MainAxisAlignment.CENTER),
             ft.Row([history], alignment=ft.MainAxisAlignment.CENTER))

ft.app(target=main, view=ft.WEB_BROWSER)
