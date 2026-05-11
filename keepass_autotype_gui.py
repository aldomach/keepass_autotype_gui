import tkinter as tk

def button_click(shortcut):
    text_field.insert(tk.END, shortcut)

root = tk.Tk()
root.title("KeepassXC Autotyper Facilitator GUI - aldo.net.ar")
root.resizable(False, False)  # Impedir cambiar el tamaño de la ventana
 


# Crear botones para cada atajo
shortcuts = [
    "{CLEARFIELD}", "{USERNAME}", "{PASSWORD}", "{TAB}", "{ENTER}", "{TOTP}", "{SPACE}", "{ESC}",
    "{DELAY=X}", "{DELAY X}", "{UP}", "{DOWN}", "{LEFT}", "{RIGHT}",
    "{INSERT} ", "{DELETE} ", "{HOME} ", "{END} ", "{PGUP} ", "{PGDN} ", "{BACKSPACE}",
    "{PICKCHARS}", "{TITLE}", "{URL}", "{NOTES}", "{CAPSLOCK} ", "{S:<ATTRIBUTE_NAME>}",
    "{LEFTBRACE}", "{RIGHTBRACE}", "{<KEY> X}", "{MODE=VIRTUAL}", "+", "^", "%", "#", "{F2}", "{F5}", "{F12}", "{F16}","{PICKCHARS}",
]

# Dividir los atajos en 4 columnas
columns = 8
rows = (len(shortcuts) + columns - 1) // columns

# Set the width of all buttons to 20
button_width = 14

for i in range(rows):
    for j in range(columns):
        index = i * columns + j
        if index < len(shortcuts):
            shortcut = shortcuts[index]
            button = tk.Button(root, text=shortcut, command=lambda s=shortcut: button_click(s), width=button_width)
            button.grid(row=i, column=j, padx=5, pady=5)

# Crear campo de texto para mostrar el atajo seleccionado
text_field = tk.Text(root, height=5, width=120)
text_field.grid(row=rows, columnspan=columns, padx=10)

# Agregar scroll al campo de texto
scrollbar = tk.Scrollbar(root, command=text_field.yview)
scrollbar.grid(row=rows, column=columns, sticky='ns')
text_field.config(yscrollcommand=scrollbar.set)

# Crear campo de texto para las instrucciones
instructions = """
{TAB}, {ENTER}, {SPACE}, 
{INSERT},{DELETE}, {HOME},      Presiona la tecla correspondiente del teclado:
{END}, {PGUP}, {PGDN}, 
{BACKSPACE}, {CAPSLOCK}, {ESC}

{UP}, {DOWN}, {LEFT}, {RIGHT}   Presiona la tecla de flecha correspondiente:        
{F1}, {F2}, ..., {F16}          Presiona F1, F2, etc.:                            
{LEFTBRACE}, {RIGHTBRACE}       Presiona { o }, respectivamente:                    
{<TECLA> X}                     Repite <TECLA> X veces (por ejemplo, {SPACE 5} inserta cinco espacios):
{DELAY=X}       Establece un retraso entre pulsaciones de teclas de X milisegundos: 
{DELAY X}       Pausa la escritura durante X milisegundos:
{CLEARFIELD}    Borra el campo de entrada: 
{PICKCHARS}     Selecciona caracteres específicos de la contraseña de un diálogo:"""

instructions_field = tk.Text(root, height=15, width=120, bg='ghost white')
instructions_field.insert(tk.END, instructions)
instructions_field.grid(row=rows+1, columnspan=columns, padx=10, pady=10)

# Agregar scroll al campo de texto de instrucciones
instructions_scrollbar = tk.Scrollbar(root, command=instructions_field.yview)
instructions_scrollbar.grid(row=rows+1, column=columns, sticky='ns')
instructions_field.config(yscrollcommand=instructions_scrollbar.set)

# Agregar margen de 15 píxeles en la parte superior e inferior de la ventana
root.wm_geometry("985x530+15+15")

root.mainloop()
