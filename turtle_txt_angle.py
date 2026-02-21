# save as turtle_txt_angle.py
import turtle

class Patch_txt_angle:
    def RawTurtleDOTwrite(self, arg, move=False, align="left", font=("Arial", 11, "normal"), txt_angle=0):
        if self.undobuffer:
            self.undobuffer.push(["seq"])
            self.undobuffer.cumulate = True
        end = self._write(str(arg), align.lower(), font, txt_angle)
        if move: x, y = self.pos() ; self.setpos(end, y)
        if self.undobuffer: self.undobuffer.cumulate = False
        
    def RawTurtleDOT_write(self, txt, align, font, txt_angle):
        item, end = self.screen._write(self._position, txt, align, font, self._pencolor, txt_angle)
        self.items.append(item)
        if self.undobuffer: self.undobuffer.push(("wri", item))
        return end
        
    def TurtleScreenBaseDOT_write(self, pos, txt, align, font, pencolor, txt_angle):
        x, y = pos ; x = x * self.xscale ; y = y * self.yscale
        anchor = {"left":"sw", "center":"s", "right":"se" }
        item = self.cv.create_text(x-1, -y, text = txt, anchor = anchor[align],
            fill = pencolor, font = font, angle = txt_angle)
        x0, y0, x1, y1 = self.cv.bbox(item)
        self.cv.update()
        return item, x1-1
        
import turtle

turtle.RawTurtle.write = Patch_txt_angle.RawTurtleDOTwrite
turtle.RawTurtle._write = Patch_txt_angle.RawTurtleDOT_write
turtle.TurtleScreenBase._write = Patch_txt_angle.TurtleScreenBaseDOT_write