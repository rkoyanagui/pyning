import math
import tkinter as tk
from math import pi


class CircleDraught(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack(side=tk.TOP, fill=tk.X)
        self.create_widgets()
        self.draw()

    def create_widgets(self):
        self.create_toolbar()
        self.canvas = tk.Canvas(self, width=1000, height=600, bg="white")
        self.canvas.pack()
        self.create_status_bar()

    def create_toolbar(self):
        self.toolbar = tk.Frame(self, relief=tk.SUNKEN, bd=1)

        centre_x_label = tk.Label(self.toolbar, text="Centre X:")
        centre_x_label.pack(side=tk.LEFT, padx=2, pady=2)
        self.centre_x_entry = tk.Entry(self.toolbar, width=10)
        self.centre_x_entry.pack(side=tk.LEFT, padx=2, pady=2)

        centre_y_label = tk.Label(self.toolbar, text="Centre Y:")
        centre_y_label.pack(side=tk.LEFT, padx=2, pady=2)
        self.centre_y_entry = tk.Entry(self.toolbar, width=10)
        self.centre_y_entry.pack(side=tk.LEFT, padx=2, pady=2)

        small_radius_label = tk.Label(self.toolbar, text="Small radius:")
        small_radius_label.pack(side=tk.LEFT, padx=2, pady=2)
        self.small_radius_entry = tk.Entry(self.toolbar, width=10)
        self.small_radius_entry.pack(side=tk.LEFT, padx=2, pady=2)

        big_radius_label = tk.Label(self.toolbar, text="Big radius:")
        big_radius_label.pack(side=tk.LEFT, padx=2, pady=2)
        self.big_radius_entry = tk.Entry(self.toolbar, width=10)
        self.big_radius_entry.pack(side=tk.LEFT, padx=2, pady=2)

        num_of_divisions_label = tk.Label(self.toolbar, text="Num. of divs.:")
        num_of_divisions_label.pack(side=tk.LEFT, padx=2, pady=2)
        self.num_of_divisions_entry = tk.Entry(self.toolbar, width=10)
        self.num_of_divisions_entry.pack(side=tk.LEFT, padx=2, pady=2)

        draw_btn = tk.Button(
            self.toolbar,
            text="Draw",
            command=self.draw)
        draw_btn.pack(side=tk.LEFT, padx=2, pady=2)

        self.toolbar.pack(side=tk.TOP, fill=tk.X)

    def create_status_bar(self):
        self.status_bar = tk.Frame(self, relief=tk.SUNKEN, bd=1)

        self.grid_size_text = tk.StringVar(
            value="cx=500, cy=300, r=200, R=200, num_of_divisions=30"
        )
        self.grid_size_label = tk.Label(self.status_bar,
                                        textvariable=self.grid_size_text)
        self.grid_size_label.pack(side=tk.LEFT, padx=2, pady=2)

        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def draw(self):
        cx = int(self.centre_x_entry.get() or 500)
        cy = int(self.centre_y_entry.get() or 300)
        r = int(self.small_radius_entry.get() or 200)
        R = int(self.big_radius_entry.get() or 200)
        num_of_divisions = int(self.num_of_divisions_entry.get() or 30)
        self.update_grid(cx, cy, r, R, num_of_divisions)
        self.canvas.delete("all")
        self.canvas.create_oval(
            [(cx - r, cy - r), (cx + r, cy + r)],
            outline="black"
        )

        very_small_angle = pi / 180
        small_angle = pi / num_of_divisions - very_small_angle
        big_angle = pi / num_of_divisions + very_small_angle
        offset = big_angle / 2
        c0 = (
            math.floor(cx + math.cos(offset) * r),
            math.floor(cy - math.sin(offset) * r)
        )
        inner_points = [(offset, c0)]
        for i in range(1, num_of_divisions * 2 + 1):
            step = big_angle
            if i % 2 == 0:
                step = math.floor(small_angle)
            angle = inner_points[i - 1][0] + step
            c1 = (
                math.floor(cx + math.cos(angle) * r),
                math.floor(cy - math.sin(angle) * r)
            )
            inner_points.append((angle, c1))

        small_angle = pi / num_of_divisions - very_small_angle
        big_angle = pi / num_of_divisions + very_small_angle
        offset = small_angle / 2
        outer_points = [(
            offset,
            (cx + math.cos(offset) * R, cy - math.sin(offset) * R)
        )]
        for i in range(1, num_of_divisions * 2 + 1):
            step = big_angle
            if i % 2 == 1:
                step = small_angle
            angle = outer_points[i - 1][0] + step
            outer_points.append((
                angle,
                (cx + math.cos(angle) * R, cy - math.sin(angle) * R)
            ))

        points = zip(inner_points, outer_points)
        for p in points:
            self.canvas.create_line([p[0][1], p[1][1]], fill="black")

    def update_grid(self, cx, cy, r, R, num_of_divisions):
        self.grid_size_text.set(
            "cx={}, cy={}, r={}, R={}, num_of_divisions={}".format(
                cx,
                cy,
                r,
                R,
                num_of_divisions
            )
        )


if __name__ == "__main__":
    app = CircleDraught()
    app.master.title("Circle")
    app.mainloop()
