import os
import customtkinter as ctk
from PIL import Image


# ----------------------------
# Configuración global
# ----------------------------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Ventana principal
        self.title("Sistemas de Administración")
        self.geometry("600x350")
        self.resizable(False, False)
        self.configure(fg_color="#EDEDED")

        # Cargar iconos
        self.icono_inventario = self.cargar_icono("icons/inventario.png", (64, 64))
        self.icono_ventas = self.cargar_icono("icons/ventas.png", (64, 64))

        # Construcción de la interfaz
        self.crear_titulo()
        self.crear_area_tarjetas()
        self.crear_footer()

    def cargar_icono(self, ruta, size):
        if os.path.exists(ruta):
            imagen = Image.open(ruta)
            return ctk.CTkImage(light_image=imagen, dark_image=imagen, size=size)
        return None

    def crear_titulo(self):
        frame_titulo = ctk.CTkFrame(
            self,
            height=45,
            corner_radius=0,
            fg_color="#F4E5B8"
        )
        frame_titulo.pack(fill="x")

        lbl_titulo = ctk.CTkLabel(
            frame_titulo,
            text="Sistemas de Administración",
            font=("Courier New", 20, "bold"),
            text_color="black"
        )
        lbl_titulo.pack(side="left", padx=15, pady=8)

    def crear_area_tarjetas(self):
        frame_principal = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        frame_principal.pack(expand=True, fill="both", pady=20)

        contenedor = ctk.CTkFrame(
            frame_principal,
            fg_color="transparent"
        )
        contenedor.place(relx=0.5, rely=0.5, anchor="center")

        tarjeta_inventario = self.crear_tarjeta(
            parent=contenedor,
            titulo="Inventario",
            icono=self.icono_inventario,
            comando=self.abrir_inventario
        )
        tarjeta_inventario.grid(row=0, column=0, padx=35)

        tarjeta_ventas = self.crear_tarjeta(
            parent=contenedor,
            titulo="Ventas",
            icono=self.icono_ventas,
            comando=self.abrir_ventas
        )
        tarjeta_ventas.grid(row=0, column=1, padx=35)

    def crear_tarjeta(self, parent, titulo, icono, comando):
        tarjeta = ctk.CTkFrame(
            parent,
            width=160,
            height=170,
            corner_radius=15,
            fg_color="#F8F8F8",
            border_width=1,
            border_color="#D9D9D9"
        )
        tarjeta.grid_propagate(False)

        boton_icono = ctk.CTkButton(
            tarjeta,
            text="",
            image=icono,
            width=90,
            height=90,
            corner_radius=15,
            fg_color="#F4E5B8",
            hover_color="#EAD89C",
            border_width=1,
            border_color="#D4A72C",
            command=comando
        )
        boton_icono.pack(pady=(20, 10))

        lbl_texto = ctk.CTkLabel(
            tarjeta,
            text=titulo,
            font=("Courier New", 16, "bold"),
            text_color="black"
        )
        lbl_texto.pack()

        return tarjeta

    def crear_footer(self):
        footer = ctk.CTkFrame(
            self,
            height=28,
            corner_radius=0,
            fg_color="#F5F5F5"
        )
        footer.pack(fill="x", side="bottom")

        lbl_footer = ctk.CTkLabel(
            footer,
            text="© 2026 Admin Store",
            font=("Arial", 11),
            text_color="gray20"
        )
        lbl_footer.pack(side="left", padx=10, pady=4)

    def abrir_inventario(self):
        print("Abriste Inventario")

    def abrir_ventas(self):
        print("Abriste Ventas")


if __name__ == "__main__":
    app = App()
    app.mainloop()