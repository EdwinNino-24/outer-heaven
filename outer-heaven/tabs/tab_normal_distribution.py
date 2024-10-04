import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from models.normal_distribution import NormalDistribution
from models.pseudo_random_number_visualizer import PseudoRandomNumberVisualizer


class TabNormalDistribution(ttk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.results = [] 
        self.create_widgets()

    def create_widgets(self):
        vcmd = (self.register(lambda P: P.isdigit() or P == ""), '%P')

        title = tk.Label(self, text="DISTRIBUCIÓN NORMAL", font=("Arial", 16, "bold")) 
        title.grid(row=0, column=0, pady=(0, 0), padx=(75, 75))

        self.mu_label = tk.Label(self, text="Media:")  
        self.mu_label.grid(row=1, column=0, pady=(0, 0))
        self.mu_entry = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.mu_entry.grid(row=1, column=0, pady=(50, 0))
        
        self.sigma_label = tk.Label(self, text="Desviación Estándar:")  
        self.sigma_label.grid(row=1, column=0, pady=(100, 0))
        self.sigma_entry = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.sigma_entry.grid(row=1, column=0, pady=(150, 0))
        
        self.iteration_label = tk.Label(self, text="Número de Iteraciones:") 
        self.iteration_label.grid(row=2, column=0, pady=(0, 0)) 
        self.iteration_entry = tk.Entry(self, validate="key", validatecommand=vcmd)
        self.iteration_entry.grid(row=2, column=0, pady=(50, 0))

        generate_button = tk.Button(self, text="Generar Números", command=self.generate_numbers) 
        generate_button.grid(row=3, column=0, pady=(0, 0))
        generate_button.config(bg="black", fg="white")
        
        save_button = tk.Button(self, text="Guardar Resultados", command=self.save_results) 
        save_button.grid(row=4, column=0, pady=(0, 0)) 
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
        if not self.mu_entry.get() or not self.sigma_entry.get() or not self.iteration_entry.get():
            messagebox.showwarning("Advertencia", "Todos los campos deben estar llenos.") 
            return False
        if int(self.iteration_entry.get()) <= 0:
            messagebox.showwarning("Advertencia", "El número de iteraciones debe ser mayor que cero.")
            return False
        return True

    def generate_numbers(self):
        if not self.validate_fields():
            return

        mu = int(self.mu_entry.get())
        sigma = int(self.sigma_entry.get())
        num_iterations = int(self.iteration_entry.get())

        generator = NormalDistribution(mu, sigma, num_iterations)
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
