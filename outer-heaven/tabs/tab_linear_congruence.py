import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from models.linear_congruence import LinearCongruence
from models.pseudo_random_number_visualizer import PseudoRandomNumberVisualizer


class TabLinearCongruence(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.results = [] 
        self.create_widgets()

    def create_widgets(self):
        vcmd = (self.register(lambda P: P.isdigit() or P == ""), '%P')

        title = tk.Label(self, text="CONGRUENCIA LINEAL", font=("Arial", 16, "bold")) 
        title.grid(row=0, column=0, pady=(0, 0), padx=(75, 75))

        formula = tk.Label(self, text="Ri=xi/m-1 E[0,1]", font=("Arial", 14))
        formula.grid(row=0, column=0, pady=(50, 0))
        
        self.iteration_label = tk.Label(self, text="Número de Iteraciones:") 
        self.iteration_label.grid(row=0, column=0, pady=(100, 0)) 
        self.iteration_entry = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.iteration_entry.grid(row=0, column=0, pady=(150, 0))

        self.seed_label = tk.Label(self, text="xo:")  
        self.seed_label.grid(row=1, column=0, pady=(0, 0))
        self.seed_entry = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.seed_entry.grid(row=1, column=0, pady=(50, 0))

        self.k_label = tk.Label(self, text="k:")  
        self.k_label.grid(row=1, column=0, pady=(100, 0)) 
        self.k_entry = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.k_entry.grid(row=1, column=0, pady=(150, 0))
        
        self.c_label = tk.Label(self, text="c:")  
        self.c_label.grid(row=1, column=0, pady=(200, 0)) 
        self.c_entry = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.c_entry.grid(row=1, column=0, pady=(250, 0))
        
        self.g_label = tk.Label(self, text="g:")  
        self.g_label.grid(row=1, column=0, pady=(300, 0)) 
        self.g_entry = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.g_entry.grid(row=1, column=0, pady=(350, 0))
        
        self.min_label = tk.Label(self, text="Min:")  
        self.min_label.grid(row=2, column=0, pady=(0, 0)) 
        self.min_entry = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.min_entry.grid(row=2, column=0, pady=(50, 0))

        self.max_label = tk.Label(self, text="Max:") 
        self.max_label.grid(row=2, column=0, pady=(100, 0)) 
        self.max_entry = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.max_entry.grid(row=2, column=0, pady=(150, 0))

        generate_button = tk.Button(self, text="Generar Números", command=self.generate_numbers) 
        generate_button.grid(row=3, column=0, pady=(100, 0))
        generate_button.config(bg="black", fg="white")
        
        save_button = tk.Button(self, text="Guardar Resultados", command=self.save_results) 
        save_button.grid(row=4, column=0, pady=(25, 0)) 
        save_button.config(bg="green", fg="white")

        self.tree = ttk.Treeview(self, columns=("i", "xi", "Ri", "Ni"), show="headings", height=30)
        self.tree.heading("i", text="i")
        self.tree.heading("xi", text="xi")
        self.tree.heading("Ri", text="Ri")
        self.tree.heading("Ni", text="Ni")
        self.tree.grid(row=0, column=1, rowspan=5, padx=10, pady=10, sticky="nsew")

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=0, column=2, rowspan=5, sticky="ns", padx=(0, 10))
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.tag_configure('repeated', background='red')

    def validate_fields(self):
        if not self.seed_entry.get() or not self.iteration_entry.get() or not self.k_entry.get() or not self.c_entry.get() or not self.g_entry.get() or not self.min_entry.get() or not self.max_entry.get():
            messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos.") 
            return False
        if int(self.iteration_entry.get()) <= 0:
            messagebox.showwarning("Advertencia", "El número de iteraciones debe ser mayor que cero.")
            return False
        return True

    def generate_numbers(self):
        if not self.validate_fields():
            return

        seed = int(self.seed_entry.get())
        num_iterations = int(self.iteration_entry.get())
        k = int(self.k_entry.get())
        c = int(self.c_entry.get())
        g = int(self.g_entry.get())
        min_val = float(self.min_entry.get())
        max_val = float(self.max_entry.get())

        generator = LinearCongruence(seed, num_iterations, k, c, g, min_val, max_val)
        self.results = generator.generate()

        for row in self.tree.get_children():
            self.tree.delete(row)

        ri_values = [Ri for _, Ri, _ in self.results]
        repeated = {Ri for Ri in ri_values if ri_values.count(Ri) > 1}

        for i, (xi, Ri, Ni) in enumerate(self.results, start=1):
            if Ri in repeated:
                self.tree.insert("", "end", values=(i, xi, Ri, Ni), tags=('repeated',))
            else:
                self.tree.insert("", "end", values=(i, xi, Ri, Ni))
                
        visualizer = PseudoRandomNumberVisualizer(self.results)
        visualizer.plot_collage()

    def save_results(self):
        if not self.results:
            messagebox.showwarning("Advertencia", "No hay resultados para guardar.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        
        if file_path:
            with open(file_path, 'w') as f:
                seen = set()
                for _, _, Ni in self.results:
                    if Ni not in seen:
                        f.write(f"{Ni}\n")
                        seen.add(Ni)
            
            os.startfile(file_path)
