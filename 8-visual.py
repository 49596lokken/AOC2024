f = open("8.txt").read()

from random import randint

import tkinter
import time

def isIn(pos, g):
    return pos.real < len(g) and pos.imag < len(g[0]) and pos.real >=0 and pos.imag >=0

class Visualisation:
    def __init__(self, f, colours):
        self.square_size = 16

        self.root = tkinter.Tk()

        self.root.geometry(f"{self.square_size*(len(f)+1)}x{10+self.square_size*(len(f[0])+1)}")
        self.canvas = tkinter.Canvas(height=self.square_size*len(f),width=self.square_size*len(f[0]))
        self.nodes = {w:[] for w in waves}

        

        self.antinodes = set()
        self.colours = colours

        for i in range(len(f)):
            for j in range(len(f[i])):
                if f[i][j] in colours:
                    self.nodes[f[i][j]].append(complex(i, j))
                    self.canvas.create_rectangle(i*self.square_size, j*self.square_size, (i+1)*self.square_size, (j+1)*self.square_size, fill=self._from_rgb(colours[f[i][j]]))
                    self.canvas.create_text((i+1/2)*self.square_size, (j+1/2)*self.square_size, text=f[i][j])

        self.all_nodes = set()

        for w in self.nodes:
            for node in self.nodes[w]:
                self.all_nodes.add(node)



        self.canvas.create_oval(0, 0, self.square_size, self.square_size, fill="red")
        self.canvas.create_oval((self.square_size)*(len(f)-1), self.square_size*(len(f[0])-1), self.square_size*len(f), self.square_size*len(f[0]), fill="red")

        self.canvas.pack()

        self.sequence = []
        self.calculate_sequence()



    def calculate_sequence(self):
        for w in waves:
            for i, node in enumerate(self.nodes[w]):
                for node2 in self.nodes[w][i+1:]:
                    #antinodes.add((node2, w))
                    an1 = 2*node - node2
                    an2 = 2*node2 - node

                    while isIn(an1, f):
                        self.sequence.append((an1, self._from_rgb(self.colours[w]), node, node2))
                        an1 += node - node2
                    while isIn(an2, f):
                        self.sequence.append((an2, self._from_rgb(self.colours[w]), node, node2))
                        an2 += node2 - node

    def _from_rgb(self, rgb):
        """translates an rgb tuple of int to a tkinter friendly color code
        """
        return "#%02x%02x%02x" % rgb   


    def draw(self):
        lastp1 = 0
        lastp2 = 0
        parent1 = None
        parent2 = None
        for antinode, colour, p1, p2 in self.sequence:
            parentChange = False
            if lastp1 != p1:
                parentChange = True
                lastp1 = p1
                if parent1 is not None:
                    self.canvas.delete(parent1)
                parent1 = self.canvas.create_oval(self.square_size*p1.real, 
                                                  self.square_size*p1.imag, 
                                                  self.square_size*(p1.real+1), 
                                                  self.square_size*(p1.imag+1), 
                                                  fill=None,
                                                  outline="black",
                                                  width=3)
                
            if lastp2 != p2:
                parentChange = True
                lastp2 = p2
                if parent2 is not None:
                    self.canvas.delete(parent2)
                parent2 = self.canvas.create_oval(self.square_size*p2.real, 
                                                  self.square_size*p2.imag, 
                                                  self.square_size*(p2.real+1), 
                                                  self.square_size*(p2.imag+1), 
                                                  fill=None,
                                                  outline="black",
                                                  width=3)


            if not antinode in self.all_nodes:
                self.canvas.create_rectangle(self.square_size*antinode.real, 
                                            self.square_size*antinode.imag, 
                                            self.square_size*(antinode.real+1), 
                                            self.square_size*(antinode.imag+1), 
                                            fill=colour)
            if parentChange:
                self.root.after(500)         
            

            self.canvas.pack()
            self.root.update()
            self.root.after(1)

    def run(self):
        self.root.after(1000, self.draw)
        self.root.mainloop()
        


waves = set(f) - set(".")

f = f.splitlines()




colours = {w:(tuple(randint(0,255) for _ in range(3))) for w in waves}

Visualisation(f, colours).run()