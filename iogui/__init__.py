import tkinter


def ioform(
        form_name='Simple input-output form',
        input_label_name='Input',
        output_label_name='Output',
        execute_button_text='Execute'
):
    def decorator(logic):
        def wrapper(*args, **kwargs):
            window = tkinter.Tk()
            input_label = tkinter.Label(window,text=str(input_label_name)+':')
            input_label.grid(row=0, column=0)
            input_text = tkinter.Text(window, wrap=tkinter.WORD)
            input_text.grid(row=1, column=0)
            output_label = tkinter.Label(window,text=str(output_label_name)+':')
            output_label.grid(row=0, column=1)
            output_text = tkinter.Text(window, wrap=tkinter.WORD)
            output_text.grid(row=1, column=1)

            def execute():
                result = str(logic(input_text.get('1.0',tkinter.END), *args, **kwargs))
                output_text.delete('1.0', tkinter.END)
                output_text.insert('1.0',result)
            execute_button = tkinter.Button(window, text=str(execute_button_text), command=execute)
            execute_button.grid(row=2, column=0, columnspan=2)
            window.mainloop()
        return wrapper
    return decorator