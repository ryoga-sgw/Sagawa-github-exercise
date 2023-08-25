def on_forever():
    basic.show_icon(IconNames.EIGHTH_NOTE)
    basic.pause(500)
    basic.show_icon(IconNames.QUARTER_NOTE)
    basic.pause(500)
basic.forever(on_forever)
