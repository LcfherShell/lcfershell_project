import os

class Home:
  def __init__(self, pages, attrb, frm):
      self.pages = pages
      self.attrb = attrb
      self.frm   = frm
  def home(self):
     if self.frm == 0 and self.attrb == 0 :
        return '{}, {}={}, {}={}'.format(self.pages, self.frm ,self.frm, self.attrb,self.attrb)
     elif self.frm == 0:
        return '{}, {}={}'.format(self.pages, self.frm ,self.frm)
     elif self.attrb == 0:
        return '{}, {}={}'.format(self.pages, self.attrb ,self.attrb)
     else:
        return '{}'.format(self.pages)
ome = Home('index.html', 'core', 'form').home()
print ("render_template("+ome+")")

