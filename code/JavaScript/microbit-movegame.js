// Code for MicroBit
// You can move "_" by button A to left and button B to right
// And I know, its very simple thing, but I want to post it here, because it was actually one of my first "programs", that I ever did.
// Requirements: MicroBit, LCD1602
input.onButtonPressed(Button.A, function () {
    if (dot_started == 0) {
        I2C_LCD1602.clear()
        I2C_LCD1602.ShowString("-", 0, 0)
        dot_started = 1
    } else {
        I2C_LCD1602.shl()
    }
})
input.onButtonPressed(Button.AB, function () {
    if (started == 1) {
        I2C_LCD1602.clear()
        I2C_LCD1602.ShowString("Sleep Mode...", 0, 0)
        I2C_LCD1602.ShowString("zzz...", 0, 1)
        basic.pause(2000)
        I2C_LCD1602.clear()
        I2C_LCD1602.BacklightOff()
        started = 0
    } else {
        I2C_LCD1602.clear()
        I2C_LCD1602.BacklightOn()
        dot_started = 0
        started = 1
        I2C_LCD1602.ShowString("MoveGame | Use", 0, 0)
        I2C_LCD1602.ShowString("A and B buttons", 0, 1)
    }
})
input.onButtonPressed(Button.B, function () {
    if (dot_started == 0) {
        I2C_LCD1602.clear()
        I2C_LCD1602.ShowString("-", 0, 0)
        dot_started = 1
    } else {
        I2C_LCD1602.shr()
    }
})
let started = 0
let dot_started = 0
I2C_LCD1602.LcdInit(39)
dot_started = 0
started = 1
I2C_LCD1602.ShowString("MoveGame | Use", 0, 0)
I2C_LCD1602.ShowString("A and B buttons", 0, 1)
