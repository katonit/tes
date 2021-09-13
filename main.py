def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_icon(IconNames.EIGTH_NOTE)
    else:
        basic.clear_screen()
basic.forever(on_forever)
