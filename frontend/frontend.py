from tkinter import *
import subprocess,time
import views
import json
from publish import client

def get_scriptnames():
    data = views.get_scriptnames()["data"]
    payload = {"testing" : "django"}
    payload = json.dumps(payload)
    return data


def get_body(id):
    global current_body, current_id
    body = views.get_scriptbody(id)["body"]
    current_id = id
    current_body = body
    code_element.delete(1.0, END)
    code_element.insert(1.0, current_body)
    current_script_label.config(text = f'current_id = {current_id}')


def save_code():
    if current_id is not None:
        current_body=code_element.get("1.0",'end-1c')
        data={"id":current_id,"body":current_body}
        payload=json.dumps(data)
        client.publish("save_script",payload)
        status = views.save_script(current_id,current_body)["status"]
        update_message(status)
    else:
        update_message("error")
    

def run_code():
    if current_id is not None:
        current_body=code_element.get("1.0",'end-1c')
        temp_file = open("temp_file.py","w")
        temp_file.write(current_body)
        temp_file.close()
        start_time=time.time()
        s2=subprocess.run("py temp_file.py",text=True,capture_output=True)
        output=s2.returncode
        end_time=time.time()
        #print(start_time,end_time)
        if s2.returncode==0:
            status="success"
        else:
            status="error"

        data={"id":current_id, "starttime":start_time, "endtime":end_time, "output":output}
        payload=json.dumps(data)
        client.publish("save_log",payload)
        
        status_ = views.save_log(current_id,start_time,end_time,output)["status"]
        update_message(status)


def new_script():
    global row_count,script_elements
    current_body=code_element.get("1.0",'end-1c')
    name=name_box_entry.get()
    data={"body":current_body, "name":name}
    payload=json.dumps(data)
    client.publish("new_script",payload)
    res=views.new_script(name,current_body)
    status = res["status"]
    update_message(status)
    if status=="success":
        id=res["id"]
        row_count+=1
        label  = Label(frame1, text = id)
        button = Button(frame1, text = name, command = lambda id=id: get_body(id))
        delete_button = Button(frame1, text="delete", command = lambda id=id: delete_script(id))
        label.grid(row = row_count, column = 1, padx = 40)
        button.grid(row = row_count, column = 2, padx = 40)
        delete_button.grid(row = row_count, column = 3, padx = 40)
        script_elements.append([label,button,delete_button])


def delete_script(id):
    payload=dict({"id" : id})
    payload=json.dumps(payload)
    client.publish(f"delete_script/{id}",payload)
    status = views.delete_script(id)["status"]
    update_message(status)
    delete_all_ui()
    load_page()
        

def update_message(message):
    
    global message_label
    color=""
    if message == "success":
        color="green"
    else:
        color = "red"
        message = "error"
    message_label.config(text = message, foreground=color)
    # time.sleep(3)
    # message_label.config(text = "process", foreground="blue")


def load_page():
    global row_count,script_elements
    row_count = 1
    script_names=get_scriptnames()
    for i in script_names:
        row_count+= 1
        label  = Label(frame1, text = i[0])
        button = Button(frame1, text = i[1], command = lambda id=i[0]: get_body(id))
        delete_button = Button(frame1, text="delete", command = lambda id=i[0]: delete_script(id))
        label.grid(row = row_count, column = 1, padx = 40)
        button.grid(row = row_count, column = 2, padx = 40)
        delete_button.grid(row=row_count,column = 3, padx = 40)
        script_elements.append([label,button,delete_button])

def delete_all_ui():

    global script_elements
    for i in script_elements:
        i[0].grid_remove()
        i[1].grid_remove()
        i[2].grid_remove()
    script_elements=[]


root = Tk()
root.title('NETRMM')
script_names = []
current_id = None
current_body = ""
row_count=0
page_number=1


frame0 = Frame(root, height = 10)
frame1 = Frame(root, height = 300)
frame2 = Frame(root, height = 100)
frame3 = Frame(root, height = 300)
frame0.grid(row = 1, column = 1, pady=10)
frame1.grid(row = 2, column = 1, pady=50)
frame2.grid(row = 3, column = 1, pady=50)
frame3.grid(row = 4, column = 1)


message_label = Label(frame0, text="", font= 20)
message_label.grid()


current_script_label=Label(frame2,text=f'current_id = {current_id}')
save_button = Button(frame2, text = "Save", command = save_code)
run_button = Button(frame2, text = "Run", command = run_code)
save_as_new=Button(frame2,text="Save as New",command = new_script)
name_box_label=Label(frame2,text="New Script name")
name_box_entry=Entry(frame2)


code_element = Text(frame3)


current_script_label.grid(row=1,column=1,pady=10)
save_button.grid(row = 1, column = 2,pady=10)
run_button.grid(row = 1, column = 3,pady=10)
save_as_new.grid(row=2,column=3)
name_box_label.grid(row=2,column=1)
name_box_entry.grid(row=2,column=2)


code_element.grid()

label  = Label(frame1, text = "ID")
button = Label(frame1, text = "Name")
label.grid(row = row_count, column = 1, padx = 40,pady=20)
button.grid(row = row_count, column = 2, padx = 40, pady=20)

script_elements = []
row_count=1
load_page()
# print(script_elements,row_count)


root.mainloop()