import tkinter as tk

class SnakeSimulation(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("เกมงู")
        self.geometry("400x450")
        self.snake_matrix = [[0, 0], [0, 0], [0, 0], [0, 0]]

        self.canvas = tk.Canvas(self, width=400, height=400, bg="black")
        self.canvas.pack()

        self.draw_snake()

        self.x_plus_button = tk.Button(self, text="X+", command=self.move_x_plus)
        self.x_plus_button.pack(side=tk.LEFT)
        self.y_plus_button = tk.Button(self, text="Y+", command=self.move_y_plus)
        self.y_plus_button.pack(side=tk.LEFT)
        self.x_minus_button = tk.Button(self, text="X-", command=self.move_x_minus)
        self.x_minus_button.pack(side=tk.LEFT)
        self.y_minus_button = tk.Button(self, text="Y-", command=self.move_y_minus)
        self.y_minus_button.pack(side=tk.LEFT)
        self.increase_length_button = tk.Button(self, text="เพิ่มความยาว", command=self.increase_length)
        self.increase_length_button.pack(side=tk.LEFT)
        self.decrease_length_button = tk.Button(self, text="ลดความยาว", command=self.decrease_length)
        self.decrease_length_button.pack(side=tk.LEFT)

    def draw_snake(self):
        self.canvas.delete("all")
        for segment in self.snake_matrix:
            x, y = segment
            self.canvas.create_rectangle(x * 20, y * 20, (x + 1) * 20, (y + 1) * 20, fill="green")

    def move_x_plus(self):
        head_x = self.snake_matrix[0][0] + 1
        if head_x < 20:  # Check for boundary
            self.snake_matrix.insert(0, [head_x, self.snake_matrix[0][1]])
            self.snake_matrix.pop()
            self.draw_snake()

    def move_y_plus(self):
        head_y = self.snake_matrix[0][1] + 1
        if head_y < 20:  # Check for boundary
            self.snake_matrix.insert(0, [self.snake_matrix[0][0], head_y])
            self.snake_matrix.pop()
            self.draw_snake()

    def move_x_minus(self):
        head_x = self.snake_matrix[0][0] - 1
        if head_x >= 0:  # Check for boundary
            self.snake_matrix.insert(0, [head_x, self.snake_matrix[0][1]])
            self.snake_matrix.pop()
            self.draw_snake()

    def move_y_minus(self):
        head_y = self.snake_matrix[0][1] - 1
        if head_y >= 0:  # Check for boundary
            self.snake_matrix.insert(0, [self.snake_matrix[0][0], head_y])
            self.snake_matrix.pop()
            self.draw_snake()

    def increase_length(self):
        last_segment = self.snake_matrix[-1]
        self.snake_matrix.append([last_segment[0], last_segment[1]])
        self.draw_snake()

    def decrease_length(self):
        if len(self.snake_matrix) > 1:
            self.snake_matrix.pop()
            self.draw_snake()

if __name__ == "__main__":
    app = SnakeSimulation()
    app.mainloop()
    