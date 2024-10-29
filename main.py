from telefono import Telefono
from menu import mostrar_menu_principal

def main():
    telefono = Telefono(
        id=1,
        nombre="Mi Telefono",
        modelo="Modelo X",
        sistema_operativo="Android",
        sistema_operativo_version="11.0",
        RAM=4,
        cap_almacenamiento=64,
        num_telefono=1234567890,
        codigo_desbloqueo="1234"
    )
    mostrar_menu_principal(telefono)

if __name__ == "__main__":
    main()
