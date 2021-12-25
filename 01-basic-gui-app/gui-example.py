from guizero import App, Text, Box, PushButton, Picture

# Create a function to show the text, image, enable the hide button and disable the show button::
def show_greeting():
    greeting_box.visible = True
    hide_button.enabled = True
    show_button.enabled = False

# Create a function to hide the text, image, enable the show button and disable the hide button:
def hide_greeting():
    greeting_box.visible = False
    hide_button.enabled = False
    show_button.enabled = True

# Create the main container for the app, 
# set the title of the app and set the background to black:
app = App(title="Hello World")
app.bg = "black"

# Create a box to contain the message and world_image variables so that they can be addresseed as one.
greeting_box = Box(app, align = "top", visible = False)

# Create a text box:
message = Text(greeting_box, text="Hello World!", size = 26, color = "white")

# Import an image:
world_image = Picture(greeting_box, image = "world.png", height = 400, width = 400)

# Create a box for the two buttons to be be contained in:
buttons_box = Box(app, width = "fill", align = "bottom")

# Create a button that will call the show_text function to make the text visible:
show_button = PushButton(buttons_box, show_greeting, text = "Show", align = "left")

# Create a button that will call the hide_text function to make the text invisible:
hide_button = PushButton(buttons_box, hide_greeting, text = "Hide", align = "right", enabled = False)

# Run the app:
app.display()