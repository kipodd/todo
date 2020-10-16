import PySimpleGUI as sg

todos = ["Plan the family trip to Europe",
         "Buy flowers for mom's birthday",
         "Send tax report"]
done = ["Finish todo app"]

sg.theme("Reddit")

layout = [
    [sg.Text("To Do:")],
    [sg.Listbox(values=todos, size=(64, 7), key="todos")],
    [sg.Text("Done:")],
    [sg.Listbox(values=done, size=(64, 7), key="done")],
    [
        sg.Button(" Add ", key="add"),
        sg.Button(" Edit ", key="edit"),
        sg.Button(" Delete ", key="delete"),
        sg.Button(" Mark as Done ", key="mark_done"),
        sg.Button(" Check everything, I need a beer! ", key="mark_all_done")
    ]
]

window = sg.Window("To Do", layout)
while True:
    event, values = window.Read()

    if event == "add" and (new_task := sg.popup_get_text("Add task:", no_titlebar=True)) \
            and new_task not in set(todos):
        todos.append(new_task)
        window["todos"].Update(values=todos)
    elif event == "edit" and (selected := values["todos"] and values["todos"][0]) \
            and (new_task := sg.popup_get_text("Edit task:", no_titlebar=True)) \
            and new_task not in set(todos):
        todos = [t if t != selected else new_task for t in todos]
        window["todos"].Update(values=todos)
    elif event == "delete" and (selected := values["todos"] and values["todos"][0]):
        todos.remove(selected)
        window["todos"].Update(values=todos)
    elif event == "mark_done" and (selected := values["todos"] and values["todos"][0]):
        todos.remove(selected)
        done.append(selected)
        window["todos"].Update(values=todos)
        window["done"].Update(values=done)
    elif event == "mark_all_done":
        done += todos
        todos = []
        window["todos"].Update(values=todos)
        window["done"].Update(values=done)
    elif event == None:
        break

window.Close()
